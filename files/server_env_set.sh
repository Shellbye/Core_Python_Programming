#!/bin/bash

chmod +x install.sh
./install.sh


# nginx & git
apt-get install -y nginx
apt-get install -y git
apt-get install -y build-essential
apt-get install -y zliblg-dev
apt-get install -y libsqlite3-dev
apt-get install -y libreadline6-dev
apt-get install -y libgdbm-dev
apt-get install -y libbz2-dev
apt-get install -y tk-dev
apt-get install -y vim


# pip & django & uwsgi
apt-get install -y python-pip
echo -n "Please input your Django version:"
read d_version
pip install Django==$d_version
pip install uwsgi
# uwsgi need south to work...
pip install South

# needed before pip install some package
aptitude install -y python-dev
apt-get install -y libevent-dev


# pip install
echo -n "Please input your pip package, separated by black space:"
read pip_package
pip install $pip_package


cd /etc/nginx/
mkdir django
cd django
echo -n "Please input your Repository url:"
read url
git clone $url


echo -n "Please input your project name:"
read p_name
cd $p_name

echo -n "Please input your nginx conf file name:"
read conf_name
ln -s /etc/nginx/django/$p_name/$conf_name /etc/nginx/sites-enabled/


echo -n "Please input your uwsgi file name:"
read uwsgi_name
mkdir /var/log/uwsgi/
touch /var/log/uwsgi/$p_name.log

uwsgi --ini /etc/nginx/django/$p_name/$uwsgi_name
service nginx restart
