#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from mathecamp_konfigurator.camp import Mathecamp
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
    schedule = getScheduleExample()
    nextHumanId = 7
    nextRoomId = 4
    nextActivityId = 3
    nextMathCircleId = 3
    nextExpenseId = 2
    nextSpaceTimeSlotId = 4
    startTime = datetime(2018, 8, 18, 10, 0, 0)
    endTime = datetime(2018, 8, 26, 11, 30, 0)

    return ([Mathecamp(startTime, endTime, nextHumanId, nextRoomId,
                       nextActivityId, nextMathCircleId, nextExpenseId, nextSpaceTimeSlotId, generalRooms, privateRooms,
                       activities, spactimeSlots, mathCircles, expenses, participants, counselors, guests, schedule[0]),
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
                 "spacetimeSlots": {x: y.toDict() for (x, y) in spactimeSlots.items()},
                 "schedule": schedule[1]
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

def test_mathecampToDictAndFromDict():
    mathecampDictionary = getMathecampExample()[1]
    assert (Mathecamp.fromDict(mathecampDictionary).toDict() == mathecampDictionary)


###############
# Print tests #
###############

def test_mathecampPrint():
    mathecamp = getMathecampExample()[0]
    print(mathecamp)
    assert (mathecamp.__str__() == "Mathecamp(2018-08-18 10:00:00, 2018-08-26 11:30:00,"
                                   " 7, 4, 3, 3, 2, 4, "
                                   "{'1': 'GeneralRoom(test,[Equipment.PIANO, Equipment.WHITEBOARD])', "
                                   "'2': 'GeneralRoom(Scheune,[Equipment.BLACKBOARD])', "
                                   "'3': 'GeneralRoom(Mont Blanc,[])'}, "
                                   "{'4': 'PrivateRoom(test,4,[3, 4, 5],22:00:00,False)', "
                                   "'5': 'PrivateRoom(test,2,[1, 2],None,True)', "
                                   "'6': 'PrivateRoom(test,4,[],None,False)'}, "
                                   "{'1': 'Activity(Fußball,2,[1, 2],[3],[1])', "
                                   "'2': 'Activity(Free-Solo-Klettern,3,[1, 2, 3, 5, 6, 4],[5, 6],[2])'}, "
                                   "{'1': 'SpaceTimeSlot([2018-08-22 09:00:00,2018-08-22 10:30:00],1)', "
                                   "'2': 'SpaceTimeSlot([2018-08-23 14:00:00,2018-08-23 16:30:00],2)', "
                                   "'3': 'SpaceTimeSlot([2018-08-23 14:30:00,2018-08-23 18:00:00],3)', "
                                   "'4': 'SpaceTimeSlot([2018-08-22 09:00:00,2018-08-22 10:30:00],2)'}, "
                                   "{'1': \"MathCircle(10a,10,[3, 4],2,['Symplektische Geometrie', 'Motive'])\", "
                                   "'2': 'MathCircle(5c,5,[5],1,[])'}, "
                                   "{'1': 'Expense(Garn,20,[1, 2],False)'}, "
                                   "{'3': \"Participant(Weihnachtsmann,Der,1987-08-20,Gender.MALE,['test@musmehl.de'],"
                                   "['01112222222'],Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,"
                                   "TransportType.BUS,2018-08-27 11:30:00,TransportType.PRIVATE,"
                                   "[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42, 300, False, 10a, 10, "
                                   "['Programmieren'], ['test2@musmehl.de'], {}, ['Uroma'], [50, 62], ['Geige'], "
                                   "['Kokain'], ['Schnupfen'], False, True, True, True)\", "
                                   "'4': \"Participant(Epunkt,Jost,1987-08-20,Gender.MALE,['test@musmehl.de'],"
                                   "['01112222222'],Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,"
                                   "TransportType.BUS,2018-08-27 11:30:00,TransportType.PRIVATE,"
                                   "[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42, 300, False, 10a, 10, "
                                   "['Programmieren'], ['test2@musmehl.de'], {}, ['Uroma'], [50, 62], ['Geige'], "
                                   "['Kokain'], ['Schnupfen'], False, True, True, True)\", "
                                   "'5': \"Participant(Marx,Karl,1987-08-20,Gender.MALE,['test@musmehl.de'],"
                                   "['01112222222'],Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,"
                                   "TransportType.BUS,2018-08-27 11:30:00,TransportType.PRIVATE,"
                                   "[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42, 300, False, 10a, 10, "
                                   "['Programmieren'], ['test2@musmehl.de'], {}, ['Uroma'], [50, 62], ['Geige'], "
                                   "['Kokain'], ['Schnupfen'], False, True, True, True)\"}, "
                                   "{'1': \"Counselor(Merkel,Angela,1987-08-20,Gender.MALE,['test@musmehl.de'],"
                                   "['01112222222'],Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,"
                                   "TransportType.BUS,2018-08-27 11:30:00,TransportType.PRIVATE,"
                                   "[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42, [8, 9])\", "
                                   "'2': \"Counselor(Man,Iron,1987-08-20,Gender.MALE,['test@musmehl.de'],"
                                   "['01112222222'],Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,"
                                   "TransportType.BUS,2018-08-27 11:30:00,TransportType.PRIVATE,"
                                   "[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42, [8, 9])\"}, "
                                   "{'6': \"Guest(Bombadil,Tom,1987-08-20,Gender.MALE,['test@musmehl.de'],"
                                   "['01112222222'],Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,"
                                   "TransportType.BUS,2018-08-27 11:30:00,TransportType.PRIVATE,"
                                   "[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42)\"}, "
                                   "Schedule([(1, 3, 1), (2, 4, 2)]))")

#######################
# Adding methods test #
#######################
