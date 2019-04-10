#!/usr/bin/python3
"""delete old archives"""
from fabric.api import env, hosts, local, run
from fabric.context_managers import lcd, cd


env.hosts = ['35.237.253.193', '35.231.141.38']


def do_clean(number=0):
    if number is 0:
        number = 1
    with lcd("versions/"):
        local("ls -t | tail -n+{} | xargs rm".format(number))
    with cd("/data/web_static/releases"):
        run("ls -t | tail -n+{} | xargs rm".format(number))
