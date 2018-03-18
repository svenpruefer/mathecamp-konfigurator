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

from datetime import datetime
from mathecamp_konfigurator import db


class Activity(db.Model):
    """
        This class represents an activity such as afternoon activities or bigger projects that need to be organized or
        planned.
    """
    
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    time = db.Column(db.DateTime)
    
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    room = db.relationship("Room")
    
    expense = db.relationship("Expense", back_populates = "activity")
    
    def __repr__(self):
        return ("Activity({0},{1},{2})".format(self.name, self.time, self.room_id))
    
    def toDict(self):
        return ({"name": self.name, "time": self.time, "room_id": self.room_id})
    
    @classmethod
    def fromDict(cls, dictionary):
        return (Activity(name = dictionary["name"], time = dictionary["time"], room_id = dictionary["room_id"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Activity(dictionary["name"],
                         datetime.strptime(dictionary["time"], "%Y-%m-%d %H:%M:%S"),
                         int(dictionary["room_id"])))
