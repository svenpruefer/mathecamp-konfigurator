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

"""This file defines enums used in mathecamp-konfigurator"""

__docformat__ = 'reStructuredText'


##########
# Import #
##########

from enum import Enum

##########
# Gender #
##########


class Gender(Enum):
    FEMALE = 1
    MALE = 2

    @classmethod
    def fromString(cls, string):
        conversion = {
            "Gender.FEMALE": Gender.FEMALE,
            "Gender.MALE": Gender.MALE
        }
        return conversion[string]

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
            "Occupation.Guest": Occupation.GUEST
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


class FoodRestriction(Enum):
    """
    Enum for food restrictions of people
    """

    VEGETARIAN = 1
    VEGAN = 2
    NO_MEAT = 3
    NO_FISH = 4
    CELIAC_DISEASE = 5
    NO_NUTS = 6
    NO_EGGS = 7
    NO_CARROTS = 8

    @classmethod
    def fromString(cls, string):
        conversion = {
            "FoodRestriction.VEGETARIAN": FoodRestriction.VEGETARIAN,
            "FoodRestriction.VEGAN": FoodRestriction.VEGAN,
            "FoodRestriction.NO_MEAT": FoodRestriction.NO_MEAT,
            "FoodRestriction.NO_FISH": FoodRestriction.NO_FISH,
            "FoodRestriction.CELIAC_DISEASE": FoodRestriction.CELIAC_DISEASE,
            "FoodRestriction.NO_NUTS": FoodRestriction.NO_NUTS,
            "FoodRestriction.NO_EGGS": FoodRestriction.NO_EGGS,
            "FoodRestriction.NO_CARROTS": FoodRestriction.NO_CARROTS
        }
        return conversion[string]

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


class TransportType(Enum):
    """
    Enum for various possibilities of how people can arrive at or leave from the Mathecamp
    """

    BUS = 1
    PRIVATE = 2
    SELF = 3

    @classmethod
    def fromString(cls, string):
        conversion = {
            "TransportType.BUS": TransportType.BUS,
            "TransportType.PRIVATE": TransportType.PRIVATE,
            "TransportType.SELF": TransportType.SELF
        }
        return conversion[string]

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


class Equipment(Enum):
    """
    Enum for possible equipment that can be in a room
    """

    PIANO = 1
    BLACKBOARD = 2
    WHITEBOARD = 3
    CANVAS = 4

    @classmethod
    def fromString(cls, string):
        conversion = {
            "Equipment.PIANO": Equipment.PIANO,
            "Equipment.BLACKBOARD": Equipment.BLACKBOARD,
            "Equipment.WHITEBOARD": Equipment.WHITEBOARD,
            "Equipment.CANVAS": Equipment.CANVAS
        }
        return conversion[string]

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
