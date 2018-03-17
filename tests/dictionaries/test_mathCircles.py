#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mathecamp_konfigurator.model.types import MathCircle


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
