# -*- coding: utf-8 -*-
import os
from datetime import timedelta
from os.path import abspath as os_path_abspath
from os.path import dirname as os_path_dirname
from os.path import join as os_path_join

current_dir = os_path_abspath(os_path_dirname(__file__))


# BASIC
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os_path_join(current_dir, '../', 'data.sqlite')
USE_TOKEN_AUTH = True

# EMAIL
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.getenv('GMAIL_USERNAME')
MAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')

# SECURITY
SECRET_KEY = os.getenv('SECRET_KEY') or 'secret_secret_secret'
SECURITY_REGISTERABLE = True
SECURITY_REGISTER_URL = '/auth/register'
SECURITY_PASSWORD_HASH = os.getenv('SECURITY_PASSWORD_HASH') or 'sha512_crypt'
SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT') or 'salt_salt_salt'
JWT_EXPIRATION_DELTA = timedelta(days=10)

# REST-API
REST_API_PREFIX = '/api/v1'
JWT_AUTH_HEADER_PREFIX = 'bearer'


SQLALCHEMY_TRACK_MODIFICATIONS = False
