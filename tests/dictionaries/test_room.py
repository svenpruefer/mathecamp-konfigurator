from datetime import time
from mathecamp_konfigurator.mktypes import Room, Equipment, GeneralRoom, PrivateRoom


################
# Sample Cases #
################

def getRoomExample():
    return (Room("test"), {"name": "test"})


def getGeneralRoomExample(nr=0):
    if nr == 0:
        return (GeneralRoom("test", [Equipment.PIANO, Equipment.CANVAS]),
                {"name": "test", "equipment": [Equipment.PIANO, Equipment.CANVAS]})
    elif nr ==1:
        return (GeneralRoom("Scheune", [Equipment.PIANO, Equipment.CANVAS]),
                {"name": "Scheune", "equipment": [Equipment.PIANO, Equipment.CANVAS]})
    else:
        return (GeneralRoom("Mont Blanc", [Equipment.PIANO, Equipment.CANVAS]),
                {"name": "Mont Blanc", "equipment": [Equipment.PIANO, Equipment.CANVAS]})

def getPrivateRoomExample():
    return (PrivateRoom("test", 17, [3, 7, 1], time(22, 0, 0), False),
            {"name": "test", "capacity": 17, "inhabitants": [3, 7, 1],
             "bedtime": time(22, 0, 0), "reservedForCounselors": False})


#####################
# Constructor Tests #
#####################

def test_roomConstructorAndToDict():
    (room, roomDict) = getRoomExample()
    assert (room.toDict() == roomDict)


def test_generalRoomConstructorAndToDict():
    (room, roomDict) = getGeneralRoomExample()
    assert (room.toDict() == roomDict)


def test_privateRoomConstructorAndToDict():
    (room, roomDict) = getPrivateRoomExample()
    assert (room.toDict() == roomDict)


####################
# Dictionary tests #
####################

def test_roomToDictAndFromDict():
    roomDictionary = getRoomExample()[1]
    assert (Room.fromDict(roomDictionary).toDict() == roomDictionary)


def test_generalRoomToDictAndFromDict():
    roomDictionary = getGeneralRoomExample()[1]
    assert (GeneralRoom.fromDict(roomDictionary).toDict() == roomDictionary)


def test_privateRoomToDictAndFromDict():
    roomDictionary = getPrivateRoomExample()[1]
    assert (PrivateRoom.fromDict(roomDictionary).toDict() == roomDictionary)


###############
# Print Tests #
###############

def test_roomPrint():
    room = getRoomExample()[0]
    assert (room.__str__() == "Room(test)")


def test_generalRoomPrint():
    generalRoom = getGeneralRoomExample()[0]
    assert (generalRoom.__str__() == "GeneralRoom(test,[<Equipment.PIANO: 1>, <Equipment.CANVAS: 4>])")


def test_privateRoomPrint():
    privateRoom = getPrivateRoomExample()[0]
    assert (privateRoom.__str__() == "PrivateRoom(test,17,[3, 7, 1],22:00:00,False)")
