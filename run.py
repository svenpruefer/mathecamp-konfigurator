#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Sven Prüfer
#
# This file is part of mathecamp-konfigurator.
#
# mathecamp-konfigurator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# mathecamp-konfigurator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mathecamp-konfigurator.  If not, see <http://www.gnu.org/licenses/>.

"""This is the main entry point of mathecamp-konfigurator"""

__docformat__ = 'reStructuredText'

###########
# Imports #
###########

from mathecamp_konfigurator import app


if __name__ == '__main__':
    app.run()
