#!/bin/bash
BGreen='\e[1;32m'
normal=`tput sgr0`


echo -e "${BGreen}"
echo -e "================================"
echo -e "==  1/4 INSTALL ENVIRONMENT   =="
echo -e "================================"
echo -e "\033[0m${normal}"
virtualenv -p /usr/bin/python2.7 venv


echo -e "${BGreen}"
echo -e "================================"
echo -e "==  2/4 INSTALL REQUIREMENTS  =="
echo -e "================================"
echo -e "\033[0m${normal}"
source venv/bin/activate
pip2.7 install -r requirements.txt
bower install

echo -e "${BGreen}"
echo -e "================================"
echo -e "==  3/4    CONFIGURATION      =="
echo -e "================================"
echo -e "\033[0m${normal}"
cp configuration/example.py configuration/local.py
echo -n "Enter your GMAIL_USERNAME [Enter]: "
read GMAIL_USERNAME
echo `export GMAIL_USERNAME=$GMAIL_USERNAME`
echo -n "Enter your GMAIL_PASSWORD [Enter]: "
read GMAIL_PASSWORD
echo `export GMAIL_PASSWORD=$GMAIL_PASSWORD`


echo -e "${BGreen}"
echo -e "================================"
echo -e "==  4/4   INITIALIZATION DB   =="
echo -e "================================"
echo -e "\033[0m${normal}"
python2.7 manage.py db init
python2.7 manage.py db migrate
python2.7 manage.py db upgrade
python2.7 manage.py create_role --name 'admin'
python2.7 manage.py create_user --email=gmail@gmail.com --password=password
python2.7 manage.py add_role --user gmail@gmail.com --role admin
