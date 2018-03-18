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

from flask import Blueprint, redirect, url_for
from flask import render_template
from mathecamp_konfigurator.export import IO
import os

camp = Blueprint('camp', __name__)

@camp.route('/load_project/', methods=['POST'])
def loadProject():
    mathecampIO = IO(os.path.realpath(__file__)[:-36] + "tests\\IO\\resources\\")
    mathecamp = mathecampIO.readMathecampFromFiles()
    return redirect(url_for('overview/general/'), beginningDate=mathecamp.dates['start'])
