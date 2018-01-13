#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from mathecamp_konfigurator.mktypes import Schedule


################
# Sample Cases #
################

def getScheduleExample():
    return (Schedule([(1, 3, 1), (2, 4, 2)]),
            [{"mathCircleID": 1, "spaceTimeSlotID": 3, "teacherID": 1},
             {"mathCircleID": 2, "spaceTimeSlotID": 4, "teacherID": 2}])


#####################
# Constructor Tests #
#####################

def test_scheduleConstructorAndToDict():
    (schedule, scheduleDict) = getScheduleExample()
    assert (schedule.toDict() == scheduleDict)


####################
# Dictionary tests #
####################

def test_scheduleToDictAndFromDict():
    scheduleDict = getScheduleExample()[1]
    assert (Schedule.fromDict(scheduleDict).toDict() == scheduleDict)


###############
# Print Tests #
###############

def test_schedulePrint():
    schedule = getScheduleExample()[0]
    assert (schedule.__str__() == "Schedule([(1, 3, 1), (2, 4, 2)])")
