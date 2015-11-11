# Flask-Restless-Restangular-with-JWT-auth
example blog application based on Flask-Restless on backend and Restangular on frontend


[![Software License][ico-license]](LICENSE.md)
[![Quality Score][ico-code-quality]][link-code-quality]
[![Code Health][ico-code-health]][link-code-health]

# Quick Start

    - cd path/to/projects
    - git clone https://github.com/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth.git
    - cd Flask-Restless-Restangular-with-JWT-auth
    - virtualenv -p /usr/bin/python2.7 venv
    - source venv/bin/activate
    - pip2.7 install -r requirements.txt
    - bower install
    - python2.7 db.py db init
    - python2.7 db.py db migrate
    - python2.7 db.py db upgrade
    - python2.7 manage.py create_user --email=gmail@gmail.com --password=password
    - cp configuration/example.py configuration/local.py
    - python2.7 manage.py server
    - go to http://127.0.0.1:8001/
    - enjoy!

[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
[ico-code-quality]: https://scrutinizer-ci.com/g/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth/badges/quality-score.png?b=master
[ico-code-health]: https://landscape.io/github/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth/master/landscape.svg?style=flat

[link-code-quality]: https://scrutinizer-ci.com/g/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth
[link-code-health]: https://landscape.io/github/shepilov-vladislav/Flask-Restless-Restangular-with-JWT-auth/master
