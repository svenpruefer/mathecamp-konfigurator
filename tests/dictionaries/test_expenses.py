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

from mathecamp_konfigurator.model.types import Expense


################
# Sample Cases #
################

def getExpenseExample():
    return (Expense("Garn", 20, [1, 2], False), {"name": "Garn", "amount": 20, "usage": [1, 2], "payedAlready": False})


#####################
# Constructor tests #
#####################

def test_expenseConstructorAndToDict():
    (expense, expenseDict) = getExpenseExample()
    assert (expense.toDict() == expenseDict)


####################
# Dictionary tests #
####################

def test_expenseToDictAndFromDict():
    expenseDictionary = getExpenseExample()[1]
    assert (Expense.fromDict(expenseDictionary).toDict() == expenseDictionary)


###############
# Print tests #
###############

def test_expensePrint():
    expense = getExpenseExample()[0]
    assert (expense.__str__() == "Expense(Garn,20,[1, 2],False)")
