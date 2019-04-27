#!/usr/bin/python
from Alfred import Tools
import os
import sys

def get_appid(app):
    cmd = "osascript -e 'id of app \"" + app + "\"'"
    resp = os.popen(cmd).read().splitlines()
    resp = resp[0] if len(resp) > 0 else None
    return resp

def duti(appid,ext):
    resp = os.system("/usr/local/bin/duti -s " + appid + " " + ext + " all")
    return True if resp == 0 else False

query = Tools.getArgv(1)
[app,ext] = query.split('=')

app_id = get_appid(app)
if app_id is not None:
    resp = duti(app_id,ext)
else:
    resp = False

if resp:
    sys.stdout.write("%s succesfully assigned to %s" % (ext,app))
else:
    sys.stdout.write("Unabled to assign %s to %s" % (ext,app))