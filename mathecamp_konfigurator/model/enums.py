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

"""This file defines enums in mathecamp-konfigurator by mirroring their SQL counterparts instead of using the enum
 package. This has the advantage of allowing to add new 'enums' dynamically."""

__docformat__ = 'reStructuredText'


##########
# Import #
##########

from enum import Enum
from mathecamp_konfigurator.model.types import EnumMixin

##########
# Gender #
##########


class Gender(EnumMixin):
    """
    Possible genders in mathecamp_konfigurator.
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def fromString(cls, string):
        if string.startswith('Gender.'):
            return Gender(name=string.split('.')[1])
        else:
            raise ValueError("String to parse did not start with 'Gender.'")

    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return result
        for entry in string.strip()[1:-1].split(','):
            result.append(Gender.fromString(entry.strip()))
        return result

    def __str__(self):
        return "Gender." + self.name.__str__()

    def __repr__(self):
        return self.__str__()


##############
# Occupation #
##############


class Occupation(Enum):
    """
    Enum for distinguish different types of people
    """

    COUNSELOR = 1
    PARTICIPANT = 2
    GUEST = 3

    @classmethod
    def fromString(cls, string):
        conversion = {
            "Occupation.COUNSELOR": Occupation.COUNSELOR,
            "Occupation.PARTICIPANT": Occupation.PARTICIPANT,
            "Occupation.GUEST": Occupation.GUEST
        }
        return conversion[string]

    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return result
        for entry in string.strip()[1:-1].split(','):
            result.append(Occupation.fromString(entry.strip()))
        return result

    def __str__(self):
        return "Occupation." + self.name.__str__()

    def __repr__(self):
        return self.__str__()

#####################
# Food Restricitons #
#####################


class FoodRestriction(EnumMixin):
    """
    Enum for food restrictions of people
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def fromString(cls, string):
        if string.startswith('FoodRestriction.'):
            return FoodRestriction(name=string.split('.')[1])
        else:
            raise ValueError("String to parse did not start with 'FoodRestriction.'")

    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return result
        for entry in string.strip()[1:-1].split(','):
            result.append(FoodRestriction.fromString(entry.strip()))
        return result

    def __str__(self):
        return "FoodRestriction." + self.name.__str__()

    def __repr__(self):
        return self.__str__()


###################
# Transport Types #
###################


class TransportType(EnumMixin):
    """
    Enum for various possibilities of how people can arrive at or leave from the Mathecamp
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def fromString(cls, string):
        if string.startswith('TransportType.'):
            return TransportType(name=string.split('.')[1])
        else:
            raise ValueError("String to parse did not start with 'TransportType.'")

    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return result
        for entry in string.strip()[1:-1].split(','):
            result.append(TransportType.fromString(entry.strip()))
        return result

    def __str__(self):
        return "TransportType." + self.name.__str__()

    def __repr__(self):
        return self.__str__()

#############
# Equipment #
#############


class Equipment(EnumMixin):
    """
    Enum for possible equipment that can be in a room
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def fromString(cls, string):
        if string.startswith('Equipment.'):
            return Equipment(name=string.split('.')[1])
        else:
            raise ValueError("String to parse did not start with 'Equipment.'")

    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return result
        for entry in string.strip()[1:-1].split(','):
            result.append(Equipment.fromString(entry.strip()))
        return result

    def __str__(self):
        return "Equipment." + self.name.__str__()

    def __repr__(self):
        return self.__str__()
