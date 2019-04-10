#!/usr/bin/python3
"""delete old archives"""
from fabric.api import env, hosts, local, run
from fabric.context_managers import lcd, cd


env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'
env.hosts = ['35.237.253.193', '35.231.141.38']


def do_clean(number=0):
    """clean old archives"""
    if number is 0 or 1:
        number = 2
    with lcd("versions/"):
        local("ls -1t | tail -n+{} | xargs rm -f".format(number+1))
    with cd("/data/web_static/releases"):
        run("ls -1t | tail -n+{} | xargs rm -rf".format(number+1))
