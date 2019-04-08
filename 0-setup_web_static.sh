#!/usr/bin/env bash
# configure web servers for deployment
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo 'butter' > /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo echo "server {
    listen 80 default_server;
    location / {
             add_header X-Served-By 494-web-01;
    }
    location /hbnb_static {
             alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-enabled/default

sudo service nginx restart
