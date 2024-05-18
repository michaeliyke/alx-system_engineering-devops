#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from pathlib import Path
from fabric.api import env

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    path = Path(archive_path)
    if not archive_path or not path.is_file():
        return False

    return do_deploy(archive_path)

