from datetime import datetime
from src.mktypes import Schedule


################
# Sample Cases #
################

def getScheduleExample():
    return (Schedule([(1, 1, 1), (2, 2, 3)]),
            [{"mathCircleID": 1, "spaceTimeSlotID": 1, "teacherID": 1},
             {"mathCircleID": 2, "spaceTimeSlotID": 2, "teacherID": 3}])


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
    assert (schedule.__str__() == "Schedule([(1, 1, 1), (2, 2, 3)])")
