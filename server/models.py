# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask.ext.security import UserMixin, RoleMixin
from flask.ext.sqlalchemy import SQLAlchemy
from savalidation import ValidationMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .errors_handlers import CheckError

db = SQLAlchemy()


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin, ValidationMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def check_mail_for_uniqueness(self, new_email):
        if self.query.filter_by(email=new_email).first() is None:
            result = True
        else:
            result = False
        return result

    def check_unique_username(self, new_username):
        if self.query.filter_by(username=new_username).first() is None:
            result = True
        else:
            result = False
        return result

    def import_data(self, data):
        try:
            self.email = data['email']
        except KeyError as key_err:
            raise CheckError('Invalid user: missing ' + key_err.args[0])
        try:
            self.username = data['username']
        except KeyError as key_err:
            raise CheckError('Invalid username: missing ' + key_err.args[0])
        try:
            self.password = data['password']
        except KeyError as key_err:
            raise CheckError('Invalid password: missing ' + key_err.args[0])
        return self
