# This file defines most types which are not people used in mathecamp-konfigurator.

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
    NO_EGGS = 7
    NO_CARROTS = 8

class TransportType(Enum):
    BUS = 1
    PRIVATE = 2
    SELF = 3

class Equipment(Enum):
    PIANO = 1
    BLACKBOARD = 2
    WHITEBOARD = 3
    CANVAS = 4
        
##########
# Circle #
##########

class MathCircle:
    """
    This class represents a math circle (i.e. a group of students participating in the morning math circles together
    """
    
    def __init__(self, grade=0, members=[], room=None, topics=[]):
        """
        This is the main constructor of a math circle
        :param grade: the grade of the math circle as an integer
        :param members: the members of the math circle as an integer of IDs (i.e. integers) of the participants
        :param room: the room where the math circle takes place as an enum of type Room
        :param topics: a list of strings corresponding to the covered topics
        """
        self.grade = grade
        self.members = members
        self.room = room
        self.topics = topics

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
        self.room = ""

#########
# Rooms #
#########

class Room:
    """
    This class represents a general room at Violau
    """

    def __init__(self, id, name):
        """
        The main constructor of a room
        :param id: the id of the room as an integer
        :param name: The name of the room as a string
        """
        self.id = id
        self.name = name


class GeneralRoom(Room):
    """
    This class represents a general room for everybodys usage
    """

    def __init__(self, id, name, equipment):
        """
        The main constructor of a general room
        :param name: the name of the room as a string
        :param equipment: the equipment available in this room as an enum of type Equipment
        """
        Room.__init__(self, id, name)
        self.equipment = equipment

class PrivateRoom(Room):
    """
    This class represents a private room for sleeping
    """

    def __init__(self, id, name="", capacity=0, inhabitants=[], bedtime=date.max):
        """
        The main constructor of a private room
        :param name: the name of the room as a string
        :param equipment: the equipment available in this room as an enum of type Equipment
        """
        Room.__init__(self, id, name)
        self.capacity = capacity
        self.inhabitants = inhabitants
        self.bedtime = bedtime