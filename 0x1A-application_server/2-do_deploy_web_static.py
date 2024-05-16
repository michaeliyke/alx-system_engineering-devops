#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import env, run, put
from pathlib import Path

env.user = "ubuntu"
env.hosts = ["18.204.16.105", "18.234.145.122"]


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    path = Path(archive_path)
    release = "/data/web_static/releases/{}".format(path.stem)
    latest = "/data/web_static/current"  # symlink to lastest release
    if not path.exists():
        return False

    # upload to the temp dir of each server
    try:
        put(archive_path, f"/tmp/{path.name}")
        # uncompress to /data/web_static/releases/archive_name
        run(f"mkdir -p {release}")
        run("sudo chown -R ubuntu:ubuntu /data/")
        # run(f"rm -rf {release}/*")
        run(f"tar -xzf /tmp/{path.name}  -C {release} --strip-components=1")
        # run(f"mv {release}/web_static/* {release}")
        # run(f"rmdir {release}/web_static")
        run(f"rm -f /tmp/{path.name}")  # delete archive from /tmp/
        run(f"rm -rf {latest}")  # recreate the symlink current
        run(f"ln -s {release} {latest}")
    except Exception:
        return False
    return True

