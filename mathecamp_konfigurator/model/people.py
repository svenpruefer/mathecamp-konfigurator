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

"""This file defines all people related types"""

__docformat__ = 'reStructuredText'

##########
# Import #
##########


from mathecamp_konfigurator.model.types import *
from mathecamp_konfigurator.model.enums import *
import ast

#########
# Human #
#########


class Human:
    """
    This class is a general human, i.e. either a particpant, a counselor or a guest.
    """

    def __init__(self, familyName="", givenName="", birthDate=date.min, gender=None, emailAddresses=None,
                 phoneNumbers=None, street="", streetNumber="", postalCode="", place="", arrivalTime=None,
                 arrivalType=None, departureTime=None, departureType=None, foodRestrictions=None, miscellaneous="",
                 room=None):
        """
        Basic constructor for general humans.
        :param familyName: Persons family name
        :param givenName: Persons given name
        :param birthDate: Persons birth date as a python3 Datetime.time value
        :param gender: Persons gender as an enum of type Gender
        :param emailAddresses: a list of email addresses for that person
        :param phoneNumbers: a list of phone numbers for that person as a string
        :param street: correspondance address street name
        :param streetNumber: correspondance address street number, can be a string
        :param postalCode: correspondance address postalCode as a string
        :param place: correspondance addess place
        :param arrivalTime: Persons arrival time at the Mathecamp as Datetime.time
        :param arrivalType: Persons arrival type at the Mathecamp as an enum of type TransportType
        :param departureTime: Persons departure time at the Mathecamp as Datetime.time
        :param departureType: Persons departure type at the Mathecamp as an enum of type TransportType
        :param foodRestrictions: Persons food restrictions as a list of enums of type FoodRestriction
        :param miscellaneous: a generic string
        :param room: Persons room in Violau as an ID of a Room
        """
        if phoneNumbers is None:
            phoneNumbers = []
        if foodRestrictions is None:
            foodRestrictions = []
        if emailAddresses is None:
            emailAddresses = []
        self.familyName = familyName
        self.givenName = givenName
        self.birthDate = birthDate
        self.gender = gender
        self.emailAddresses = emailAddresses
        self.phoneNumbers = phoneNumbers
        self.street = street
        self.streetNumber = streetNumber
        self.postalCode = postalCode
        self.place = place
        self.arrivalTime = arrivalTime
        self.arrivalType = arrivalType
        self.departureTime = departureTime
        self.departureType = departureType
        self.foodRestrictions = foodRestrictions
        self.miscellaneuos = miscellaneous
        self.room = room

    def getAddress(self):
        """
        This method returns the address of the person in the format "Street No, PLZ Place".
        :return address: String
        """
        return self.street + " " + self.streetNumber + ", " + str(self.postalCode) + " " + self.place

    def __str__(self):
        return ("Human({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(self.familyName, self.givenName,
                                                                                   self.birthDate, self.gender,
                                                                                   self.emailAddresses,
                                                                                   self.phoneNumbers,
                                                                                   self.street, self.streetNumber,
                                                                                   self.postalCode, self.place,
                                                                                   self.arrivalTime, self.arrivalType,
                                                                                   self.departureTime,
                                                                                   self.departureType,
                                                                                   self.foodRestrictions,
                                                                                   self.miscellaneuos, self.room))

    def toDict(self):
        """
        returns a dictionary of the human for saving in a csv file
        :return: a dictionary with keys familyName, givenName, birthDate, gender, emailAddresses, phoneNumbers, street,
        streetNumber, postalCode, place, arrivalTime, arrivalType, departureTime, departureType, foodRestrictions,
        miscellaneuos and room
        """
        return ({"familyName": self.familyName, "givenName": self.givenName, "birthDate": self.birthDate,
                 "gender": self.gender, "emailAddresses": self.emailAddresses, "phoneNumbers": self.phoneNumbers,
                 "street": self.street, "streetNumber": str(self.streetNumber), "postalCode": str(self.postalCode),
                 "place": self.place, "arrivalTime": self.arrivalTime, "arrivalType": self.arrivalType,
                 "departureTime": self.departureTime, "departureType": self.departureType,
                 "foodRestrictions": self.foodRestrictions, "miscellaneous": self.miscellaneuos, "room": self.room})

    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a human instance from a dictionary, inverse to 'toDict'
        :return: an instance of human
        """
        return (Human(dictionary["familyName"], dictionary["givenName"], dictionary["birthDate"], dictionary["gender"],
                      dictionary["emailAddresses"], dictionary["phoneNumbers"], dictionary["street"],
                      dictionary["streetNumber"],
                      dictionary["postalCode"], dictionary["place"], dictionary["arrivalTime"],
                      dictionary["arrivalType"],
                      dictionary["departureTime"], dictionary["departureType"], dictionary["foodRestrictions"],
                      dictionary["miscellaneous"], dictionary["room"]))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        """
        creates a participant instance from a dictionary, inverse to 'toDict'
        :return: an instance of a participant
        """
        return (Human(dictionary["familyName"],
                      dictionary["givenName"],
                      datetime.date(datetime.strptime(dictionary["birthDate"], "%Y-%m-%d")),
                      Gender.fromString(dictionary["gender"]),
                      ast.literal_eval(dictionary["emailAddresses"]),
                      ast.literal_eval(dictionary["phoneNumbers"]),
                      dictionary["street"],
                      dictionary["streetNumber"],
                      dictionary["postalCode"],
                      dictionary["place"],
                      datetime.strptime(dictionary["arrivalTime"], "%Y-%m-%d %H:%M:%S"),
                      TransportType.fromString(dictionary["arrivalType"]),
                      datetime.strptime(dictionary["departureTime"], "%Y-%m-%d %H:%M:%S"),
                      TransportType.fromString(dictionary["departureType"]),
                      FoodRestriction.parseListString(dictionary["foodRestrictions"]),
                      dictionary["miscellaneous"],
                      int(dictionary["room"])))


###############
# Participant #
###############

class Participant(Human):
    """
    This class represents a person that participates in the Mathecamp.
    """

    occupation = Occupation.PARTICIPANT

    def __init__(self, familyName="", givenName="", birthDate=date.min, campPrice=0,
                 moneyPayedAlready=0, circle=None, grade=0, topicWishes=None, emailAddresses=None,
                 emailAddressesParents=None, gender=None, phoneNumbers=None, phoneNumbersEmergency=None, room=None,
                 street="", streetNumber="", postalCode="", place="", arrivalTime=None, arrivalType=None,
                 departureTime=None, departureType=None, departureOtherPerson=None, friends=None, instrument=None,
                 medicalDrugs=None, foodRestrictions=None, illness="", rideSharing=None, swimmingPermission=None,
                 leavingPermission=None, sportsPermission=None, miscellaneous=""):
        """
        Basic constructor for participants
        :param familyName: Participants family name
        :param givenName: Participants given name
        :param birthDate: Participants birthDate as a python3 datetime.date value
        :param campPrice: Corresponding price for person as an integer, might be 0
        :param moneyPayedAlready: Already payed amounts of money as integers
        :param circle: the circle that the participant is assigned to, its value is of class MathCircle
        :param grade: the grade of the participante as an integer
        :param topicWishes: a list of strings containing the participants topic wishes
        :param emailAddresses: a list of stings of email addresses of the participant
        :param emailAddressesParents: a  list of stings of email addresses of the participants parents
        :param gender: the participants gender as an enum of type Gender
        :param phoneNumbers: a list of strings giving the participants phone numbers
        :param phoneNumbersEmergency: a dictionary of strings where the key is the emergency contact name and its value
        is the emergency contacts phone number
        :param room: the participants room as a class of type Room
        :param street: the participants street as a string
        :param streetNumber: the participants street number as a string
        :param postalCode: the participants postal code as a string
        :param place: the participants city as a string
        :param arrivalTime: the participants arrival time at the Mathecamp as a datetime.time
        :param arrivalType: the participants arrival type as an enum of type TransportType
        :param departureTime: the participants departure time at the Mathecamp as a datetime.time
        :param departureType: the participants departure type as an enum of type TransportType
        :param departureOtherPerson: a list of strings containing the names of the people allowed to pick up the
        participant
        :param friends: a list of integers corresponding to ids of friends of the participant
        :param instrument: a list of instruments as strings
        :param medicalDrugs: a list of medical drugs as strings
        :param foodRestrictions: a list of enums of type FoodRestriction of the participant
        :param illness: a list of strings of diseases or illnesses of the participant
        :param rideSharing: a Boolean whether the participant wants to share his contact data with other participants
        :param swimmingPermission: a Boolean whether the participant is allowed to swim
        :param leavingPermission: a Boolean whether the participant is allowed to leave the premises in a small group
        after telling counselors
        :param sportsPermission: a Boolean whether the participant is allowed to do sports
        :param miscellaneous: a string for miscellaneous information
        """

        if phoneNumbers is None:
            phoneNumbers = []
        if emailAddressesParents is None:
            emailAddressesParents = []
        if medicalDrugs is None:
            medicalDrugs = []
        if foodRestrictions is None:
            foodRestrictions = []
        if departureOtherPerson is None:
            departureOtherPerson = []
        if instrument is None:
            instrument = []
        if friends is None:
            friends = []
        if phoneNumbersEmergency is None:
            phoneNumbersEmergency = {}
        if emailAddresses is None:
            emailAddresses = []
        if topicWishes is None:
            topicWishes = []

        Human.__init__(self, familyName, givenName, birthDate, gender, emailAddresses,
                       phoneNumbers, street, streetNumber, postalCode, place, arrivalTime,
                       arrivalType, departureTime, departureType, foodRestrictions, miscellaneous, room)

        self.campPrice = campPrice
        self.moneyPayedAlready = moneyPayedAlready
        self.circle = circle
        self.grade = grade
        self.topicWishes = topicWishes
        self.emailAddressesParents = emailAddressesParents
        self.phoneNumbersEmergency = phoneNumbersEmergency
        self.departureOtherPerson = departureOtherPerson
        self.friends = friends
        self.instrument = instrument
        self.medicalDrugs = medicalDrugs
        self.illness = illness
        self.rideSharing = rideSharing
        self.swimmingPermission = swimmingPermission
        self.leavingPermission = leavingPermission
        self.sportsPermission = sportsPermission

    def __str__(self):
        humanPrint = Human.__str__(self)[5:]
        return ("Participant" + humanPrint[:len(
            humanPrint) - 1] + ", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})"
                .format(self.campPrice, self.moneyPayedAlready, self.circle, self.grade, self.topicWishes,
                        self.emailAddressesParents, self.phoneNumbersEmergency, self.departureOtherPerson, self.friends,
                        self.instrument, self.medicalDrugs, self.illness, self.rideSharing,
                        self.swimmingPermission, self.leavingPermission, self.sportsPermission))

    def toDict(self):
        """
        returns a dictionary of the participant for saving in a csv file
        :return: a dictionary with keys familyName, givenName, birthDate, gender, emailAddresses, phoneNumbers, street,
        streetNumber, postalCode, place, arrivalTime, arrivalType, departureTime, departureType, foodRestrictions,
        miscellaneuos, room, grade, circle, campPrice, moneyPayedAlready, topicWishes, emailAddressesParents,
        phoneNumbersEmergency, departureOtherPerson, friends, instrument, medicalDrugs, foodRestrictions, illness,
        rideSharing, swimmingPermission, leavingPermission, sportsPermission
        """
        newDict = Human.toDict(self)
        for (k, v) in {"grade": self.grade, "circle": self.circle, "campPrice": self.campPrice,
                       "moneyPayedAlready": self.moneyPayedAlready, "topicWishes": self.topicWishes,
                       "emailAddressesParents": self.emailAddressesParents,
                       "phoneNumbersEmergency": self.phoneNumbersEmergency,
                       "departureOtherPerson": self.departureOtherPerson,
                       "friends": self.friends, "instrument": self.instrument, "medicalDrugs": self.medicalDrugs,
                       "illness": self.illness, "rideSharing": self.rideSharing,
                       "swimmingPermission": self.swimmingPermission, "leavingPermission": self.leavingPermission,
                       "sportsPermission": self.sportsPermission}.items():
            newDict[k] = v
        return newDict

    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a participant instance from a dictionary, inverse to 'toDict'
        :return: an instance of a participant
        """
        return (Participant(dictionary["familyName"], dictionary["givenName"], dictionary["birthDate"],
                            dictionary["campPrice"], dictionary["moneyPayedAlready"], dictionary["circle"],
                            dictionary["grade"], dictionary["topicWishes"], dictionary["emailAddresses"],
                            dictionary["emailAddressesParents"], dictionary["gender"], dictionary["phoneNumbers"],
                            dictionary["phoneNumbersEmergency"], dictionary["room"], dictionary["street"],
                            dictionary["streetNumber"], dictionary["postalCode"], dictionary["place"],
                            dictionary["arrivalTime"],
                            dictionary["arrivalType"], dictionary["departureTime"], dictionary["departureType"],
                            dictionary["departureOtherPerson"], dictionary["friends"], dictionary["instrument"],
                            dictionary["medicalDrugs"], dictionary["foodRestrictions"], dictionary["illness"],
                            dictionary["rideSharing"], dictionary["swimmingPermission"],
                            dictionary["leavingPermission"],
                            dictionary["sportsPermission"], dictionary["miscellaneous"]))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        """
        creates a participant instance from a dictionary, inverse to 'toDict'
        :return: an instance of a participant
        """
        return (Participant(dictionary["familyName"],
                            dictionary["givenName"],
                            datetime.date(datetime.strptime(dictionary["birthDate"], "%Y-%m-%d")),
                            int(dictionary["campPrice"]),
                            ast.literal_eval(dictionary["moneyPayedAlready"]),
                            dictionary["circle"],
                            int(dictionary["grade"]),
                            ast.literal_eval(dictionary["topicWishes"]),
                            ast.literal_eval(dictionary["emailAddresses"]),
                            ast.literal_eval(dictionary["emailAddressesParents"]),
                            Gender.fromString(dictionary["gender"]),
                            ast.literal_eval(dictionary["phoneNumbers"]),
                            ast.literal_eval(dictionary["phoneNumbersEmergency"]),
                            int(dictionary["room"]),
                            dictionary["street"],
                            dictionary["streetNumber"],
                            dictionary["postalCode"],
                            dictionary["place"],
                            datetime.strptime(dictionary["arrivalTime"], "%Y-%m-%d %H:%M:%S"),
                            TransportType.fromString(dictionary["arrivalType"]),
                            datetime.strptime(dictionary["departureTime"], "%Y-%m-%d %H:%M:%S"),
                            TransportType.fromString(dictionary["departureType"]),
                            ast.literal_eval(dictionary["departureOtherPerson"]),
                            ast.literal_eval(dictionary["friends"]),
                            ast.literal_eval(dictionary["instrument"]),
                            ast.literal_eval(dictionary["medicalDrugs"]),
                            FoodRestriction.parseListString(dictionary["foodRestrictions"]),
                            ast.literal_eval(dictionary["illness"]),
                            ast.literal_eval(dictionary["rideSharing"]),
                            ast.literal_eval(dictionary["swimmingPermission"]),
                            ast.literal_eval(dictionary["leavingPermission"]),
                            ast.literal_eval(dictionary["sportsPermission"]),
                            dictionary["miscellaneous"]))


