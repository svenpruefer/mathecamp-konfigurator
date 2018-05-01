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

"""This file defines enums in mathecamp-konfigurator by mirroring their SQL counterparts instead of using the enum
 package. This has the advantage of allowing to add new 'enums' dynamically."""

__docformat__ = 'reStructuredText'

###########
# Imports #
###########

from mathecamp_konfigurator import db
from mathecamp_konfigurator.model.types import EnumMixin

##########
# Gender #
##########


class Gender(EnumMixin, db.Model):
    """
    Possible genders in mathecamp_konfigurator
    """

    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String, unique=True)

    def __str__(self):
        return "Gender." + self.name.__str__()

    def __repr__(self):
        return self.__str__()


###################
# Transport Types #
###################


class TransportType(EnumMixin, db.Model):
    """
    Class for types of transport of people in a mathecamp. By default this includes BUS, PRIVATE and SELF.
    """

    __tablename__ = 'transporttypes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String, unique=True)

    def __str__(self):
        return "TransportType." + self.name.__str__()

    def __repr__(self):
        return self.__str__()


#############
# Penalties #
#############


class Penalty(EnumMixin, db.Model):
    """
    Class for penalties that can be given to participants at a mathecamp. By default this includes GARBAGE_SEPARATION
    and TABLE_WIPING
    """

    __tablename__ = 'penalties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String, unique=True)

    def __str__(self):
        return "Penalty." + self.name.__str__()

    def __repr__(self):
        return self.__str__()


####################
# FoodRestrictions #
####################


class FoodRestriction(EnumMixin, db.Model):
    """
    Possible food restrictions in a mathecamp. By default includes VEGETARIAN, VEGAN, NO_MEAT, NO_FISH, CELIAC_DISEASE,
    NO_NUTS, NO_EGGS, NO_CARROTS
    """

    __tablename__ = 'foodrestrictions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String)

    def __str__(self):
        return "FoodRestriction.{0}".format(self.name)

    def __repr__(self):
        return self.__str__()


#############
# Equipment #
#############


class Equipment(EnumMixin, db.Model):
    """
    Class for equipment that can be present in a room at a mathecamp. By default this includes PIANO, BLACKBOARD,
    WHITEBOARD and CANVAS
    """

    __tablename__ = 'equipment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String)

    def __str__(self):
        return "Equipment.{0}".format(self.name)

    def __repr__(self):
        return self.__str__()
