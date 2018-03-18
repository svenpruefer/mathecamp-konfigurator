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

from mathecamp_konfigurator import db
from mathecamp_konfigurator.model.association import curriculum, teachingMaterials

##############
# MathCircle #
##############

class MathCircle(db.Model):
    """
    This class represents a math circle (i.e. a group of students participating in morning math circles together
    """
    
    __tablename__ = 'mathcircles'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    grade = db.Column(db.Integer)
    
    room_id = db.Column(db.Integer, db.ForeignKey('generalrooms.id'), nullable = True)
    room = db.relationship("GeneralRoom", back_populates = True)
    
    topics = db.relationship("Topic", secondary = curriculum, back_populates = True)
    
    members = db.relationship("Participant", back_populates = True)
    
    def __str__(self):
        return ("MathCircle({0},{1},{2},{3},{4})".format(self.name, self.grade, self.members, self.room_id,
                                                         self.topics))
    
    def toDict(self):
        return ({"name": self.name, "grade": self.grade, "room_id": self.room}) # TODO read members and topics from db
    
    @classmethod
    def fromDict(cls, dictionary):
        return (MathCircle(dictionary["name"], dictionary["grade"], dictionary["room_id"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (MathCircle(name = dictionary["name"],
                           grade = int(dictionary["grade"]),
                           room_id = int(dictionary["room_id"])))


################
# Circle Slots #
################


class CircleSlot(db.Model):
    """
    This class represents a time slot for a math circle.
    """
    
    __tablename__ = 'circleslots'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    start = db.Column(db.DateTime)
    
    end = db.Column(db.DateTime)
    
    def __repr__(self):
        return ("CircleSlot({0},{1})".format(self.start, self.end))
    
    def toDict(self):
        """
        saves the circle time slot to a dictionary in order to be saved to a csv file
        
        :return: a dictionary with start and end time
        """
        return ({"start": self.start, "end": self.end})
    
    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a circle slot from a dictionary with the start and end time
        
        :param dictionary: the dictionary containing data of circle slot
        :return: the instance of the circle slot
        """
        return (CircleSlot(start = dictionary["start"], end = dictionary["end"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (CircleSlot(start = datetime.strptime(dictionary["start"], "%Y-%m-%d %H:%M:%S"),
                           end = datetime.strptime(dictionary["end"], "%Y-%m-%d %H:%M:%S")))


#########
# Topic #
#########


class Topic(db.Model):
    """
    This class represents a (math) topic
    """
    
    __tablename__ = 'topics'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    equipment = db.relationship("Equipment", secondary = teachingMaterials)
    
    def __repr__(self):
        return ("Topic({0})".format(self.name)) # TODO get equipment by querying the DB
    
    def toDict(self):
        """
        saves the teopic to a dictionary in order to be saved to a csv file

        :return: a dictionary with the name of the topic
        """
        return ({"name": self.name})
    
    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a topic from a dictionary with its name

        :param dictionary: the dictionary containing data of circle slot
        :return: the instance of the circle slot
        """
        return (Topic(name = dictionary["name"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Topic(start = dictionary["name"]))
