from mathecamp_konfigurator.camp import mathecamp
from tests.dictionaries.test_people import getCounselorExample, getParticipantExample, getGuestExample
from datetime import datetime


################
# Sample Cases #
################

# TODO write Mathecamp test example

def getMathecampExample():
    counselors = {"1" : getCounselorExample(0)[0], "2" : getCounselorExample(1)[0]}
    participants = {"3" : getParticipantExample(0)[0], "4" : getParticipantExample(1)[0], "5" : getParticipantExample(2)[0]}
    guests = {"6" : getGuestExample()[0]}
    privateRooms = {}
    generalRooms = {}
    activities = {}
    mathCircles = {}
    spactimeSlots = {}
    expenses = {}
    schedule = []
    nextHumanId = 7
    nextRoomId = 4
    nextActivityId = 3
    nextMathCircleId = 3
    nextExpenseId = 2
    nextSpaceTimeSlotId = 4

    return(mathecamp(datetime(2018, 8, 18, 10, 0, 0), datetime(2018, 8, 26, 11, 30, 0), nextHumanId, nextRoomId,
                     nextActivityId, nextMathCircleId, nextExpenseId, nextSpaceTimeSlotId, generalRooms, privateRooms,
                     activities, spactimeSlots, mathCircles, expenses, participants, counselors, guests, schedule))


#####################
# Constructor tests #
#####################

def test_mathecampConstructorAndToDict():
    mathecamp = getMathecampExample()
    assert (mathecamp.toDict() == {})


####################
# Dictionary tests #
####################

def test_mathecampToDictAndFromDict():
    mathecampDictionary = {}
    assert (mathecamp.fromDict(mathecampDictionary).toDict() == mathecampDictionary)


###############
# Print tests #
###############

def test_mathecampPrint():
    mathecamp = getMathecampExample()
    assert (mathecamp.__str__() == "")

#######################
# Adding methods test #
#######################
