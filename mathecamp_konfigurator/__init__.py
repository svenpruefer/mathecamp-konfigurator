#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Sven Prüfer
#
# This file is part of mathecamp-configurator.
#
# mathecamp-configurator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# mathecamp-configurator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mathecamp-configurator.  If not, see <http://www.gnu.org/licenses/>.

"""Top-level package for mathecamp-konfigurator."""

__author__ = """Sven Pruefer"""
__email__ = 'pruefer.sven@gmail.com'
__version__ = '0.1.0'

from flask import Flask
from .views.overview import overview

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')
app.register_blueprint(overview, url_prefix='/overview/')

@app.route('/')
def entryPoint():
    return 'This is the entry point of mathecamp-konfigurator'
