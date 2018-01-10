#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mathecamp_konfigurator.mktypes import Activity


################
# Sample Cases #
################

def getActivityExample(nr=0):
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
