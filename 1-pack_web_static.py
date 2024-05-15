#!/usr/bin/python3
"""Generate a tarball for web deployment"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Tarballs web_static, store in versions, return archive path"""
    local("mkdir -p versions")
    now = datetime.now()
    time_string = now.strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(time_string)
    res = local("tar -cvzf versions/{} web_static".format(name), capture=True)
    if res.return_code == 0:
        return "versions/{}".format(name)

