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
from mathecamp_konfigurator.model.association import roomEquipment
import ast
from datetime import time as timeDT
import time

###############
# GeneralRoom #
###############

class GeneralRoom(db.Model):
    """
    This class represents a general room for everybodys usage
    """
    
    __tablename__ = 'generalrooms'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    equipment = db.relationship("Equipment", secondary = roomEquipment)
    
    def __str__(self):
        """
        prints a general room
        
        :return: string representation of general room
        """
        return ("GeneralRoom({0})".format(self.name))  # TODO get equipment from db query
    
    def toDict(self):
        """
        serializes the general room to a dictionary for saving its data in a csv file
        
        :return: a dictionary with its name
        """
        return {"name": self.name}
    
    @classmethod
    def fromDict(cls, dictionary):
        return GeneralRoom(dictionary["name"])
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return GeneralRoom(dictionary["name"])


###############
# PrivateRoom #
###############

class PrivateRoom(db.Model):
    """
    This class represents a private room for sleeping
    """
    
    __tablename__ = 'privaterooms'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    capacity = db.Column(db.Integer)
    
    bedtime = db.Column(db.Time)
    
    reservedForCounselor = db.Column(db.Boolean)
    
    inhabitantsGuests = db.relationship("Guest", back_populates = True)
    
    inhabitantsCounselors = db.relationship("Counselor", back_populates = True)
    
    inhabitantsParticipants = db.relationship("Participant", back_populates = True)
    
    def __repr__(self):
        """
        prints private room
        
        :return: string representation of private room
        """
        return ("PrivateRoom({0},{1},{2},{3})".format(self.name, self.capacity, self.bedtime,
                                                      self.reservedForCounselors))
    
    def toDict(self):
        """
        serializes the private room to a dictionary for saving its data in a csv file
        
        :return: a dictionary with keys name, capacity, bedtime and reservedForCounselors
        """
        return {"name": self.name,
                "capacity": self.capacity,
                "bedtime": self.bedtime,
                "reservedForCounselors": self.reservedForCounselors}
    
    @classmethod
    def fromDict(cls, dictionary):
        return PrivateRoom(name = dictionary["name"],
                           capacity = dictionary["capacity"],
                           bedtime = dictionary["bedtime"],
                           reservedForCounselor = dictionary["reservedForCounselors"])
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        if dictionary["bedtime"] == "":
            bedtime = None
        else:
            bedtime = timeDT(time.strptime(dictionary["bedtime"], "%H:%M:%S").tm_hour,
                             time.strptime(dictionary["bedtime"], "%H:%M:%S").tm_min,
                             time.strptime(dictionary["bedtime"], "%H:%M:%S").tm_sec)
        return PrivateRoom(name = dictionary["name"],
                           capacity = int(dictionary["capacity"]),
                           bedtime = bedtime,
                           reservedForCounselor = ast.literal_eval(dictionary["reservedForCounselors"]))
