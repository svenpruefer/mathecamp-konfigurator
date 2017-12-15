from datetime import time, date, datetime
from src.mktypes import Room, Equipment, GeneralRoom, PrivateRoom, Gender, TransportType, FoodRestriction
from src.people import Human, Participant, Counselor, Guest


#####################
# Constructor tests #
#####################

def test_humanConstructorAndToDict():
    human = Human("Ferdinand", "Karl", date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                  "Karl-Liebknecht-Str.", 13, "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                  TransportType.BUS,
                  datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                  "Supercooler Typ!!!", 42)
    assert (human.toDict() == {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
                               "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
                               "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
                               "postalCode": "86153", "place": "Entenhausen", "streetNumber": 13,
                               "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
                               "departureTime": datetime(2018, 8, 27, 11, 30, 0),
                               "departureType": TransportType.PRIVATE,
                               "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
                               "miscellaneuos": "Supercooler Typ!!!",
                               "room": 42})


def test_participantConstructorAndToDict():
    participant = Participant("Ferdinand", "Karl", date(1987, 8, 20), 300, False, "10a", 10, ["Programmieren"],
                              ["test@musmehl.de"], ["test2@musmehl.de"], Gender.MALE, ["01112222222"], {}, 42,
                              "Karl-Liebknecht-Str.", "13", "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                              TransportType.BUS, datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, ["Uroma"],
                              [50, 62], ["Geige"], ["Kokain"], [FoodRestriction.CELIAC_DISEASE], ["Schnupfen"], False,
                              True, True, True, "Supercooler Typ!!!")
    assert (participant.toDict() == {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
                                     "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
                                     "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
                                     "postalCode": "86153", "place": "Entenhausen", "streetNumber": "13",
                                     "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
                                     "departureTime": datetime(2018, 8, 27, 11, 30, 0),
                                     "departureType": TransportType.PRIVATE,
                                     "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
                                     "miscellaneuos": "Supercooler Typ!!!",
                                     "room": 42, "campPrice": 300, "moneyPayedAlready": False, "circle": "10a",
                                     "grade": 10,
                                     "topicWishes": ["Programmieren"], "emailAddressesParents": ["test2@musmehl.de"],
                                     "phoneNumbersEmergency": {}, "departureOtherPerson": ["Uroma"],
                                     "friends": [50, 62],
                                     "instrument": ["Geige"], "medicalDrugs": ["Kokain"], "illness": ["Schnupfen"],
                                     "rideSharing": False, "swimmingPermission": True, "leavingPermission": True,
                                     "sportsPermission": True})


def test_counselorConstructorAndToDict():
    counselor = Counselor("Ferdinand", "Karl", date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                          "Karl-Liebknecht-Str.", 13, "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                          TransportType.BUS,
                          datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                          "Supercooler Typ!!!", 42, [8, 9])
    assert (counselor.toDict() == {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
                                   "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
                                   "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
                                   "postalCode": "86153", "place": "Entenhausen", "streetNumber": 13,
                                   "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
                                   "departureTime": datetime(2018, 8, 27, 11, 30, 0),
                                   "departureType": TransportType.PRIVATE,
                                   "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
                                   "miscellaneuos": "Supercooler Typ!!!",
                                   "room": 42, "preferredGrades": [8, 9]})


def test_guestConstructorAndToDict():
    guest = Guest("Ferdinand", "Karl", date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                  "Karl-Liebknecht-Str.", 13, "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                  TransportType.BUS,
                  datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                  "Supercooler Typ!!!", 42)
    assert (guest.toDict() == {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
                               "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
                               "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
                               "postalCode": "86153", "place": "Entenhausen", "streetNumber": 13,
                               "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
                               "departureTime": datetime(2018, 8, 27, 11, 30, 0),
                               "departureType": TransportType.PRIVATE,
                               "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
                               "miscellaneuos": "Supercooler Typ!!!",
                               "room": 42})


####################
# Dictionary tests #
####################

def test_humanToDictAndFromDict():
    humanDictionary = {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
                       "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
                       "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
                       "postalCode": "86153", "place": "Entenhausen", "streetNumber": 13,
                       "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
                       "departureTime": datetime(2018, 8, 27, 11, 30, 0), "departureType": TransportType.PRIVATE,
                       "foodRestrictions": [FoodRestriction.CELIAC_DISEASE], "miscellaneuos": "Supercooler Typ!!!",
                       "room": 42}
    assert (Human.fromDict(humanDictionary).toDict() == humanDictionary)


def test_participantToDictAndFromDict():
    participantDict = {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
                       "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
                       "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
                       "postalCode": "86153", "place": "Entenhausen", "streetNumber": "13",
                       "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
                       "departureTime": datetime(2018, 8, 27, 11, 30, 0),
                       "departureType": TransportType.PRIVATE,
                       "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
                       "miscellaneuos": "Supercooler Typ!!!",
                       "room": 42, "campPrice": 300, "moneyPayedAlready": False, "circle": "10a",
                       "grade": 10,
                       "topicWishes": ["Programmieren"], "emailAddressesParents": ["test2@musmehl.de"],
                       "phoneNumbersEmergency": {}, "departureOtherPerson": ["Uroma"],
                       "friends": [50, 62],
                       "instrument": ["Geige"], "medicalDrugs": ["Kokain"], "illness": ["Schnupfen"],
                       "rideSharing": False, "swimmingPermission": True, "leavingPermission": True,
                       "sportsPermission": True}
    assert (Participant.fromDict(participantDict).toDict() == participantDict)


