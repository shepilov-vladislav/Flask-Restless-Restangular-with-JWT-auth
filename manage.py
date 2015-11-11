# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell, Server
from flask.ext.security.script import (
    CreateUserCommand,
    CreateRoleCommand,
    AddRoleCommand,
    RemoveRoleCommand,
    ActivateUserCommand,
    DeactivateUserCommand,
)
from server.models import db

from run import app

migrate = Migrate(app, db)
manager = Manager(app)


def make_context():
    return {'app': app}


manager.add_command('server', Server(host='0.0.0.0', port=8001, use_debugger=True, use_reloader=True))
manager.add_command('shell', Shell(make_context=make_context))

manager.add_command('db', MigrateCommand)

manager.add_command('create_user', CreateUserCommand())
manager.add_command('create_role', CreateRoleCommand())
manager.add_command('add_role', AddRoleCommand())
manager.add_command('remove_role', RemoveRoleCommand())
manager.add_command('deactivate_user', DeactivateUserCommand())
manager.add_command('activate_user', ActivateUserCommand())


if __name__ == '__main__':
    manager.run()
