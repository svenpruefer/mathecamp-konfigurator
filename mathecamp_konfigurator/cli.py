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

"""Console script for mathecamp_konfigurator."""

__docformat__ = 'reStructuredText'

###########
# Imports #
###########

import click


@click.command()
def main(args=None):
    """Console script for mathecamp_konfigurator."""
    click.echo("Replace this message by putting your code into "
               "mathecamp_konfigurator.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
