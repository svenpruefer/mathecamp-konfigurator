from src.mktypes import Activity


################
# Sample Cases #
################

def getActivityExample():
    return (Activity("Fußball", 2, [1,2], [3], [1]))


#####################
# Constructor tests #
#####################

def test_activityConstructorAndToDict():
    activity = getActivityExample()
    assert (activity.toDict() == {"name": "Fußball", "timeAndPlace": 2, "participants": [1,2], "organizers": [3],
                                    "expenses": [1]})


####################
# Dictionary tests #
####################

def test_activityToDictAndFromDict():
    activityDictionary = {"name": "Fußball", "timeAndPlace": 2, "participants": [1,2], "organizers": [3],
                            "expenses": [1]}
    assert (Activity.fromDict(activityDictionary).toDict() == activityDictionary)


###############
# Print tests #
###############

def test_activityPrint():
    activity = getActivityExample()
    assert (activity.__str__() == "Activity(Fußball,2,[1, 2],[3],[1])")
