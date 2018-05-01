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

"""This file defines the mathCircle class"""

__docformat__ = 'reStructuredText'

###########
# Imports #
###########

import ast


class MathCircle:
    """
    This class represents a math circle (i.e. a group of students participating in the morning math circles together
    """

    def __init__(self, name, grade, members=None, room=None, topics=None):
        """
        This is the main constructor of a math circle
        :param name: the name of the circle
        :param grade: the grade of the math circle as an integer
        :param members: the members of the math circle as an integer of IDs (i.e. integers) of the participants
        :param room: the room where the math circle takes place as an ID of the room
        :param topics: a list of strings corresponding to the covered topics
        """
        if topics is None:
            topics = []
        if members is None:
            members = []
        self.name = name
        self.grade = grade
        self.members = members
        self.room = room
        self.topics = topics

    def __str__(self):
        return "MathCircle({0},{1},{2},{3},{4})".format(self.name, self.grade, self.members, self.room, self.topics)

    def toDict(self):
        return ({"name": self.name, "grade": self.grade, "members": self.members, "room": self.room,
                 "topics": self.topics})

    @classmethod
    def fromDict(cls, dictionary):
        return (MathCircle(dictionary["name"], dictionary["grade"], dictionary["members"], dictionary["room"],
                           dictionary["topics"]))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (MathCircle(dictionary["name"],
                           int(dictionary["grade"]),
                           ast.literal_eval(dictionary["members"]),
                           int(dictionary["room"]),
                           ast.literal_eval(dictionary["topics"])))