def test_counselorToDictAndFromDict():
    counselorDict = {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
                     "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
                     "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
                     "postalCode": "86153", "place": "Entenhausen", "streetNumber": 13,
                     "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
                     "departureTime": datetime(2018, 8, 27, 11, 30, 0),
                     "departureType": TransportType.PRIVATE,
                     "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
                     "miscellaneuos": "Supercooler Typ!!!",
                     "room": 42, "preferredGrades": [8, 9]}
    assert (Counselor.fromDict(counselorDict).toDict() == counselorDict)


def test_guestToDictAndFromDict():
    guestDict = {"familyName": "Ferdinand", "givenName": "Karl", "birthDate": date(1987, 8, 20),
                 "gender": Gender.MALE, "emailAddresses": ["test@musmehl.de"],
                 "phoneNumbers": ["01112222222"], "street": "Karl-Liebknecht-Str.",
                 "postalCode": "86153", "place": "Entenhausen", "streetNumber": 13,
                 "arrivalTime": datetime(2018, 8, 19, 9, 30, 0), "arrivalType": TransportType.BUS,
                 "departureTime": datetime(2018, 8, 27, 11, 30, 0),
                 "departureType": TransportType.PRIVATE,
                 "foodRestrictions": [FoodRestriction.CELIAC_DISEASE],
                 "miscellaneuos": "Supercooler Typ!!!",
                 "room": 42}
    assert (Guest.fromDict(guestDict).toDict() == guestDict)


###############
# Print tests #
###############

def test_humanPrint():
    human = Human("Ferdinand", "Karl", date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                  "Karl-Liebknecht-Str.", 13, "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                  TransportType.BUS,
                  datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                  "Supercooler Typ!!!", 42)
    assert (
        human.__str__() == "Human(Ferdinand,Karl,1987-08-20,Gender.MALE,['test@musmehl.de'],['01112222222'],"
        + "Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,TransportType.BUS,2018-08-27 11:30:00,"
        + "TransportType.PRIVATE,[<FoodRestriction.CELIAC_DISEASE: 5>],Supercooler Typ!!!,42)")


def test_participantPrint():
    participant = Participant("Ferdinand", "Karl", date(1987, 8, 20), 300, False, "10a", 10, ["Programmieren"],
                              ["test@musmehl.de"], ["test2@musmehl.de"], Gender.MALE, ["01112222222"], {}, 42,
                              "Karl-Liebknecht-Str.", "13", "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                              TransportType.BUS, datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, ["Uroma"],
                              [50, 62], ["Geige"], ["Kokain"], [FoodRestriction.CELIAC_DISEASE], ["Schnupfen"], False,
                              True, True, True, "Supercooler Typ!!!")
    assert (participant.__str__() == "Participant(Ferdinand,Karl,1987-08-20,Gender.MALE,['test@musmehl.de'],"
            + "['01112222222'],Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,TransportType.BUS,"
            + "2018-08-27 11:30:00,TransportType.PRIVATE,[<FoodRestriction.CELIAC_DISEASE: 5>],Supercooler Typ!!!,"
            + "42, 300, False, 10a, 10, ['Programmieren'], ['test2@musmehl.de'], {}, ['Uroma'], [50, 62], ['Geige'],"
            + " ['Kokain'], ['Schnupfen'], False, True, True, True)")


def test_counselorPrint():
    counselor = Counselor("Ferdinand", "Karl", date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                          "Karl-Liebknecht-Str.", 13, "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                          TransportType.BUS,
                          datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                          "Supercooler Typ!!!", 42, [8, 9])
    assert (
        counselor.__str__() == "Counselor(Ferdinand,Karl,1987-08-20,Gender.MALE,['test@musmehl.de'],['01112222222'],"
        + "Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,TransportType.BUS,2018-08-27 11:30:00,"
        + "TransportType.PRIVATE,[<FoodRestriction.CELIAC_DISEASE: 5>],Supercooler Typ!!!,42, [8, 9])")


def test_guestPrint():
    guest = Guest("Ferdinand", "Karl", date(1987, 8, 20), Gender.MALE, ["test@musmehl.de"], ["01112222222"],
                  "Karl-Liebknecht-Str.", 13, "86153", "Entenhausen", datetime(2018, 8, 19, 9, 30, 0),
                  TransportType.BUS,
                  datetime(2018, 8, 27, 11, 30, 0), TransportType.PRIVATE, [FoodRestriction.CELIAC_DISEASE],
                  "Supercooler Typ!!!", 42)
    assert (
        guest.__str__() == "Guest(Ferdinand,Karl,1987-08-20,Gender.MALE,['test@musmehl.de'],['01112222222'],"
        + "Karl-Liebknecht-Str.,13,86153,Entenhausen,2018-08-19 09:30:00,TransportType.BUS,2018-08-27 11:30:00,"
        + "TransportType.PRIVATE,[<FoodRestriction.CELIAC_DISEASE: 5>],Supercooler Typ!!!,42)")
