# This file defines all people related types

##########
# Import #
##########

#from datetime import *
from src.mktypes import *

#########
# Human #
#########

class Human:
    """
    This class is a general human, i.e. either a particpant, a counselor or a guest.
    """

    def __init__(self, id=0, family_name="", given_name="", birthDate=date.min, gender=None, emailAddresses=[],
                 phoneNumbers=[], street="", streetNumber="", postalCode="", place="", arrivalTime=None,
                 arrivalType=None, departureTime=None, departureType=None, foodRestrictions=[], miscellaneous="",
                 room=None):
        """
        Basic constructor for general humans.
        :param id: Unique id per Person in the whole Mathecamp
        :param family_name: Persons family name
        :param given_name: Persons given name
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
        :param room: Persons room in Violau as a class of type Room
        """
        self.id = id
        self.family_name = family_name
        self.given_name = given_name
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

###############
# Participant #
###############

class Participant(Human):
    """
    This class represents a person that participates in the Mathecamp.
    """

    occupation = Occupation.PARTICIPANT

    def __init__(self, id=0, family_name="", given_name="", birthDate=date.min, campPrice=0,
                 moneyPayedAlready=0, circle=None, grade=0, topicWishes=[], emailAddresses=[],
                 emailAdressesParents=[], gender=None, phoneNumbers=[], phoneNumbersEmergency={},  room=None,
                 street="", streetNumber="", postalCode="", place="", arrivalTime=None, arrivalType=None,
                 departureTime=None, departureType=None, departureOtherPerson=[], friends=[], instrument=[],
                 medicalDrugs=[], foodRestrictions=[], illness="", rideSharing=None, swimmingPermission=None,
                 leavingPermission=None, sportsPermission=None, miscellaneous=""):
        """
        Basic constructor for participants
        :param id: Unique id per Person in the whole mathecamp
        :param family_name: Participants family name
        :param given_name: Participants given name
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

        Human.__init__(self, id, family_name, given_name, birthDate, gender, emailAddresses,
                 phoneNumbers, street, streetNumber, postalCode, place, arrivalTime,
                 arrivalType, departureTime, departureType, foodRestrictions, miscellaneous, room)
        self.campPrice = campPrice
        self.moneyPayedAlready = moneyPayedAlready
        self.circle = circle
        self.grade = grade
        self.topicWishes = topicWishes
        self.emailAddressesParents = emailAdressesParents
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

#############
# Counselor #
#############

class counselor(Human):
    """
    This class represents a counselor in the Mathecamp.
    """

    occupation = Occupation.COUNSELOR

    def __init__(self, id=0, family_name="", given_name="", birthDate=date.min, emailAddresses=[], gender=None,
                 phoneNumbers=[], street="", streetNumber="", postalCode="", place="",
                 arrivalTime=None, arrivalType=None, departureTime=None, departureType=None, foodRestrictions=[],
                 miscellaneous="", room=None, preferredGrades=[]):
        """
        Basic constructor for counselors
        :param id: Unique id per Person in the whole mathecamp
        :param family_name: Participants family name
        :param given_name: Participants given name
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

        Human.__init__(self, id, family_name, given_name, birthDate, gender, emailAddresses,
                 phoneNumbers, street, streetNumber, postalCode, place, arrivalTime,
                 arrivalType, departureTime, departureType, foodRestrictions, miscellaneous, room)
        self.preferredGrades= preferredGrades
