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

##########
# Import #
##########

from datetime import *
from datetime import time as timeDT
import time
from dateutil.parser import parser
from enum import Enum
import ast


# <editor-fold desc="Enums">

#########
# Enums #
#########

class Gender(Enum):
    FEMALE = 1
    MALE = 2
    
    @classmethod
    def fromString(cls, string):
        conversion = {
            "Gender.FEMALE": Gender.FEMALE,
            "Gender.MALE": Gender.MALE
        }
        return (conversion[string])
    
    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return (result)
        for entry in string.strip()[1:-1].split(','):
            result.append(Gender.fromString(entry.strip()))
        return (result)
    
    def __str__(self):
        return ("Gender." + self.name.__str__())
    
    def __repr__(self):
        return (self.__str__())


class Occupation(Enum):
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
        return (conversion[string])
    
    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return (result)
        for entry in string.strip()[1:-1].split(','):
            result.append(Occupation.fromString(entry.strip()))
        return (result)
    
    def __str__(self):
        return ("Occupation." + self.name.__str__())
    
    def __repr__(self):
        return (self.__str__())


class FoodRestriction(Enum):
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
        return (conversion[string])
    
    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return (result)
        for entry in string.strip()[1:-1].split(','):
            result.append(FoodRestriction.fromString(entry.strip()))
        return (result)
    
    def __str__(self):
        return ("FoodRestriction." + self.name.__str__())
    
    def __repr__(self):
        return (self.__str__())


class TransportType(Enum):
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
        return (conversion[string])
    
    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return (result)
        for entry in string.strip()[1:-1].split(','):
            result.append(TransportType.fromString(entry.strip()))
        return (result)
    
    def __str__(self):
        return ("TransportType." + self.name.__str__())
    
    def __repr__(self):
        return (self.__str__())


class Equipment(Enum):
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
        return (conversion[string])
    
    @classmethod
    def parseListString(cls, string):
        result = []
        if string == "[]":
            return (result)
        for entry in string.strip()[1:-1].split(','):
            result.append(Equipment.fromString(entry.strip()))
        return (result)
    
    def __str__(self):
        return ("Equipment." + self.name.__str__())
    
    def __repr__(self):
        return (self.__str__())


# </editor-fold>

##########
# Circle #
##########

class MathCircle:
    """
    This class represents a math circle (i.e. a group of students participating in the morning math circles together
    """
    
    def __init__(self, name, grade, members = None, room = None, topics = None):
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
        return ("MathCircle({0},{1},{2},{3},{4})".format(self.name, self.grade, self.members, self.room, self.topics))
    
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


############
# Activity #
############

class Activity:
    """
    This class represents an activity such as afternoon activities or bigger projects that need to be organized or
    planned.
    """
    
    def __init__(self, name, timeAndPlace = None, participants = None, organizers = None, expenses = None):
        """
        the main constructor of an activity
        :param name: the name of the activity as a string
        :param timeAndPlace: time and place of the activity as the id of a spaceTimeSlot
        :param participants: a list of IDs of people refering to participants
        :param organizers: a list of IDs of people refering to organizers, usually counselors
        :param expenses: a list of associated expenses
        """
        if (participants == None):
            participants = []
        if (organizers == None):
            organizers = []
        if (expenses == None):
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


############
# Schedule #
############

class Schedule:
    """
    This class represents an instance of a schedule, i.e. a plan who is doing what at which time at which place. For
    this purpose it primarily consists of a list of activities.
    """
    
    def __init__(self, listOfMathCircles = None):
        """
        The main constructor of a (math circle) schedule
        :param listOfMathCircles: a list of tuples of IDs of (math circle, spacetime slot, teacher)
        """
        if listOfMathCircles == None:
            listOfMathCircles = []
        self.entries = listOfMathCircles
    
    def __str__(self):
        return ("Schedule({})".format(self.entries))
    
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
        return (Schedule([(dict["mathCircleID"], dict["spaceTimeSlotID"], dict["teacherID"]) for dict in dictionary]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Schedule(
            [(int(dict["mathCircleID"]), int(dict["spaceTimeSlotID"]), int(dict["teacherID"])) for dict in dictionary]))


############
# Expenses #
############

class Expense:
    """
    This class represents an expense for something.
    """
    
    def __init__(self, name, amount = 0, usage = None, payedAlready = False):
        if usage == None:
            usage = []
        self.amount = amount
        self.name = name
        self.usage = usage
        self.payedAlready = payedAlready
    
    def __str__(self):
        return ("Expense({0},{1},{2},{3})".format(self.name, self.amount, self.usage, self.payedAlready))
    
    def toDict(self):
        return ({"name": self.name, "amount": self.amount, "usage": self.usage, "payedAlready": self.payedAlready})
    
    @classmethod
    def fromDict(cls, dictionary):
        return (Expense(dictionary["name"], dictionary["amount"], dictionary["usage"], dictionary["payedAlready"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Expense(dictionary["name"],
                        int(dictionary["amount"]),
                        ast.literal_eval(dictionary["usage"]),
                        ast.literal_eval(dictionary["payedAlready"])))


####################
# Space-Time Slots #
####################


class SpaceTimeSlot:
    """
    This class represents a time slot with a beginning and an end as well as a place. Either can be empty. A time
    slot is represented by a 2-tuple of datetimes and a room is represented by the id of the room in the camp.
    """
    
    def __init__(self, beginning = datetime.min, end = datetime.max, room = None):
        self.beginning = beginning
        self.end = end
        self.timeSlot = [self.beginning, self.end]
        self.room = room
    
    def __str__(self):
        return ("SpaceTimeSlot([{0},{1}],{2})".format(self.beginning, self.end, self.room))
    
    def toDict(self):
        """
        saves the space-time slot to a dictionary in order to be saved to a csv file
        :return: a dictionary with beginning and end datetimes as well as the id of the room
        """
        return ({"beginning": self.beginning, "end": self.end, "room": self.room})
    
    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a space-time slot from a dictionary with keys beginning, end and room, inverse of toDict
        :param dictionary: the dictionary containing data to create the space-time slot from
        :return: the instance of the room
        """
        return (SpaceTimeSlot(dictionary["beginning"], dictionary["end"], dictionary["room"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (SpaceTimeSlot(datetime.strptime(dictionary["beginning"], "%Y-%m-%d %H:%M:%S"),
                              datetime.strptime(dictionary["end"], "%Y-%m-%d %H:%M:%S"),
                              int(dictionary["room"])))


# <editor-fold desc="Room types">

#########
# Rooms #
#########


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
        return ("Room({0})".format(self.name))
    
    def toDict(self):
        """
        serializes the room to a dictionary for saving its data in a csv file
        :return: a dictionary with key name and its value
        """
        return ({"name": self.name})
    
    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a room from a dictionary with a key "name", inverse of toDict
        :param dictionary: the dictionary containing data to create the room from
        :return: the instance of the room
        """
        return Room(dictionary["name"])


class GeneralRoom(Room):
    """
    This class represents a general room for everybodys usage
    """
    
    def __init__(self, name, equipment = None):
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
        return ("GeneralRoom({0},{1})".format(self.name, self.equipment))
    
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


class PrivateRoom(Room):
    """
    This class represents a private room for sleeping
    """
    
    def __init__(self, name = "", capacity = 0, inhabitants = None, bedtime = None, reservedForCounselors = False):
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

# </editor-fold>
