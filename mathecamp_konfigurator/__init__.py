# -*- coding: utf-8 -*-

"""Top-level package for mathecamp-konfigurator."""

from flask import Flask

__author__ = """Sven Pruefer"""
__email__ = 'pruefer.sven@gmail.com'
__version__ = '0.1.0'

app = Flask(__name__, instance_relative_config=True)

from mathecamp_konfigurator.views import views

app.config.from_object('config')
app.config.from_pyfile('config.py')
