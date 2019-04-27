#!/usr/bin/python

import os
import Alfred
import sys


def app_list(q):
    """ Generates as sorted list of App Names in /Applications folder
    
    Arguments:
        q {string} -- Search String
    
    Returns:
        list -- Sorted list of App Names in /Applications
    """
    file_list = os.listdir('/Applications')
    sorted_file_list = sorted([os.path.splitext(a)[0] for a in file_list if a.endswith('.app')])
    if q != str():
        sorted_file_list = [n for n in sorted_file_list if n.lower().startswith(q.lower())] 
    return sorted_file_list


query = Alfred.Tools.getArgv(1)
wf = Alfred.Items()
for app in app_list(query):
    wf.setItem(
        title=app,
        subtitle="Continue to assign %s?" % app,
        arg=app
    )
    wf.setIcon('/Applications/' + app + '.app','fileicon')
    wf.addItem()
if not app_list(query):
    wf.setItem(
        title="Nothing Found!",
        subtitle='No App found beginning with: "%s"' %query,
        valid=False
    )
    wf.addItem()
wf.write()