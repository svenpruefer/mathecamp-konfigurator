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

from mathecamp_konfigurator.model.mktypes import MathCircle


################
# Sample Cases #
################

def getMathCircleExample(nr = 0):
    if (nr == 0):
        return (MathCircle("10a", 10, [3, 4], 2, ["Symplektische Geometrie", "Motive"]),
                {"name": "10a", "grade": 10, "members": [3, 4], "room": 2,
                 "topics": ["Symplektische Geometrie", "Motive"]})
    else:
        return (MathCircle("5c", 5, [5], 1, []), {"name": "5c", "grade": 5, "members": [5], "room": 1,
                                                  "topics": []})


#####################
# Constructor tests #
#####################

def test_mathCircleConstructorAndToDict():
    (mathCircle, mathCircleDict) = getMathCircleExample()
    assert (mathCircle.toDict() == mathCircleDict)


####################
# Dictionary tests #
####################

def test_mathCircleToDictAndFromDict():
    mathCircleDictionary = getMathCircleExample()[1]
    assert (MathCircle.fromDict(mathCircleDictionary).toDict() == mathCircleDictionary)


###############
# Print tests #
###############

def test_mathCirclePrint():
    mathCircle = getMathCircleExample()[0]
    assert (mathCircle.__str__() == "MathCircle(10a,10,[3, 4],2,['Symplektische Geometrie', 'Motive'])")
