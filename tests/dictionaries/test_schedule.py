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

from mathecamp_konfigurator.model.mktypes import Schedule


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
