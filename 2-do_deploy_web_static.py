#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import env, run, put
from pathlib import Path

env.user = "ubuntu"
env.hosts = ["18.204.16.105", "18.234.145.122"]


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    path = Path(archive_path)
    if not path.exists():  # archive_path doesn't exist, return false
        return False

    release = "/data/web_static/releases/{}".format(path.stem)
    symlink = "/data/web_static/current"
    try:
        # upload to the temp dir of each server
        put(archive_path, "/tmp")
        # uncompress to /data/web_static/releases/archive_name
        run(f"mkdir -p {release}")
        run(f"rm -rf {release}/*")
        run(f"tar -xzf /tmp/{path.name}  -C {release}")
        run(f"mv {release}/web_static/* {release}")
        run(f"rmdir {release}/web_static")
        # delete archive from /tmp/
        run(f"rm /tmp/{path.name}")
        # recreate the symlink to point to current release
        run(f"rm {symlink}")
        run(f"ln -s {release} {symlink}")
    except:
        return False
    return True
