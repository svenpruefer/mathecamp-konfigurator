#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import time, date, datetime
from mathecamp_konfigurator.mktypes import Room, Equipment, GeneralRoom, PrivateRoom, Gender, TransportType, FoodRestriction
from mathecamp_konfigurator.people import Human, Participant, Counselor, Guest


################
# Sample Cases #
################

def getHumanExample():
    return (Human("Ferdinand", "Karl", date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                  "Karl-Liebknecht-Str.", "13", "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                  TransportType.BUS,
                  datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                  "Supercooler Typ!!!", 42),
            {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
             "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
             "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
             "postalCode": "86153", "place": "Entenhausen", "streetNumber": "13",
             "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
             "departureTime": datetime(2018, 8, 27, 11, 30, 0),
             "departureType": TransportType.PRIVATE,
             "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
             "miscellaneous": "Supercooler Typ!!!",
             "room": 42})


def getParticipantExample(nameNo = 0):
    if nameNo == 1:
        name = ("Epunkt", "Jost")
    elif nameNo == 2:
        name = ("Marx", "Karl")
    else:
        name = ("Weihnachtsmann", "Der")
    return (Participant(name[0], name[1], date(1987, 8, 20), 300, False, "10a", 10, ["Programmieren"],
                        ["test@musmehl.de"], ["test2@musmehl.de"], Gender.MALE, ["01112222222"], {}, 42,
                        "Karl-Liebknecht-Str.", "13", "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                        TransportType.BUS, datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, ["Uroma"],
                        [50, 62], ["Geige"], ["Kokain"], [FoodRestriction.CELIAC_DISEASE], ["Schnupfen"], False,
                        True, True, True, "Supercooler Typ!!!"),
            {"familyName": name[0], "givenName": name[1], "birthDate": date(1987, 8, 20),
             "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
             "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
             "postalCode": "86153", "place": "Entenhausen", "streetNumber": "13",
             "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
             "departureTime": datetime(2018, 8, 27, 11, 30, 0),
             "departureType": TransportType.PRIVATE,
             "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
             "miscellaneous": "Supercooler Typ!!!",
             "room": 42, "campPrice": 300, "moneyPayedAlready": False, "circle": "10a",
             "grade": 10,
             "topicWishes": ["Programmieren"], "emailAddressesParents": ["test2@musmehl.de"],
             "phoneNumbersEmergency": {}, "departureOtherPerson": ["Uroma"],
             "friends": [50, 62],
             "instrument": ["Geige"], "medicalDrugs": ["Kokain"], "illness": ["Schnupfen"],
             "rideSharing": False, "swimmingPermission": True, "leavingPermission": True,
             "sportsPermission": True})


def getCounselorExample(nameNo = 0):
    if nameNo == 1:
        name = ("Man", "Iron")
    else:
        name = ("Merkel", "Angela")
    return (Counselor(name[0], name[1], date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                      "Karl-Liebknecht-Str.", "13", "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                      TransportType.BUS,
                      datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                      "Supercooler Typ!!!", 42, [8, 9]),
            {"familyName": name[0], "givenName": name[1], "birthDate": date(1987, 8, 20),
             "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
             "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
             "postalCode": "86153", "place": "Entenhausen", "streetNumber": "13",
             "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
             "departureTime": datetime(2018, 8, 27, 11, 30, 0),
             "departureType": TransportType.PRIVATE,
             "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
             "miscellaneous": "Supercooler Typ!!!",
             "room": 42, "preferredGrades": [8, 9]})


def getGuestExample():
    return (Guest("Bombadil", "Tom", date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                  "Karl-Liebknecht-Str.", "13", "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                  TransportType.BUS,
                  datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                  "Supercooler Typ!!!", 42),
            {"familyName": "Bombadil", "givenName": "Tom", "birthDate": date(1987, 8, 20),
             "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
             "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
             "postalCode": "86153", "place": "Entenhausen", "streetNumber": "13",
             "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
             "departureTime": datetime(2018, 8, 27, 11, 30, 0),
             "departureType": TransportType.PRIVATE,
             "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
             "miscellaneous": "Supercooler Typ!!!",
             "room": 42})


#####################
# Constructor tests #
#####################

def test_humanConstructorAndToDict():
    (human, humanDict) = getHumanExample()
    assert (human.toDict() == humanDict)


def test_participantConstructorAndToDict():
    (participant, participantDict) = getParticipantExample()
    assert (participant.toDict() == participantDict)


def test_counselorConstructorAndToDict():
    (counselor, counselorDict) = getCounselorExample()
    assert (counselor.toDict() == counselorDict)


def test_guestConstructorAndToDict():
    (guest, guestDict) = getGuestExample()
    assert (guest.toDict() == guestDict)


####################
# Dictionary tests #
####################

def test_humanToDictAndFromDict():
    humanDictionary = getHumanExample()[1]
    assert (Human.fromDict(humanDictionary).toDict() == humanDictionary)


def test_participantToDictAndFromDict():
    participantDict = getParticipantExample()[1]
    assert (Participant.fromDict(participantDict).toDict() == participantDict)


def test_counselorToDictAndFromDict():
    counselorDict = getCounselorExample()[1]
    assert (Counselor.fromDict(counselorDict).toDict() == counselorDict)


def test_guestToDictAndFromDict():
    guestDict = getGuestExample()[1]
    assert (Guest.fromDict(guestDict).toDict() == guestDict)


###############
# Print tests #
###############

def test_humanPrint():
    human = getHumanExample()[0]
    assert (
        human.__str__() == "Human(Ferdinand,Karl,1987-08-20,Gender.MALE,['test@musmehl.de'],['01112222222'],"
        + "Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,TransportType.BUS,2018-08-27 11:30:00,"
        + "TransportType.PRIVATE,[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42)")


def test_participantPrint():
    participant = getParticipantExample()[0]
    assert (participant.__str__() == "Participant(Weihnachtsmann,Der,1987-08-20,Gender.MALE,['test@musmehl.de'],"
            + "['01112222222'],Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,TransportType.BUS,"
            + "2018-08-27 11:30:00,TransportType.PRIVATE,[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,"
            + "42, 300, False, 10a, 10, ['Programmieren'], ['test2@musmehl.de'], {}, ['Uroma'], [50, 62], ['Geige'],"
            + " ['Kokain'], ['Schnupfen'], False, True, True, True)")


def test_counselorPrint():
    counselor = getCounselorExample()[0]
    assert (
        counselor.__str__() == "Counselor(Merkel,Angela,1987-08-20,Gender.MALE,['test@musmehl.de'],['01112222222'],"
        + "Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,TransportType.BUS,2018-08-27 11:30:00,"
        + "TransportType.PRIVATE,[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42, [8, 9])")


def test_guestPrint():
    guest = getGuestExample()[0]
    assert (
        guest.__str__() == "Guest(Bombadil,Tom,1987-08-20,Gender.MALE,['test@musmehl.de'],['01112222222'],"
        + "Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,TransportType.BUS,2018-08-27 11:30:00,"
        + "TransportType.PRIVATE,[FoodRestriction.CELIAC_DISEASE],Supercooler Typ!!!,42)")
