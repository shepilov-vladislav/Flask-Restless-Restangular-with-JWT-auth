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
from flask import abort, jsonify, current_app
from datetime import datetime
jwt = JWT()


@jwt.authentication_handler
def custom_authentication_handler(username, password):
    user = datastore.find_user(email=username)
    if user is not None:
        if not user.is_active():
            abort(401)
        if username == user.email and user.check_password(password):
            return user
    return None


@jwt.identity_handler
def custom_identity_handler(payload):
    user = datastore.find_user(id=payload['user_id'])
    return user


@jwt.auth_response_handler
def custom_auth_response_callback(access_token, identity):
    del identity
    return jsonify({'token': access_token.decode('utf-8')})


@jwt.jwt_payload_handler
def custom_jwt_payload_handler(identity):
    iat = datetime.utcnow()
    exp = iat + current_app.config.get('JWT_EXPIRATION_DELTA')
    nbf = iat + current_app.config.get('JWT_NOT_BEFORE_DELTA')
    identity = getattr(identity, 'id') or identity['id']
    return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': identity, 'user_id': identity}
