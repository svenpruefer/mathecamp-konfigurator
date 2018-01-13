#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from mathecamp_konfigurator.camp import mathecamp
from tests.dictionaries.test_people import getCounselorExample, getParticipantExample, getGuestExample
from tests.dictionaries.test_room import getGeneralRoomExample, getPrivateRoomExample
from tests.dictionaries.test_activities import getActivityExample
from tests.dictionaries.test_mathCircles import getMathCircleExample
from tests.dictionaries.test_spacetimeSlot import getSpacetimeSlotExample
from tests.dictionaries.test_expenses import getExpenseExample
from tests.dictionaries.test_schedule import getScheduleExample
from datetime import datetime


################
# Sample Cases #
################

def getMathecampExample():
    counselors = {"1": getCounselorExample(0)[0], "2": getCounselorExample(1)[0]}
    participants = {"3": getParticipantExample(0)[0], "4": getParticipantExample(1)[0],
                    "5": getParticipantExample(2)[0]}
    guests = {"6": getGuestExample()[0]}
    privateRooms = {"4": getPrivateRoomExample(0)[0], "5": getPrivateRoomExample(1)[0],
                    "6": getPrivateRoomExample(2)[0]}
    generalRooms = {"1": getGeneralRoomExample(0)[0], "2": getGeneralRoomExample(1)[0],
                    "3": getGeneralRoomExample(2)[0]}
    activities = {"1": getActivityExample(0)[0], "2": getActivityExample(1)[0]}
    mathCircles = {"1": getMathCircleExample(0)[0], "2": getMathCircleExample(1)[0]}
    spactimeSlots = {"1": getSpacetimeSlotExample(0)[0], "2": getSpacetimeSlotExample(1)[0],
                     "3": getSpacetimeSlotExample(2)[0], "4": getSpacetimeSlotExample(3)[0]}
    expenses = {"1": getExpenseExample()[0]}
    schedule = getScheduleExample()[1]
    nextHumanId = 7
    nextRoomId = 4
    nextActivityId = 3
    nextMathCircleId = 3
    nextExpenseId = 2
    nextSpaceTimeSlotId = 4
    startTime = datetime(2018, 8, 18, 10, 0, 0)
    endTime = datetime(2018, 8, 26, 11, 30, 0)
    
    return ([mathecamp(startTime, endTime, nextHumanId, nextRoomId,
                       nextActivityId, nextMathCircleId, nextExpenseId, nextSpaceTimeSlotId, generalRooms, privateRooms,
                       activities, spactimeSlots, mathCircles, expenses, participants, counselors, guests, schedule),
             {
                 "generalData": {"startDate": startTime, "endDate": endTime, "nextHumanId": nextHumanId,
                                 "nextActivityId": nextActivityId, "nextRoomId": nextRoomId, "nextExpenseId":
                                     nextExpenseId, "nextSpaceTimeSlotId": nextSpaceTimeSlotId, "nextMathCircleId":
                                     nextMathCircleId},
                 "generalRooms": {x: y.toDict() for (x, y) in generalRooms.items()},
                 "privateRooms": {x: y.toDict() for (x, y) in privateRooms.items()},
                 "activities": {x: y.toDict() for (x, y) in activities.items()},
                 "mathCircles": {x: y.toDict() for (x, y) in mathCircles.items()},
                 "expenses": {x: y.toDict() for (x, y) in expenses.items()},
                 "participants": {x: y.toDict() for (x, y) in participants.items()},
                 "counselors": {x: y.toDict() for (x, y) in counselors.items()},
                 "guests": {x: y.toDict() for (x, y) in guests.items()},
                 "spacetimeSlots": {x: y.toDict() for (x, y) in spactimeSlots.items()}
             }])


#####################
# Constructor tests #
#####################

def test_mathecampConstructorAndToDict():
    mathecamp = getMathecampExample()[0]
    assert (mathecamp.toDict() == getMathecampExample()[1])


####################
# Dictionary tests #
####################

@pytest.mark.skip(reason = "mathecamp.fromDict not implemented yet")
def test_mathecampToDictAndFromDict():
    mathecampDictionary = getMathecampExample()[1]
    assert (mathecamp.fromDict(mathecampDictionary).toDict() == mathecampDictionary)


###############
# Print tests #
###############

@pytest.mark.skip(reason = "result still needs to be determined")
def test_mathecampPrint():
    mathecamp = getMathecampExample()
    assert (mathecamp.__str__() == "")

#######################
# Adding methods test #
#######################
