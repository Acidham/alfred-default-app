#!/usr/bin/env python3

import os
import shutil
import sys

from Alfred3 import Tools


def get_appid(app):
    cmd = "osascript -e 'id of app \"" + app + "\"'"
    resp = os.popen(cmd).read().splitlines()
    resp = resp[0] if len(resp) > 0 else None
    return resp


def duti(appid, ext):
    duti_app = shutil.which('duti')
    if duti_app is None:
        return False
    resp = os.system(f"{duti_app} -s " + appid + " " + ext + " all")
    return True if resp == 0 else False


query = Tools.getArgv(1)
[app, ext] = query.split('=')

app_id = get_appid(app)
if app_id is not None:
    resp = duti(app_id, ext)
else:
    resp = False

if resp:
    sys.stdout.write(f"{ext} succesfully assigned to {app}")
else:
    sys.stdout.write(f"Unabled to assign {ext} to {app}")
