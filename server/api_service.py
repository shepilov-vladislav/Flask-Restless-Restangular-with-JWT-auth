# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import logging

from flask.ext.restless import APIManager
from flask.ext.restless import ProcessingException
from flask_jwt import jwt_required, current_identity

logger = logging.getLogger(__name__)

configuration_object = os.environ.get('FLASK_CONFIGURATION') or 'configuration.local'
REST_API_PREFIX = None
try:
    exec('from {configuration_object} import REST_API_PREFIX'.format(configuration_object=configuration_object))
except Exception as e:
    logger.debug('Couldn\'t load REST_API_PREFIX from `%s`!\nDetails: %s', configuration_object, e)
REST_API_PREFIX = REST_API_PREFIX or '/api/v1'
from .models import User, Article


def is_authorized(user, instance):
    return int(user.id) == int(instance)


@jwt_required()
def auth_user_func(instance_id=None, **kwargs):
    del kwargs
    if not is_authorized(current_identity, instance_id):
        raise ProcessingException(description='Not Authorized', code=401)


@jwt_required()
def auth_admin_func(instance_id=None, **kwargs):
    del instance_id
    del kwargs
    raise ProcessingException(description='Only admins can access this view', code=401)


@jwt_required()
def auth_func(instance_id=None, **kwargs):
    del instance_id
    del kwargs


def auth_without_jwt(instance_id=None, **kwargs):
    del instance_id
    del kwargs

api_manager = APIManager()

api_manager.create_api(
    User,
    methods=['GET', 'PUT'],
    url_prefix=REST_API_PREFIX,
    preprocessors=dict(GET_SINGLE=[auth_user_func], GET_MANY=[auth_admin_func]),
    collection_name='user',
    include_columns=['id', 'username', 'roles'])

api_manager.create_api(
    Article,
    # results_per_page=5,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix=REST_API_PREFIX,
    preprocessors=dict(GET_SINGLE=[auth_without_jwt], GET_MANY=[auth_without_jwt]),
    collection_name='article',
    include_columns=['id', 'title', 'text', 'author', 'created_at'],
    include_methods=['author_username'])
