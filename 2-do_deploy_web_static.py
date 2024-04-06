#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import env, run, put
from pathlib import Path

env.user = "ubuntu"
env.hosts = ["18.204.16.105", "18.234.145.122"]


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    path = Path(archive_path)
    # env.hosts = ["18.234.145.122"]
    # Local file archive_path doesn't exist, return false
    if not path.exists():
        return False

    # upload to the temp dir of each server
    try:
        put(archive_path, "/tmp")
        release = "/data/web_static/releases/{}".format(path.stem)
        current = "/data/web_static/current"

        # uncompress to /data/web_static/releases/archive_name
        run(f"mkdir -p {release}")
        run("chown -R ubuntu:ubuntu /data/")
        run(f"rm -rf {release}/*")
        run(f"tar -xzf /tmp/{path.name}  -C {release}")
        run(f"mv {release}/web_static/* {release}")
        run(f"rmdir {release}/web_static")
        # delete archive from /tmp/
        run(f"rm -f /tmp/{path.name}")
        # recreate the symlink /data/web_static/current and point to archive_name
        run(f"rm -f {current}")
        run(f"ln -s {release} {current}")
    except:
        return False
    return True
