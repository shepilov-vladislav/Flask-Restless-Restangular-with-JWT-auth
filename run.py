# -*- coding: utf-8 -*-
from __future__ import absolute_import

from server import create_app

app = create_app(configuration_object='configuration.local')
if __name__ == '__main__':
    app.run()
