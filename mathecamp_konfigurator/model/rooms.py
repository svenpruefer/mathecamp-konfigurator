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

"""This file defines classes for rooms"""

__docformat__ = 'reStructuredText'

##########
# Import #
##########

from datetime import *
from datetime import time as timeDT
import time
import ast
from mathecamp_konfigurator.model.enums import *


########
# Room #
########

class Room:
    """
    This class represents a general room at Violau
    """

    def __init__(self, name):
        """
        The main constructor of a room
        :param name: The name of the room as a string
        """
        self.name = name

    def __str__(self):
        return "Room({0})".format(self.name)

    def toDict(self):
        """
        serializes the room to a dictionary for saving its data in a csv file
        :return: a dictionary with key name and its value
        """
        return {"name": self.name}

    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a room from a dictionary with a key "name", inverse of toDict
        :param dictionary: the dictionary containing data to create the room from
        :return: the instance of the room
        """
        return Room(dictionary["name"])


################
# General Room #
################


class GeneralRoom(Room):
    """
    This class represents a general room for everybodys usage
    """

    def __init__(self, name, equipment=None):
        """
        The main constructor of a general room
        :param name: the name of the room as a string
        :param equipment: the equipment available in this room as a list of enums of type Equipment
        """
        Room.__init__(self, name)

        if equipment is None:
            equipment = []

        self.equipment = equipment

    def __str__(self):
        """
        prints general room in constructor style
        :return: string representation of general room
        """
        return "GeneralRoom({0},{1})".format(self.name, self.equipment)

    def toDict(self):
        """
        serializes the general room to a dictionary for saving its data in a csv file
        :return: a dictionary with keys name and equipment
        """
        return {"name": self.name, "equipment": self.equipment}

    @classmethod
    def fromDict(cls, dictionary):
        return GeneralRoom(dictionary["name"], dictionary["equipment"])

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return GeneralRoom(dictionary["name"], Equipment.parseListString(dictionary["equipment"]))


################
# Private Room #
################


class PrivateRoom(Room):
    """
    This class represents a private room for sleeping
    """

    def __init__(self, name="", capacity=0, inhabitants=None, bedtime=None, reservedForCounselors=False):
        """
        The main constructor of a private room
        :param name: the name of the room as a string
        :param capacity: an integer describing how many people can sleep in this room
        :param inhabitants: a list of ids of humans that stay in this room
        :param bedtime: the bedtime of this room as a time value
        :param reservedForCounselors: a Boolean describing whether this is a counselor room
        """
        Room.__init__(self, name)

        if inhabitants is None:
            inhabitants = []

        self.capacity = capacity
        self.inhabitants = inhabitants
        self.bedtime = bedtime
        self.reservedForCounselors = reservedForCounselors

    def __str__(self):
        """
        prints private room in constructor style
        :return: string representation of private room
        """
        return ("PrivateRoom({0},{1},{2},{3},{4})".format(self.name, self.capacity, self.inhabitants,
                                                          self.bedtime, self.reservedForCounselors))

    def toDict(self):
        """
        serializes the private room to a dictionary for saving its data in a csv file
        :return: a dictionary with keys name, capacity, inhabitants, bedtime and reservedForCounselors
        """
        return {"name": self.name,
                "capacity": self.capacity,
                "inhabitants": self.inhabitants,
                "bedtime": self.bedtime,
                "reservedForCounselors": self.reservedForCounselors
                }

    @classmethod
    def fromDict(cls, dictionary):
        return PrivateRoom(dictionary["name"], dictionary["capacity"], dictionary["inhabitants"], dictionary["bedtime"],
                           dictionary["reservedForCounselors"])

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        if dictionary["bedtime"] == "":
            bedtime = None
        else:
            bedtime = timeDT(time.strptime(dictionary["bedtime"], "%H:%M:%S").tm_hour, time.strptime(
                dictionary["bedtime"], "%H:%M:%S").tm_min, time.strptime(
                dictionary["bedtime"], "%H:%M:%S").tm_sec)
        return PrivateRoom(dictionary["name"],
                           int(dictionary["capacity"]),
                           ast.literal_eval(dictionary["inhabitants"]),
                           bedtime,
                           ast.literal_eval(dictionary["reservedForCounselors"]))
