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

from mathecamp_konfigurator.model.types import Activity


################
# Sample Cases #
################

def getActivityExample(nr = 0):
    if nr == 0:
        return (Activity("Fußball", 2, [1, 2], [3], [1]),
                {"name": "Fußball", "timeAndPlace": 2, "participants": [1, 2], "organizers": [3],
                 "expenses": [1]})
    else:
        return (Activity("Free-Solo-Klettern", 3, [1, 2, 3, 5, 6, 4], [5, 6], [2]),
                {"name": "Free-Solo-Klettern", "timeAndPlace": 3, "participants": [1, 2, 3, 5, 6, 4],
                 "organizers": [5, 6], "expenses": [2]})


#####################
# Constructor tests #
#####################

def test_activityConstructorAndToDict():
    (activity, activityDict) = getActivityExample()
    assert (activity.toDict() == activityDict)


####################
# Dictionary tests #
####################

def test_activityToDictAndFromDict():
    activityDictionary = getActivityExample()[1]
    assert (Activity.fromDict(activityDictionary).toDict() == activityDictionary)


###############
# Print tests #
###############

def test_activityPrint():
    activity = getActivityExample()[0]
    assert (activity.__str__() == "Activity(Fußball,2,[1, 2],[3],[1])")
