[![Software License][ico-license]](LICENSE.md)
[![Quality Score][ico-code-quality]][link-code-quality]
[![Code Health][ico-code-health]][link-code-health]

# Flask-Restless-Restangular-with-JWT-auth
example blog application based on Flask-Restless on backend and Restangular on frontend

# Quick Start

    - cd path/to/projects
    - git clone https://github.com/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth.git
    - cd Flask-Restless-Restangular-with-JWT-auth
    - virtualenv -p /usr/bin/python2.7 venv
    - source venv/bin/activate
    - pip2.7 install -r requirements.txt
    - bower install
    - cp configuration/example.py configuration/local.py
    - fill you params in configuration/local.py
    - python2.7 manage.py db init
    - python2.7 manage.py db migrate
    - python2.7 manage.py db upgrade
    - python2.7 manage.py create_role --name 'admin'
    - python2.7 manage.py create_user --email=gmail@gmail.com --password=password
    - python2.7 manage.py add_role --user gmail@gmail.com --role admin
    - python2.7 manage.py server
    - go to http://127.0.0.1:8001/
    - enjoy!

[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
[ico-code-quality]: https://img.shields.io/scrutinizer/g/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth.svg?style=flat-square
[ico-code-health]: https://landscape.io/github/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth/master/landscape.svg?style=flat-square

[link-code-quality]: https://scrutinizer-ci.com/g/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth
[link-code-health]: https://landscape.io/github/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth/master
