# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask.ext.restless import APIManager
from flask.ext.restless import ProcessingException
from flask_jwt import jwt_required, current_user

from config import REST_API_PREFIX
from .models import User


def is_authorized(user, instance):
    if int(user.id) == int(instance):
        result = True
    else:
        result = False
    return result


@jwt_required()
def auth_user_func(instance_id=None, **kwargs):
    if not is_authorized(current_user, instance_id):
        raise ProcessingException(description='Not Authorized', code=401)


@jwt_required()
def auth_admin_func(instance_id=None, **kwargs):
    raise ProcessingException(description='Only admins can access this view', code=401)


@jwt_required()
def auth_func(instance_id=None, **kwargs):
    pass

api_manager = APIManager()

api_manager.create_api(
    User,
    methods=['GET', 'PUT'],
    url_prefix=REST_API_PREFIX,
    preprocessors=dict(GET_SINGLE=[auth_user_func], GET_MANY=[auth_admin_func]),
    collection_name='user',
    include_columns=['id', 'username'])
