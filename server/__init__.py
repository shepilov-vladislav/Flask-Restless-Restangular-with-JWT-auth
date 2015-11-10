# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from flask import Flask, render_template, jsonify

from .api_service import api_manager
from .extensions import (
    mail,
    cors,
    db,
    security,
    jwt
)


def create_app():
    configuration_object = os.environ.get('FLASK_CONFIGURATION') or 'configuration.local'
    app = Flask(__name__)
    app.config.from_object(configuration_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_main_routes(app)
    return app


def register_extensions(app):
    mail.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
        api_manager.init_app(app, flask_sqlalchemy_db=db)
    security.init_app(app)
    jwt.init_app(app)
    return None


def register_blueprints(app):
    from .views import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')
    return None


def register_errorhandlers(app):
    def render_error(error):
        return jsonify({
            "error": "Unauthorized",
            "description": "Please check your email to activate your account.",
            "status_code": 401
        }), 401

    for errcode in [401]:
        app.errorhandler(errcode)(render_error)
    return None


def register_main_routes(app):
    def index():
        return render_template("index.html")
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/index', 'index', index)
    return None
