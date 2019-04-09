#!/usr/bin/python3
"""distribute archive to web-server"""
from fabric.api import run
from fabric.api import put
from fabric.api import sudo
from fabric.api import hosts, env
import os


env.hosts = ['35.237.253.193', '35.231.141.38']


def do_deploy(archive_path):
    exists = os.path.isfile('{}'.format(archive_path))
    if not exists:
        return False
    try:
        put("versions/web_static_2019490105.tgz", "/tmp/")
        run("rm -rf /data/web_static/releases/web_static_2019490105/")
        run("mkdir -p /data/web_static/releases/web_static_2019490105")
        run("tar xzf /tmp/web_static_2019490105.tgz -C \
/data/web_static/releases/web_static_2019490105")
        run("mv /data/web_static/releases/web_static_2019490105/web_static/* \
        /data/web_static/releases/web_static_2019490105/")
        sudo("rm -f /tmp/web_static_2019490105.tgz")
        sudo("rm -rf /data/web_static/releases/web_static_2019490105/ \
web_static/")
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/web_static_2019490105 \
/data/web_static/current")
        return True
    except Exception as e:
        return False
