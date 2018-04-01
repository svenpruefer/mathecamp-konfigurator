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

import ast
from mathecamp_konfigurator import db


class Expense(db.Model):
    """
    This class represents an expense for something.
    """

    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    name = db.Column(db.String(128))

    amount = db.Column(db.Float)

    payedAlready = db.Column(db.Boolean)

    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    activity = db.relationship("Activity", back_populates = "expense")

    def __repr__(self):
        return ("Expense({0},{1},{2},{3})".format(self.name, self.amount, self.activity_id, self.payedAlready))

    def toDict(self):
        return ({"name": self.name, "amount": self.amount, "activity_id": self.activity_id, "payedAlready":
            self.payedAlready})

    @classmethod
    def fromDict(cls, dictionary):
        return (Expense(name = dictionary["name"], amount = dictionary["amount"], activity_id = dictionary[
            "activity_id"], payedAlready = dictionary["payedAlready"]))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Expense(name = dictionary["name"],
                        amount = float(dictionary["amount"]),
                        activity_id = int(dictionary["usage"]),
                        payedAlready = ast.literal_eval(dictionary["payedAlready"])))