#############
# Counselor #
#############

class Counselor(Human):
    """
    This class represents a counselor in the Mathecamp.
    """

    occupation = Occupation.COUNSELOR

    def __init__(self, familyName="", givenName="", birthDate=date.min, gender=None, emailAddresses=None,
                 phoneNumbers=None, street="", streetNumber="", postalCode="", place="",
                 arrivalTime=None, arrivalType=None, departureTime=None, departureType=None, foodRestrictions=None,
                 miscellaneous="", room=None, preferredGrades=None):
        """
        Basic constructor for counselors
        :param familyName: Participants family name
        :param givenName: Participants given name
        :param birthDate: Participants birthDate as a python3 datetime.date value
        :param emailAddresses: a list of stings of email addresses of the participant
        :param gender: the participants gender as an enum of type Gender
        :param phoneNumbers: a list of strings giving the participants phone numbers
        :param street: the participants street as a string
        :param streetNumber: the participants street number as a string
        :param postalCode: the participants postal code as a string
        :param place: the participants city as a string
        :param arrivalTime: the participants arrival time at the Mathecamp as a datetime.time
        :param arrivalType: the participants arrival type as an enum of type TransportType
        :param departureTime: the participants departure time at the Mathecamp as a datetime.time
        :param departureType: the participants departure type as an enum of type TransportType
        :param foodRestrictions: a list of enums of type FoodRestriction of the participant
        :param miscellaneous: a string for miscellaneous information
        :param room: the participants room as the id (i.e. an integer) of the corresponding room
        :param preferredGrades: the preferred grades of the counselor as a list of integers
        """
        if emailAddresses is None:
            emailAddresses = []
        if foodRestrictions is None:
            foodRestrictions = []
        if preferredGrades is None:
            preferredGrades = []
        if phoneNumbers is None:
            phoneNumbers = []
        Human.__init__(self, familyName, givenName, birthDate, gender, emailAddresses,
                       phoneNumbers, street, streetNumber, postalCode, place, arrivalTime,
                       arrivalType, departureTime, departureType, foodRestrictions, miscellaneous, room)
        self.preferredGrades = preferredGrades

    def __str__(self):
        humanPrint = Human.__str__(self)[5:]
        return "Counselor" + humanPrint[:len(humanPrint) - 1] + ", {})".format(self.preferredGrades)

    def toDict(self):
        """
        returns a dictionary of the counselor for saving in a csv file
        :return: a dictionary with keys familyName, givenName, birthDate, gender, emailAddresses, phoneNumbers, street,
        streetNumber, postalCode, place, arrivalTime, arrivalType, departureTime, departureType, foodRestrictions,
        miscellaneuos, room and preferredGrades
        """
        newDict = Human.toDict(self)
        newDict["preferredGrades"] = self.preferredGrades
        return newDict

    @classmethod
    def fromDict(cls, dictionary):
        """
        creates a counselor instance from a dictionary, inverse to 'toDict'
        :return: an instance of a counselor
        """
        return (Counselor(dictionary["familyName"], dictionary["givenName"], dictionary["birthDate"],
                          dictionary["gender"], dictionary["emailAddresses"],
                          dictionary["phoneNumbers"], dictionary["street"],
                          dictionary["streetNumber"],
                          dictionary["postalCode"], dictionary["place"], dictionary["arrivalTime"],
                          dictionary["arrivalType"],
                          dictionary["departureTime"], dictionary["departureType"], dictionary["foodRestrictions"],
                          dictionary["miscellaneous"], dictionary["room"], dictionary["preferredGrades"]))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        """
        creates a counselor instance from a dictionary, inverse to 'toDict'

        :return: an instance of a counselor
        """
        return (Counselor(dictionary["familyName"],
                          dictionary["givenName"],
                          datetime.date(datetime.strptime(dictionary["birthDate"], "%Y-%m-%d")),
                          Gender.fromString(dictionary["gender"]),
                          ast.literal_eval(dictionary["emailAddresses"]),
                          ast.literal_eval(dictionary["phoneNumbers"]),
                          dictionary["street"],
                          dictionary["streetNumber"],
                          dictionary["postalCode"],
                          dictionary["place"],
                          datetime.strptime(dictionary["arrivalTime"], "%Y-%m-%d %H:%M:%S"),
                          TransportType.fromString(dictionary["arrivalType"]),
                          datetime.strptime(dictionary["departureTime"], "%Y-%m-%d %H:%M:%S"),
                          TransportType.fromString(dictionary["departureType"]),
                          FoodRestriction.parseListString(dictionary["foodRestrictions"]),
                          dictionary["miscellaneous"],
                          int(dictionary["room"]),
                          ast.literal_eval(dictionary["preferredGrades"])))


