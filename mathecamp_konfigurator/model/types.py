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

"""This file defines most types which are not people used in mathecamp-konfigurator."""

__docformat__ = 'reStructuredText'

##########
# Import #
##########

from datetime import *


############
# Schedule #
############


class Schedule:
    """
    This class represents an instance of a schedule, i.e. a plan who is doing what at which time at which place. For
    this purpose it primarily consists of a list of activities.
    """

    def __init__(self, listOfMathCircles=None):
        """
        The main constructor of a (math circle) schedule
        :param listOfMathCircles: a list of tuples of IDs of (math circle, spacetime slot, teacher)
        """
        if listOfMathCircles is None:
            listOfMathCircles = []
        self.entries = listOfMathCircles

    def __str__(self):
        return "Schedule({})".format(self.entries)

    def toDict(self):
        """
        maps the schedule to a list of dictionaries for saving it in a csv file
        :return: a list where each entry is a dictionary containing a math circle ID, a spaceTime slot ID and
         a counselor ID
        """
        return ([{"mathCircleID": entry[0], "spaceTimeSlotID": entry[1], "teacherID": entry[2]}
                 for entry in self.entries])

    @classmethod
    def fromDict(cls, dictionary):
        return Schedule([(innerDict["mathCircleID"], innerDict["spaceTimeSlotID"],
                          innerDict["teacherID"]) for innerDict in dictionary])

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Schedule(
            [(int(innerDict["mathCircleID"]), int(innerDict["spaceTimeSlotID"]),
              int(innerDict["teacherID"])) for innerDict in dictionary]))


####################
# Space-Time Slots #
####################


class SpaceTimeSlot:
    """
    This class represents a time slot with a beginning and an end as well as a place. Either can be empty. A time
    slot is represented by a 2-tuple of datetimes and a room is represented by the id of the room in the camp.
    """

    def __init__(self, beginning=datetime.min, end=datetime.max, room=None):
        self.beginning = beginning
        self.end = end
        self.timeSlot = [self.beginning, self.end]
        self.room = room

    def __str__(self):
        return "SpaceTimeSlot([{0},{1}],{2})".format(self.beginning, self.end, self.room)

    def toDict(self):
        """
        saves the space-time slot to a dictionary in order to be saved to a csv file
        :return: a dictionary with beginning and end datetimes as well as the id of the room
        """
        return {"beginning": self.beginning, "end": self.end, "room": self.room}

    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a space-time slot from a dictionary with keys beginning, end and room, inverse of toDict
        :param dictionary: the dictionary containing data to create the space-time slot from
        :return: the instance of the room
        """
        return SpaceTimeSlot(dictionary["beginning"], dictionary["end"], dictionary["room"])

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (SpaceTimeSlot(datetime.strptime(dictionary["beginning"], "%Y-%m-%d %H:%M:%S"),
                              datetime.strptime(dictionary["end"], "%Y-%m-%d %H:%M:%S"),
                              int(dictionary["room"])))

#############
# Penalties #
#############

class Penalty:
    """
    This class represents a penalty.
    """

    def __init__(self, name=""):
        """
        Basic constructor of a penalty
        :param name: name of the penalty
        """
        self.name = name

    def __str__(self):
        return "Penalty(" + self.name + ")"

    def toDict(self):
        return {"name": self.name}

    @classmethod
    def fromDict(cls, dictionary):
        return Penalty(dictionary["name"])

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return Penalty(dictionary["name"])
