#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from mathecamp_konfigurator.mktypes import SpaceTimeSlot


################
# Sample Cases #
################

def getSpacetimeSlotExample(nr = 0):
    if nr == 0:
        return (SpaceTimeSlot(datetime(2018, 8, 22, 9, 0, 0), datetime(2018, 8, 22, 10, 30, 0), 1),
            {"beginning": datetime(2018, 8, 22, 9, 0, 0),
             "end": datetime(2018, 8, 22, 10, 30, 0),
             "room": 1})
    elif nr == 1:
        return (SpaceTimeSlot(datetime(2018, 8, 23, 14, 0, 0), datetime(2018, 8, 23, 16, 30, 0), 2),
                {"beginning": datetime(2018, 8, 23, 14, 0, 0),
                 "end": datetime(2018, 8, 23, 16, 30, 0),
                 "room": 2})
    elif nr == 2:
        return (SpaceTimeSlot(datetime(2018, 8, 23, 14, 30, 0), datetime(2018, 8, 23, 18, 0, 0), 3),
                {"beginning": datetime(2018, 8, 23, 14, 30, 0),
                 "end": datetime(2018, 8, 23, 18, 0, 0),
                 "room": 3})
    else:
        return (SpaceTimeSlot(datetime(2018, 8, 22, 9, 0, 0), datetime(2018, 8, 22, 10, 30, 0), 2),
                {"beginning": datetime(2018, 8, 22, 9, 0, 0),
                 "end": datetime(2018, 8, 22, 10, 30, 0),
                 "room": 2})


#####################
# Constructor Tests #
#####################

def test_spacetimeSlotConstructorAndToDict():
    (spacetimeslot, spacetimeSlotDict) = getSpacetimeSlotExample()
    assert (spacetimeslot.toDict() == spacetimeSlotDict)


####################
# Dictionary tests #
####################

def test_spacetimeSlotToDictAndFromDict():
    spacetimeSlotDictionary = getSpacetimeSlotExample()[1]
    assert (SpaceTimeSlot.fromDict(spacetimeSlotDictionary).toDict() == spacetimeSlotDictionary)


###############
# Print Tests #
###############

def test_spacetimeSlotPrint():
    spacetimeSlot = getSpacetimeSlotExample()[0]
    assert (spacetimeSlot.__str__() == "SpaceTimeSlot([2018-08-22 09:00:00,2018-08-22 10:30:00],1)")
