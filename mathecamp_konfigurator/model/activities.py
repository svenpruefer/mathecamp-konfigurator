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

"""This file defines activities"""

__docformat__ = 'reStructuredText'

###########
# Imports #
###########

import ast


class Activity:
    """
    This class represents an activity such as afternoon activities or bigger projects that need to be organized or
    planned.
    """

    def __init__(self, name, timeAndPlace=None, participants=None, organizers=None, expenses=None):
        """
        the main constructor of an activity
        :param name: the name of the activity as a string
        :param timeAndPlace: time and place of the activity as the id of a spaceTimeSlot
        :param participants: a list of IDs of people refering to participants
        :param organizers: a list of IDs of people refering to organizers, usually counselors
        :param expenses: a list of associated expenses
        """
        if participants is None:
            participants = []
        if organizers is None:
            organizers = []
        if expenses is None:
            expenses = []
        self.name = name
        self.timeAndPlace = timeAndPlace
        self.participants = participants
        self.organizers = organizers
        self.expenses = expenses

    def __str__(self):
        return ("Activity({0},{1},{2},{3},{4})".format(self.name, self.timeAndPlace,
                                                       self.participants, self.organizers, self.expenses))

    def toDict(self):
        return ({"name": self.name, "timeAndPlace": self.timeAndPlace, "participants": self.participants,
                 "organizers": self.organizers, "expenses": self.expenses})

    @classmethod
    def fromDict(cls, dictionary):
        return (Activity(dictionary["name"], dictionary["timeAndPlace"], dictionary["participants"],
                         dictionary["organizers"], dictionary["expenses"]))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Activity(dictionary["name"],
                         int(dictionary["timeAndPlace"]),
                         ast.literal_eval(dictionary["participants"]),
                         ast.literal_eval(dictionary["organizers"]),
                         ast.literal_eval(dictionary["expenses"])))
