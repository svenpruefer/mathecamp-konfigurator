# This file defines the main class mathecamp

###########
# Imports #
###########
from datetime import *
from src.people import *


#############
# Mathecamp #
#############


class mathecamp():
    """
    This is the main class representing all the data that a mathecamp comprises at any time of the planning
    """

    # <editor-fold desc="Constructor">
    def __init__(self, startDate=datetime.min, endDate=datetime.max, nextHumanId=1, nextRoomId=1, nextActivityId=1,
                 nextMathCircleId=1, nextExpenseId=1, rooms=None, activities=None, mathCircles=None, expenses=None,
                 participants=None, counselors=None, guests=None):
        """
        The main constructor of a mathecamp instance
        :param startDate: the start date time of the camp
        :param endDate: the end date time of the camp
        :param nextHumanId: the next used Id for a human
        :param nextRoomId: the next used Id for a room
        :param nextActivityId: the next used Id for an activity
        :param nextMathCircleId: the next used Id for a math circle
        :param nextExpenseId: the next used Id for an expense
        :param rooms: rooms in the camp as a dictionary
        :param activities: activities in the camp as a dictionary
        :param mathCircles: math circles in the camp as a dictionary
        :param expenses: expenses in the camp as a dictionary
        :param participants: participants in the camp as a dictionary
        :param counselors: counselors in the camp as a dictionary
        :param guests: guests in the camp as a dictionary
        """

        if guests is None:
            guests = {}
        if counselors is None:
            counselors = {}
        if participants is None:
            participants = {}
        if expenses is None:
            expenses = {}
        if mathCircles is None:
            mathCircles = {}
        if activities is None:
            activities = {}
        if rooms is None:
            rooms = {}

        self.dates = {"start": startDate, "end": endDate}
        self.nextIds = {"Human": nextHumanId, "Room": nextRoomId, "Activity": nextActivityId,
                        "MathCircle": nextMathCircleId, "Expense": nextExpenseId}
        self.rooms = rooms
        self.activities = activities
        self.mathCircles = mathCircles
        self.expenses = expenses
        self.participants = participants
        self.counselors = counselors
        self.guests = guests

    # </editor-fold>

    # <editor-fold desc="Serialization">
    def serializeToDictionaries(self):
        """
        Serializes the state of the mathecamp such that it can be easily written to CSV files.
        :return: a dictionary containing the following data:
        generalData : a list of dictionaries each having an entry "parameter" and an entry "value" which represent
        the general settings and data of the mathecamp
        rooms: a dictionary containing

        """

    # </editor-fold>

    # <editor-fold desc="Helper methods">
    def isDuringCamp(self, time: datetime):
        """
        returns a Boolean stating whether the given date time is during the Mathecamp or not
        :param time: datetime to check
        :return: a Boolean
        """
        if (self.dates["start"] <= time and time <= self.dates["end"]):
            return True
        else:
            return False

    # </editor-fold>

    # <editor-fold desc="Add data methods">

    def addRoom(self, room):
        """
        method for adding a room to the project
        :param room: a room of type Room
        :return:
        """

        self.rooms.append((self.nextIds["Room"], room))
        self.nextIds["Room"] += 1

    def addActivity(self, activity):
        """
        method for adding an activity to the project
        :param activity: an activity of type Activity
        :return:
        """

        self.activities.append((self.nextIds["Activity"], activity))
        self.nextIds["Activity"] += 1

    def addMathCircle(self, mathCircle):
        """
        method for adding a math circle to the project
        :param mathCircle: a mathcircle of type MathCircle
        :return:
        """

        self.mathCircles.append((self.nextIds["MathCircle"], mathCircle))
        self.nextIds["MathCircle"] += 1

    def addHuman(self, human):
        """
        method for adding an arbitrary human
        :param human: the person to be added of type either Participant, Counselor or Guest
        :return:
        """

        nextId = self.nextIds["Human"]
        if isinstance(human, Participant):
            self.participants.append((nextId, human))
        elif isinstance(human, Counselor):
            self.counselors.append((nextId, human))
        elif isinstance(human, Guest):
            self.guests.append((nextId, human))
        self.nextIds["Human"] += 1

    def addExpense(self, expense):
        """
        method for adding an expense
        :param expense: the expense to add of type Expense
        :return:
        """

        self.expenses.append((self.nextIds["Expense"], expense))
        self.nextIds["Expense"] += 1
        # </editor-fold>
