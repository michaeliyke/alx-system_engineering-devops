#!/usr/bin/python3
"""Deleting all the release archives except the most recent one of N more"""
from pathlib import Path
from datetime import datetime

dep = __import__("3-deploy_web_static")
deploy = dep.deploy
do_deploy = dep.do_deploy
do_pack = dep.do_pack


def do_clean(number=0):
    """Ceanup the archive files except the most recent one or N more"""
    dates = []
    base = Path("./versions")
    for file_name in base.iterdir():
        date_str = file_name.stem.replace("web_static_", "")
        dates.append(datetime.strptime(date_str, "%Y%m%d%H%M%S"))
    dates.sort(reverse=True)

    try:
        number = int(number)
    except ValueError:
        return False

    number = 1 if number == 0 or number == 1 else number
    if number < 0 or number >= len(dates):
        return False
    for date in dates[number:]:
        date_str = datetime.strftime(date, "%Y%m%d%H%M%S")
        name = "./versions/web_static_{}.tgz".format(date_str)
        print("Deleting: {}".format(name))
        Path(name).unlink()

