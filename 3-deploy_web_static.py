#!/usr/bin/python3
"""distribute archive to web-servers"""
from datetime import datetime
from fabric.api import put
from fabric.api import sudo
from fabric.api import hosts, env
from fabric.api import local
import os


env.hosts = ['35.237.253.193', '35.231.141.38']


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


def do_deploy(archive_path):
    """deploy on server"""
    a_list = archive_path.split("/")
    filename = a_list[-1]
    extension_list = filename.split(".")
    no_extension = extension_list[0]
    exists = os.path.isfile('{}'.format(archive_path))
    if not exists:
        return False
    try:
        put(archive_path, "/tmp/")
        sudo("rm -rf /data/web_static/releases/" + no_extension)
        sudo("mkdir -p /data/web_static/releases/" + no_extension)
        sudo("tar xzf /tmp/" + filename + " -C " +
             "/data/web_static/releases/" + no_extension)
        sudo("mv -f /data/web_static/releases/" +
             no_extension + "/web_static/* /data/web_static/releases/" +
             no_extension)
        sudo("rm -f /tmp/" + filename)
        sudo("rm -rf /data/web_static/releases/" +
             no_extension + "web_static/")
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/" + no_extension +
             " /data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """deploy archives on web-servers"""
    path = do_pack()
    if path is None:
        return False
    status = do_deploy(path)
    return (status)
