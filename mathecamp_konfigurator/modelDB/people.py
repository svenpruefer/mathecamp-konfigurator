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

"""This file defines all people related types."""

##########
# Import #
##########

from mathecamp_konfigurator.modelDB.association import interests, parentsEmail, emergencyNumbers, musicians, sickPeople
from mathecamp_konfigurator.modelDB.association import friendships, gradePreferences
from mathecamp_konfigurator import db
from mathecamp_konfigurator.modelDB.enums import Gender, TransportType

#########
# Human #
#########


class Human(db.Model):
    """
    This class is a general human, i.e. either a participant, a counselor or a guest.
    """

    __tablename__ = 'humans'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    familyName = db.Column(db.String)

    givenName = db.Column(db.String)

    birthDate = db.Column(db.DateTime)

    gender = db.Column(db.Enum(Gender))

    emailAddresses = db.relationship("EmailAddress")

    phoneNumbers = db.relationship("PhoneNumber")

    street = db.Column(db.String)

    streetNumber = db.Column(db.String)

    postalCode = db.Column(db.String)

    place = db.Column(db.String)

    arrivalTime = db.Column(db.DateTime)

    arrivalType = db.Column(db.Enum(TransportType))

    departureTime = db.Column(db.DateTime)

    departureType = db.Column(db.Enum(TransportType))

    foodRestrictions = db.relationship("FoodRestriction")

    miscellaneous = db.Column(db.String)

    room_id = db.Column(db.Integer, db.ForeignKey('privaterooms.id'))
    room = db.relationship("PrivateRoom")

###############
# Participant #
###############


class Participant(db.Model):
    """
    A class for participants
    """

    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    human_id = db.Column(db.Integer, db.ForeignKey("humans.id"))
    human = db.relationship("Human")

    campPrice = db.Column(db.Float)

    moneyPayedAlread = db.Column(db.Boolean)

    mathCircle_id = db.Column(db.Integer, db.ForeignKey('mathcircles.id'))
    mathCircle = db.relationship("MathCircle")

    grade = db.Column(db.Integer)

    topicWishes = db.relationship("Topic", secondary = interests)

    emailAddressesParents = db.relationship("EmailAddress", secondary = parentsEmail)

    phoneNumbersEmergency = db.relationship("PhoneNumber", secondary = emergencyNumbers)

    picture = db.Column(db.LargeBinary)

    departureOtherPerson = db.Column(db.String)

    friends = db.relationship("Participant", secondary = friendships,
                              primaryjoin = id == friendships.c.friend_id,
                              secondaryjoin = id == friendships.c.islikedfriend_id,
                              backref = "isLikedBy")

    instruments = db.relationship("Instrument", secondary = musicians)

    illness = db.relationship("Illness", secondary = sickPeople)

    rideSharingPermission = db.Column(db.Boolean)

    swimmingPermission = db.Column(db.Boolean)

    leavingPermission = db.Column(db.Boolean)

    sportsPermission = db.Column(db.Boolean)

#############
# Counselor #
#############


class Counselor(db.Model):
    """
    A class for counselors
    """

    __tablename__ = 'counselors'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    human_id = db.Column(db.Integer, db.ForeignKey('humans.id'))
    human = db.relationship("Human")

    preferredGrades = db.relationship("Grade", secondary = gradePreferences)

#########
# Guest #
#########


class Guest(db.Model):
    """
    A class for guests
    """

    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    human_id = db.Column(db.Integer, db.ForeignKey('humans.id'))
    human = db.relationship("Human")
