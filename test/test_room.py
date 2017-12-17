from datetime import time
from src.mktypes import Room, Equipment, GeneralRoom, PrivateRoom

################
# Sample Cases #
################

def getRoomExample():
    return(Room("test"))

def getGeneralRoomExample():
    return(GeneralRoom("test", [Equipment.PIANO, Equipment.CANVAS]))

def getPrivateRoomExample():
    return(PrivateRoom("test", 17, [3, 7, 1], time(22, 0, 0), False))

#####################
# Constructor Tests #
#####################

def test_roomConstructorAndToDict():
    room = Room("test")
    assert (room.toDict() == {"name": "test"})


def test_generalRoomConstructorAndToDict():
    room = GeneralRoom("test", [Equipment.PIANO, Equipment.CANVAS])
    assert (room.toDict() == {"name": "test", "equipment": [Equipment.PIANO, Equipment.CANVAS]})


def test_privateRoomConstructorAndToDict():
    room = PrivateRoom("test", 17, [3, 7, 1], time(22, 0, 0), False)
    assert (room.toDict() == {"name": "test", "capacity": 17, "inhabitants": [3, 7, 1],
                              "bedtime": time(22, 0, 0), "reservedForCounselors": False})


####################
# Dictionary tests #
####################

def test_roomToDictAndFromDict():
    roomDictionary = {"name": "test"}
    assert (Room.fromDict(roomDictionary).toDict() == roomDictionary)


def test_generalRoomToDictAndFromDict():
    roomDictionary = {"name": "test", "equipment": [Equipment.PIANO, Equipment.CANVAS]}
    assert (GeneralRoom.fromDict(roomDictionary).toDict() == roomDictionary)


def test_privateRoomToDictAndFromDict():
    roomDictionary = {"name": "test", "capacity": 17, "inhabitants": [3, 7, 1],
                      "bedtime": time(22, 0, 0), "reservedForCounselors": False}
    assert (PrivateRoom.fromDict(roomDictionary).toDict() == roomDictionary)


###############
# Print Tests #
###############

def test_roomPrint():
    room = Room("test")
    assert (room.__str__() == "Room(test)")


def test_generalRoomPrint():
    generalRoom = GeneralRoom("test", [Equipment.CANVAS])
    assert (generalRoom.__str__() == "GeneralRoom(test,[<Equipment.CANVAS: 4>])")


def test_privateRoomPrint():
    privateRoom = PrivateRoom("test", 17, [3, 7, 1], time(22, 0, 0), False)
    assert (privateRoom.__str__() == "PrivateRoom(test,17,[3, 7, 1],22:00:00,False)")