#########
# Guest #
#########

class Guest(Human):
    """
    This class represents a guest at the Mathecamp who may or may not stay there for a night.
    """

    occupation = Occupation.GUEST

    def __init__(self, familyName="", givenName="", birthDate=date.min, gender=None, emailAddresses=None,
                 phoneNumbers=None, street="", streetNumber="", postalCode="", place="",
                 arrivalTime=None, arrivalType=None, departureTime=None, departureType=None, foodRestrictions=None,
                 miscellaneous="", room=None):
        """
        Basic constructor for guests
        :param familyName: Guests family name
        :param givenName: Guests given name
        :param birthDate: Guests birthDate as a python3 datetime.date value
        :param emailAddresses: a list of stings of email addresses of the Guest
        :param gender: the Guests gender as an enum of type Gender
        :param phoneNumbers: a list of strings giving the Guests phone numbers
        :param street: the Guests street as a string
        :param streetNumber: the Guests street number as a string
        :param postalCode: the Guests postal code as a string
        :param place: the Guests city as a string
        :param arrivalTime: the Guests arrival time at the Mathecamp as a datetime.time
        :param arrivalType: the Guests arrival type as an enum of type TransportType
        :param departureTime: the Guests departure time at the Mathecamp as a datetime.time
        :param departureType: the Guests departure type as an enum of type TransportType
        :param foodRestrictions: a list of enums of type FoodRestriction of the Guest
        :param miscellaneous: a string for miscellaneous information
        :param room: the Guests room as the id (i.e. an integer) of the corresponding room
        """
        if foodRestrictions is None:
            foodRestrictions = []
        if emailAddresses is None:
            emailAddresses = []
        if phoneNumbers is None:
            phoneNumbers = []
        Human.__init__(self, familyName, givenName, birthDate, gender, emailAddresses,
                       phoneNumbers, street, streetNumber, postalCode, place, arrivalTime,
                       arrivalType, departureTime, departureType, foodRestrictions, miscellaneous, room)

    def __str__(self):
        guestString = Human.__str__(self)[5:]
        return "Guest" + guestString

    def toDict(self):
        """
        maps guest instance to dictionary in order to save it to a csv file
        :return: a dictionary with keys
        """
        return Human.toDict(self)

    @classmethod
    def fromDict(cls, dictionary):
        """
        parses a dictionary and yields a guest instance, inverse to toDict
        :param dictionary: the dictionary to parse
        :return: an instance of a guest
        """
        return (Guest(dictionary["familyName"], dictionary["givenName"], dictionary["birthDate"], dictionary["gender"],
                      dictionary["emailAddresses"], dictionary["phoneNumbers"], dictionary["street"],
                      dictionary["streetNumber"],
                      dictionary["postalCode"], dictionary["place"], dictionary["arrivalTime"],
                      dictionary["arrivalType"],
                      dictionary["departureTime"], dictionary["departureType"], dictionary["foodRestrictions"],
                      dictionary["miscellaneous"], dictionary["room"]))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        """
        creates a guest instance from a dictionary, inverse to 'toDict'

        :return: an instance of a guest
        """
        return (Guest(dictionary["familyName"],
                      dictionary["givenName"],
                      datetime.date(datetime.strptime(dictionary["birthDate"], "%Y-%m-%d")),
                      Gender.fromString(dictionary["gender"]),
                      ast.literal_eval(dictionary["emailAddresses"]),
                      ast.literal_eval(dictionary["phoneNumbers"]),
                      dictionary["street"],
                      dictionary["streetNumber"],
                      dictionary["postalCode"],
                      dictionary["place"],
                      datetime.strptime(dictionary["arrivalTime"], "%Y-%m-%d %H:%M:%S"),
                      TransportType.fromString(dictionary["arrivalType"]),
                      datetime.strptime(dictionary["departureTime"], "%Y-%m-%d %H:%M:%S"),
                      TransportType.fromString(dictionary["departureType"]),
                      FoodRestriction.parseListString(dictionary["foodRestrictions"]),
                      dictionary["miscellaneous"],
                      int(dictionary["room"])))
