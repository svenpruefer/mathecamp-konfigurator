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


class Gender:
    """
    Possible genders in mathecamp_konfigurator.
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def fromString(cls, string):
        if string.startswith('Gender.'):
            return string.split('.')[1]
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


class FoodRestriction:
    """
    Possible food restrictions in a mathecamp. By default includes VEGETARIAN, VEGAN, NO_MEAT, NO_FISH, CELIAC_DISEASE,
    NO_NUTS, NO_EGGS, NO_CARROTS
    """

    def __init__(self, name):
        self.name =name

    @classmethod
    def fromString(cls, string):
        if string.startswith('FoodRestriction.'):
            return string.split('.')[1]
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


class TransportType:
    """
    Class for types of transport of people in a mathecamp. By default this includes BUS, PRIVATE and SELF.
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def fromString(cls, string):
        if string.startswith('TransportType.'):
            return string.split('.')[1]
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


class Equipment:
    """
    Class for equipment that can be present in a room at a mathecamp. By default this includes PIANO, BLACKBOARD,
    WHITEBOARD and CANVAS
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def fromString(cls, string):
        if string.startswith('Equipment.'):
            return string.split('.')[1]
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


class Penalty:
    """
    Class for penalties that can be given to participants at a mathecamp. By default this includes GARBAGE_SEPARATION
    and TABLE_WIPING
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def fromString(cls, string):
        if string.startswith('Penalty.'):
            return string.split('.')[1]
        else:
            raise ValueError("String to parse did not start with 'Penalty.'")

    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return result
        for entry in string.strip()[1:-1].split(','):
            result.append(Penalty.fromString(entry.strip()))
        return result

    def __str__(self):
        return "Penalty." + self.name.__str__()

    def __repr__(self):
        return self.__str__()
