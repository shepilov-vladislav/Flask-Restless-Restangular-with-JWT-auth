# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime

from flask import (
    render_template,
    flash,
    url_for,
    request,
    Blueprint,
    jsonify,
    current_app as app
)
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

from .errors_handlers import CheckError
from .extensions import datastore
from .models import db, User

users_bp = Blueprint('users', __name__)


@users_bp.errorhandler(CheckError)
def hook_validation_error(e):
    response = jsonify(
        {
            'status': 400,
            'error': 'BAD REQUEST',
            'message': str(e)
        })
    response.status_code = 400
    return response


@users_bp.route('/email', methods=['POST'])
def check_email():
    data = request.get_json(force=True)
    if not User().check_mail_for_uniqueness(data['email']):
        return hook_validation_error('Email already exists. Please register with a new email.')
    else:
        return jsonify({'valid': 'true'})


@users_bp.route('/username', methods=['POST'])
def check_username():
    data = request.get_json(force=True)
    if not User().check_unique_username(data['username']):
        return hook_validation_error('Username already exists. Please register with a new username.')
    else:
        return jsonify({'valid': 'true'})


@users_bp.route('/', methods=['POST'])
def registration_user():
    data = request.get_json(force=True)
    if not User().check_mail_for_uniqueness(data['email']):
        return hook_validation_error('Email already exists. Please register with a new email.')
    elif not User().check_unique_username(data['username']):
        return hook_validation_error('Username already exists, please try another username')
    else:
        user = datastore.create_user(email=data['email'], password=data['password'])
        user.set_password(data['password'])
        user.active = False
        user.username = data['username']
        db.session.commit()

    email_token = generate_confirmation_token(user.email)
    confirm_url = url_for('.confirm_email', token=email_token, _external=True)

    mail = Mail()
    msg = Message("Please confirm your account", sender="example_rest_blog@gmail.com", recipients=[user.email])
    msg.body = render_template(
        "email/confirmation_email.txt",
        confirmation_url=confirm_url,
        user=user
    )
    msg.html = render_template(
        "email/confirmation_email.html",
        confirmation_url=confirm_url,
        user=user
    )
    mail.send(msg)

    return jsonify({
        'id': user.id,
        'message': 'User successfully created, please check your email to activate your account'
    })


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


@users_bp.route('/confirm/<token>')
def confirm_email(token):
    email = confirm_token(token)
    user = User.query.filter_by(email=email).first_or_404()
    if user.email == email:
        user.active = True
        user.confirmed_at = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    else:
        flash('The confirmation link is invalid or has expired.', 'danger')
    return render_template("email/confirm.html")


def confirm_token(token, expiration=4800):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except Exception:
        return hook_validation_error("Token is not verified!")
    return email
