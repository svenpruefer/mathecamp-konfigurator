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

from datetime import time
from mathecamp_konfigurator.model.rooms import Room, Equipment, GeneralRoom, PrivateRoom


################
# Sample Cases #
################

def getRoomExample():
    return (Room("test"), {"name": "test"})


def getGeneralRoomExample(nr = 0):
    if nr == 0:
        return (GeneralRoom("test", [Equipment("PIANO"), Equipment("WHITEBOARD")]),
                {"name": "test", "equipment": [Equipment("PIANO"), Equipment("WHITEBOARD")]})
    elif nr == 1:
        return (GeneralRoom("Scheune", [Equipment("BLACKBOARD")]),
                {"name": "Scheune", "equipment": [Equipment("BLACKBOARD")]})
    else:
        return (GeneralRoom("Mont Blanc", []),
                {"name": "Mont Blanc", "equipment": []})


def getPrivateRoomExample(nr = 0):
    if nr == 0:
        return (PrivateRoom("test", 4, [3, 4, 5], time(22, 0, 0), False),
                {"name": "test", "capacity": 4, "inhabitants": [3, 4, 5],
                 "bedtime": time(22, 0, 0), "reservedForCounselors": False})
    elif nr == 1:
        return (PrivateRoom("test", 2, [1, 2], None, True),
                {"name": "test", "capacity": 2, "inhabitants": [1, 2],
                 "bedtime": None, "reservedForCounselors": True})
    else:
        return (PrivateRoom("test", 4, [], None, False),
                {"name": "test", "capacity": 4, "inhabitants": [],
                 "bedtime": None, "reservedForCounselors": False})


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
    assert (generalRoom.__str__() == "GeneralRoom(test,[Equipment.PIANO, Equipment.WHITEBOARD])")


def test_privateRoomPrint():
    privateRoom = getPrivateRoomExample()[0]
    assert (privateRoom.__str__() == "PrivateRoom(test,4,[3, 4, 5],22:00:00,False)")
