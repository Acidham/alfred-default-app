#!/usr/bin/python
import os
import Alfred

def get_assinged_app(ext):
    resp = os.popen("/usr/local/bin/duti -x " + ext).read().splitlines()
    return resp

ext = Alfred.Tools.getArgv(1) 
if not(ext.startswith('.')):
    ext = '.' + ext

assigned_app = get_assinged_app(ext)
wf = Alfred.Items()
if len(assigned_app) == 0:
    wf.setItem(
        title='%s is not assigned to an App' % ext,
        subtitle="Continue?",
        arg=ext
    )
    wf.setIcon('proceed.png','icon')
    wf.addItem()
    wf.setItem(
        title='Don\'t Continue?',
        arg='QUIT'
    )
    wf.setIcon('stop.png','icon')
    wf.addItem()
else:
    wf.setItem(
        title='\"%s\" is assigned to \"%s\"' % (ext,assigned_app[0]),
        subtitle='Continue?',
        arg=ext
    )
    wf.setIcon('proceed.png','icon')
    wf.addItem()
    wf.setItem(
        title='Don\'t Continue?',
        arg='QUIT'
    )
    wf.setIcon('stop.png','icon')
    wf.addItem()

wf.write()

