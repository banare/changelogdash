#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

dashboard manager
~~~~~~~~~~~~~~~~~

This module contains the management functionality.

"""

import os
import redi

from flaskext.script import Manager

from dash import app, g, redis_connect
from dash.views.index import view_sync_url

manager = Manager(app)

app.test_request_context('/').push()
redi.config.init(r=redis_connect())


@manager.command
def clear_db():

    r = redis_connect()
    r.flushall()


@manager.command
def sync():
    view_sync_url()


if __name__ == '__main__':
    manager.run()