# -*- coding: utf-8 -*-
from __future__ import absolute_import


class CheckError(ValueError):
    pass


from flask.ext.mail import Mail
mail = Mail()


from flask.ext.cors import CORS
cors = CORS()


from flask.ext.security import Security, SQLAlchemyUserDatastore
from .models import User, Role, db
datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=datastore)


from flask_jwt import JWT
from flask import abort
jwt = JWT()


@jwt.authentication_handler
def authenticate(username, password):
    user = datastore.find_user(email=username)
    if user is not None:
        if not user.is_active():
            abort(401)
        if username == user.email and user.check_password(password):
            return user
    return None


@jwt.user_handler
def load_user(payload):
    user = datastore.find_user(id=payload['user_id'])
    return user
