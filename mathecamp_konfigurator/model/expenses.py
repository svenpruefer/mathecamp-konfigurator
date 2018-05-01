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

"""This file defines expenses"""

__docformat__ = 'reStructuredText'

###########
# Imports #
###########

import ast


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
