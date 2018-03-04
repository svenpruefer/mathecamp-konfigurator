#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file defines the main class mathecamp

__docformat__ = 'reStructuredText'

###########
# Imports #
###########
from datetime import *
from mathecamp_konfigurator.people import *
from sortedcontainers import SortedDict, SortedList
from dateutil.parser import parse


#############
# Mathecamp #
#############


class Mathecamp():
    """
    This is the main class representing all the data that a mathecamp comprises at any time of the planning
    """

    # <editor-fold desc="Constructor">
    def __init__(self, startDate=datetime.min, endDate=datetime.max, nextHumanId=1, nextRoomId=1,
                 nextActivityId=1,
                 nextMathCircleId=1, nextExpenseId=1, nextSpaceTimeSlotId=1, generalRooms=None,
                 privateRooms=None,
                 activities=None, spacetimeSlots=None,
                 mathCircles=None, expenses=None,
                 participants=None, counselors=None, guests=None, schedule=None):
        """
        The main constructor of a mathecamp instance
        :param startDate: the start date time of the camp
        :param endDate: the end date time of the camp
        :param nextHumanId: the next used Id for a human
        :param nextRoomId: the next used Id for a room
        :param nextActivityId: the next used Id for an activity
        :param nextMathCircleId: the next used Id for a math circle
        :param nextExpenseId: the next used Id for an expense
        :param nextSpaceTimeSlotId: the next used Id for a space-time slot
        :param generalRooms: general rooms in the camp as a dictionary
        :param privateRooms: private rooms in the camp as a dictionary
        :param activities: activities in the camp as a dictionary
        :param spacetimeSlots: spacetime slots in the camp as a dictionary
        :param mathCircles: math circles in the camp as a dictionary
        :param expenses: expenses in the camp as a dictionary
        :param participants: participants in the camp as a dictionary
        :param counselors: counselors in the camp as a dictionary
        :param guests: guests in the camp as a dictionary
        """

        if guests is None:
            guests = SortedDict({})
        if counselors is None:
            counselors = SortedDict({})
        if participants is None:
            participants = SortedDict({})
        if expenses is None:
            expenses = SortedDict({})
        if mathCircles is None:
            mathCircles = SortedDict({})
        if activities is None:
            activities = SortedDict({})
        if spacetimeSlots is None:
            spacetimeSlots = SortedDict({})
        if generalRooms is None:
            generalRooms = SortedDict({})
        if privateRooms is None:
            privateRooms = SortedDict({})
        if schedule is None:
            schedule = Schedule(SortedList([]))

        self.dates = SortedDict({"start": startDate, "end": endDate})
        self.nextIds = SortedDict({"Human": nextHumanId, "Room": nextRoomId, "Activity": nextActivityId,
                                   "MathCircle": nextMathCircleId, "Expense": nextExpenseId,
                                   "SpaceTimeSlot": nextSpaceTimeSlotId})
        self.generalRooms = SortedDict(generalRooms)
        self.privateRooms = SortedDict(privateRooms)
        self.activities = SortedDict(activities)
        self.mathCircles = SortedDict(mathCircles)
        self.expenses = SortedDict(expenses)
        self.participants = SortedDict(participants)
        self.counselors = SortedDict(counselors)
        self.guests = SortedDict(guests)
        self.schedule = schedule
        self.spacetimeSlots = SortedDict(spacetimeSlots)

    # </editor-fold>

    # <editor-fold desc="Serialization">
    def toDict(self):
        """
        Serializes the state of the mathecamp such that it can be easily written to CSV files.
        :return: a dictionary containing the following data:
        generalData : a list of dictionaries each having an entry "parameter" and an entry "value" which represent
        the general settings and data of the mathecamp
        privateRooms, generalRooms, activities, mathCircles, expenses, participants, counselors, guests and schedule: dictionaries with IDs
        as keys and dictionaries with their respective data as values
        """

        generalDataDict = SortedDict({})
        privateRoomDict = SortedDict({})
        generalRoomDict = SortedDict({})
        activityDict = SortedDict({})
        mathCircleDict = SortedDict({})
        expenseDict = SortedDict({})
        participantDict = SortedDict({})
        counselorDict = SortedDict({})
        guestDict = SortedDict({})
        spacetimeSlotDict = SortedDict({})

        generalDataDict["startDate"] = self.dates["start"]
        generalDataDict["endDate"] = self.dates["end"]
        generalDataDict["nextHumanId"] = self.nextIds["Human"]
        generalDataDict["nextActivityId"] = self.nextIds["Activity"]
        generalDataDict["nextRoomId"] = self.nextIds["Room"]
        generalDataDict["nextExpenseId"] = self.nextIds["Expense"]
        generalDataDict["nextSpaceTimeSlotId"] = self.nextIds["SpaceTimeSlot"]
        generalDataDict["nextMathCircleId"] = self.nextIds["MathCircle"]

        for (k, v) in self.generalRooms.items():
            generalRoomDict[k] = SortedDict(v.toDict())

        for (k, v) in self.privateRooms.items():
            privateRoomDict[k] = SortedDict(v.toDict())

        for (k, v) in self.activities.items():
            activityDict[k] = SortedDict(v.toDict())

        for (k, v) in self.mathCircles.items():
            mathCircleDict[k] = SortedDict(v.toDict())

        for (k, v) in self.expenses.items():
            expenseDict[k] = SortedDict(v.toDict())

        for (k, v) in self.participants.items():
            participantDict[k] = SortedDict(v.toDict())

        for (k, v) in self.counselors.items():
            counselorDict[k] = SortedDict(v.toDict())

        for (k, v) in self.guests.items():
            guestDict[k] = SortedDict(v.toDict())

        for (k, v) in self.spacetimeSlots.items():
            spacetimeSlotDict[k] = SortedDict(v.toDict())

        return (SortedDict({
            "generalData": generalDataDict,
            "generalRooms": generalRoomDict,
            "privateRooms": privateRoomDict,
            "activities": activityDict,
            "mathCircles": mathCircleDict,
            "expenses": expenseDict,
            "participants": participantDict,
            "counselors": counselorDict,
            "guests": guestDict,
            "spacetimeSlots": spacetimeSlotDict,
            "schedule": self.schedule.toDict()
        }))

    @classmethod
    def fromDict(cls, dictionary):
        """
        opposite of 'toDict", deserializes a dictionary of dictionaries to a new instance of mathecamp
        :param dictionary: data to deserialize
        :return: a new instance of a mathecamp
        """

        return (Mathecamp(
            dictionary["generalData"]["startDate"],
            dictionary["generalData"]["endDate"],
            dictionary["generalData"]["nextHumanId"],
            dictionary["generalData"]["nextRoomId"],
            dictionary["generalData"]["nextActivityId"],
            dictionary["generalData"]["nextMathCircleId"],
            dictionary["generalData"]["nextExpenseId"],
            dictionary["generalData"]["nextSpaceTimeSlotId"],
            {k: GeneralRoom.fromDict(v) for (k, v) in dictionary["generalRooms"].items()},
            {k: PrivateRoom.fromDict(v) for (k, v) in dictionary["privateRooms"].items()},
            {k: Activity.fromDict(v) for (k, v) in dictionary["activities"].items()},
            {k: SpaceTimeSlot.fromDict(v) for (k, v) in dictionary["spacetimeSlots"].items()},
            {k: MathCircle.fromDict(v) for (k, v) in dictionary["mathCircles"].items()},
            {k: Expense.fromDict(v) for (k, v) in dictionary["expenses"].items()},
            {k: Participant.fromDict(v) for (k, v) in dictionary["participants"].items()},
            {k: Counselor.fromDict(v) for (k, v) in dictionary["counselors"].items()},
            {k: Guest.fromDict(v) for (k, v) in dictionary["guests"].items()},
            Schedule.fromDict(dictionary["schedule"])
        ))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        """
        creates a Mathecmap instance from a dictionary of strings as is created by deserializing csv tables

        :param dictionary: the dictionary to parse
        :return: a new instance of a Mathecamp
        """

        return (Mathecamp(
            datetime.strptime(dictionary["generalData"]["startDate"], "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(dictionary["generalData"]["endDate"], "%Y-%m-%d %H:%M:%S"),
            int(dictionary["generalData"]["nextHumanId"]),
            int(dictionary["generalData"]["nextRoomId"]),
            int(dictionary["generalData"]["nextActivityId"]),
            int(dictionary["generalData"]["nextMathCircleId"]),
            int(dictionary["generalData"]["nextExpenseId"]),
            int(dictionary["generalData"]["nextSpaceTimeSlotId"]),
            {k: GeneralRoom.fromDictOfStrings(v) for (k, v) in dictionary["generalRooms"].items()},
            {k: PrivateRoom.fromDictOfStrings(v) for (k, v) in dictionary["privateRooms"].items()},
            {k: Activity.fromDictOfStrings(v) for (k, v) in dictionary["activities"].items()},
            {k: SpaceTimeSlot.fromDictOfStrings(v) for (k, v) in dictionary["spacetimeSlots"].items()},
            {k: MathCircle.fromDictOfStrings(v) for (k, v) in dictionary["mathCircles"].items()},
            {k: Expense.fromDictOfStrings(v) for (k, v) in dictionary["expenses"].items()},
            {k: Participant.fromDictOfStrings(v) for (k, v) in dictionary["participants"].items()},
            {k: Counselor.fromDictOfStrings(v) for (k, v) in dictionary["counselors"].items()},
            {k: Guest.fromDictOfStrings(v) for (k, v) in dictionary["guests"].items()},
            Schedule.fromDictOfStrings(dictionary["schedule"])))

    # </editor-fold>

    # <editor-fold desc="Helper methods">

    def __str__(self):
        return (
            "Mathecamp(" + self.dates["start"].__str__() + ", " +
            self.dates["end"].__str__() + ", " +
            self.nextIds["Human"].__str__() + ", " +
            self.nextIds["Room"].__str__() + ", " +
            self.nextIds["Activity"].__str__() + ", " +
            self.nextIds["MathCircle"].__str__() + ", " +
            self.nextIds["Expense"].__str__() + ", " +
            self.nextIds["SpaceTimeSlot"].__str__() + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.generalRooms.items()}).__str__()[11:-1] + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.privateRooms.items()}).__str__()[11:-1] + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.activities.items()}).__str__()[11:-1] + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.spacetimeSlots.items()}).__str__()[11:-1] + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.mathCircles.items()}).__str__()[11:-1] + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.expenses.items()}).__str__()[11:-1] + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.participants.items()}).__str__()[11:-1] + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.counselors.items()}).__str__()[11:-1] + ", " +
            SortedDict({k.__str__(): v.__str__() for (k, v) in self.guests.items()}).__str__()[11:-1] + ", " +
            self.schedule.__str__() + ")"
        )

    def isDuringCamp(self, time):
        """
        returns a Boolean stating whether the given date time is during the Mathecamp or not
        :param time: datetime to check
        :return: a Boolean
        """
        if (self.dates["start"] <= time and time <= self.dates["end"]):
            return True
        else:
            return False

    def isConsistent(self):
        """
        checks if all referenced IDs exist in the mathcamp
        :return: a Boolean expressing whether the mathcamp is consistent or not
        """
        # TODO implement isConsistent method
        return True

    # </editor-fold>

    # <editor-fold desc="Add data methods">

    def addRoom(self, room):
        """
        method for adding a room to the project
        :param room: a room of type Room
        :return:
        """

        nextId = self.nextIds["Room"]
        if (isinstance(room, GeneralRoom)):
            self.generalRooms.append((nextId, room))
        if (isinstance(room, PrivateRoom)):
            self.privateRooms.append((nextId, room))
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

    def addRoomWithID(self, room, id):
        """
        method for adding a room to the project
        :param room: a room of type Room
        :return:
        """

        nextId = self.nextIds["Room"]
        if (isinstance(room, GeneralRoom)):
            self.generalRooms.append((nextId, room))
        if (isinstance(room, PrivateRoom)):
            self.privateRooms.append((nextId, room))
        self.nextIds["Room"] += 1

    def addActivityWithID(self, activity, id):
        """
        method for adding an activity to the project
        :param activity: an activity of type Activity
        :return:
        """

        self.activities.append((self.nextIds["Activity"], activity))
        self.nextIds["Activity"] += 1

    def addMathCircleWithID(self, mathCircle, id):
        """
        method for adding a math circle to the project
        :param mathCircle: a mathcircle of type MathCircle
        :return:
        """

        self.mathCircles.append((self.nextIds["MathCircle"], mathCircle))
        self.nextIds["MathCircle"] += 1

    def addHumanWithID(self, human, id):
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

    def addExpenseWithID(self, expense, id):
        """
        method for adding an expense
        :param expense: the expense to add of type Expense
        :return:
        """

        self.expenses.append((self.nextIds["Expense"], expense))
        self.nextIds["Expense"] += 1

    # </editor-fold>
