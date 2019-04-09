#!/usr/bin/python3
"""compress files"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """create tarball"""
    now = datetime.now()
    local("mkdir -p versions")
    name = "web_static_" + str(now.year) + str(now.month) + str(now.day)\
           + str(now.hour) + str(now.minute) + str(now.second) + ".tgz"
    local("tar czfv {} web_static".format(name))
    local("mv {} versions".format(name))
    exists = os.path.isfile('versions/{}'.format(name))
    if (exists):
        return(os.path.abspath("versions/{}".format(name)))
    return None
