from datetime import time
from src.mktypes import Room, Equipment, GeneralRoom, PrivateRoom

def test_roomConstructorAndToDict():
    room = Room("test")
    assert(room.toDict() == {"name": "test"})


def test_generalRoomConstructorAndToDict():
    room = GeneralRoom("test", [Equipment.PIANO, Equipment.CANVAS])
    assert(room.toDict() == {"name": "test", "equipment": [Equipment.PIANO, Equipment.CANVAS]})


def test_privateRoomConstructorAndToDict():
    room = PrivateRoom("test", 17, [3, 7, 1], time(22, 0, 0), False)
    assert(room.toDict() == {"name": "test", "capacity": 17, "inhabitants": [3, 7, 1],
                                     "bedtime": time(22, 0, 0), "reservedForCounselors": False})


def test_roomToDictAndFromDict():
    roomDictionary = {"name": "test"}
    assert(Room.fromDict(roomDictionary).toDict() == roomDictionary)


def test_generalRoomToDictAndFromDict():
    roomDictionary = {"name": "test", "equipment": [Equipment.PIANO, Equipment.CANVAS]}
    assert(GeneralRoom.fromDict(roomDictionary).toDict() == roomDictionary)


def test_privateRoomToDictAndFromDict():
    roomDictionary = {"name": "test", "capacity": 17, "inhabitants": [3, 7, 1],
                      "bedtime": time(22, 0, 0), "reservedForCounselors": False}
    assert(PrivateRoom.fromDict(roomDictionary).toDict() == roomDictionary)
