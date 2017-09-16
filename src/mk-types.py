# This file defines most types used in mathecamp-konfigurator.

##########
# Import #
##########

from datetime import *
from enum import Enum

#########
# Enums #
#########

class Gender(Enum):
    FEMALE = 1
    MALE = 2

class Occupation(Enum):
    COUNSELOR = 1
    PARTICIPANT = 2
    GUEST = 3

class FoodRestriction(Enum):
    VEGETARIAN = 1
    VEGAN = 2
    NO_MEAT = 3
    NO_FISH = 4
    CELIAC_DISEASE = 5
    NO_NUTS = 6

class TransportType(Enum):
    BUS = 1
    PRIVATE = 2
    SELF = 3
    
##########
# People #
##########

class Person:
    """
    This class represents a person that might participate in the Matecamp. In particular this includes participants as well as camp counselors.
    """
    
    def __init__(self, id = 0, family_name = "", given_name = "", birthDate = date.min, campPrice = 0,
                 moneyPayedAlready = 0, circle = None, grade = 0, topicWishes = "", emailAddresses = [],
                 emailAdressesParents = [], gender = None, occupation = None, phoneNumbers = [],
                 phoneNumbersEmergency = {}, street = "", streetNumber = "", postalCode = 0, place = "", arrivalTime
                 = None, arrivalType = None, departureTime = None, departureType = None, departureOtherPerson = [],
                 friends = [], instrument = [], medicalDrugs = [], foodRestrictions = [], illness = "",
                 rideSharing = None, swimmingPermission = None, leavingPermission = None, sportsPermission = None,
                 miscellaneous = ""):
        """
        Basic constructor setting everything to default values. In particular many values are None!
        """
        self.id = id
        self.family_name = family_name
        self.given_name = given_name
        self.birthDate = birthDate
        self.campPrice = campPrice
        self.moneyPayedAlready = moneyPayedAlready
        self.circle = circle
        self.grade = grade
        self.topicWishes = topicWishes
        self.emailAddresses = emailAddresses
        self.emailAddressesParents = emailAdressesParents # This is a dictionary of strings (the name) and phone numbers.
        self.gender = gender
        self.occupation = occupation
        self.phoneNumbers = phoneNumbers
        self.phoneNumbersEmergency = phoneNumbersEmergency
        self.street = street
        self.streetNumber = streetNumber
        self.postalCode = postalCode
        self.place = place
        self.arrivalTime = arrivalTime
        self.arrivalType = arrivalType
        self.departureTime = departureTime
        self.departureType = departureType
        self.departureOtherPerson = departureOtherPerson
        self.friends = friends
        self.instrument = instrument
        self.medicalDrugs = medicalDrugs
        self.foodRestrictions = foodRestrictions
        self.illness = illness
        self.rideSharing = rideSharing
        self.swimmingPermission = swimmingPermission
        self.leavingPermission = leavingPermission
        self.sportsPermission = sportsPermission
        self.miscellaneous = miscellaneous
        
    def getAddress(self):
        """
        This method returns the addressof the person in the format "Street No, PLZ Place".
        :return address: String
        """
        return self.street + " " + self.streetNumber + ", " + str(self.postalCode) + " " + self.place
        
        
##########
# Circle #
##########

class MathCircle:
    """
    This class represents a math circle in the Mathecamp.
    """
    
    def __init__(self):
        self.grade = 0
        self.members = []
        self.room = ""

############
# Activity #
############

class Activity:
    """
    This class represents an activity such as afternoon activities or bigger projects that need to be organized or
    planned.
    """
    
    def __init__(self):
        self.name = ""
        self.timeAndPlace = []
        self.participants = []
        self.organizers = []
        self.costs = 0
    
############
# Schedule #
############

class Schedule:
    """
    This class represents an instance of a schedule, i.e. a plan who is doing what at which thime at which place. For
    this purpose it primarily consists of a list of activities.
    """

############
# Expenses #
############

class Expense:
    """
    This class represents an expense for something.
    """
    
    def __init__(self):
        self.amount = 0
        self.name = ""
        self.usage = []
        self.payedAlready = False
        
####################
# Space-Time Slots #
####################

class SpaceTimeSlot:
    """
    This class represents a time slot with a beginning and an end as well as a place. Either can be empty. A time
    slot is represented by a 2-tuple of datetimes and a place is represented by a string.
    """
    
    def __init__(self):
        self.beginning = datetime.min
        self.end = datetime.max
        self.timeSlot = [self.beginning, self.end]
        self.romm = ""