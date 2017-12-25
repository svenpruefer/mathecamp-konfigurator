from datetime import datetime
from src.mktypes import SpaceTimeSlot


################
# Sample Cases #
################

def getSpacetimeSlotExample():
    return (SpaceTimeSlot(datetime(2018, 8, 22, 9, 0, 0), datetime(2018, 8, 22, 10, 30, 0), 1),
            {"beginning": datetime(2018, 8, 22, 9, 0, 0),
             "end": datetime(2018, 8, 22, 10, 30, 0),
             "room": 1})


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
