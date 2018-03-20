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

"""This file defines many types used in mathecamp-konfigurator."""

##########
# Import #
##########

from mathecamp_konfigurator import db

##################
# EmailAddresses #
##################

class EmailAddress(db.Model):
    """
    This is an email address
    """
    
    __tablename__ = 'emailAddresses'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    email = db.Column(db.String(128))
    
    def __repr__(self):
        return ("EmailAddress({0})".format(self.email))

    def toDict(self):
        return ({"email": self.email})

    @classmethod
    def fromDict(cls, dictionary):
        return (EmailAddress(email = dictionary["email"]))

    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (EmailAddress(email = dictionary["email"]))

################
# PhoneNumbers #
################

class PhoneNumber(db.Model):
    """
    This is a phone number
    """
    
    __tablename__ = 'phonenumbers'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    number = db.Column(db.String(128))
    
    owner = db.Column(db.String(128), nullable = True, default = None)
    
    def __repr__(self):
        if (self.owner == None):
            result = "PhoneNumber({0})".format(self.number)
        else:
            result = "PhoneNumber({0},{1})".format(self.number, self.owner)
        return (result)
    
    def toDict(self):
        return ({"number": self.number, "owner": self.owner})
    
    @classmethod
    def fromDict(cls, dictionary):
        return (PhoneNumber(number = dictionary["number"], owner = dictionary["owner"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (PhoneNumber(number = dictionary["number"],
                             owner = dictionary["owner"]))


####################
# FoodRestrictions #
####################

class FoodRestriction(db.Model):
    """
    This is a food restriction
    """
    
    __tablename__ = 'foodrestrictions'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    def __repr__(self):
        return("FoodRestriction({0})".format(self.name))
    
    def toDict(self):
        return ({"name": self.name})
    
    @classmethod
    def fromDict(cls, dictionary):
        return (FoodRestriction(name = dictionary["name"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (FoodRestriction(name = dictionary["name"]))


#############
# Equipment #
#############

class Equipment(db.Model):
    """
    This is equipment
    """
    
    __tablename__ = 'equipment'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    def __repr__(self):
        return ("Equipment({0})".format(self.name))
    
    def toDict(self):
        return ({"name": self.name})
    
    @classmethod
    def fromDict(cls, dictionary):
        return (Equipment(name = dictionary["name"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Equipment(name = dictionary["name"]))


##############
# Instrument #
##############

class Instrument(db.Model):
    """
    This is an instrument
    """
    
    __tablename__ = 'instruments'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    def __repr__(self):
        return ("Instrument({0})".format(self.name))
    
    def toDict(self):
        return ({"name": self.name})
    
    @classmethod
    def fromDict(cls, dictionary):
        return (Instrument(name = dictionary["name"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Instrument(name = dictionary["name"]))


###########
# Illness #
###########

class Illness(db.Model):
    """
    This class represents deseases, illnesses and medication
    """
    
    __tablename__ = 'illness'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    
    name = db.Column(db.String(128))
    
    def __repr__(self):
        return ("Illness({0})".format(self.name))
    
    def toDict(self):
        return ({"name": self.name})
    
    @classmethod
    def fromDict(cls, dictionary):
        return (Illness(name = dictionary["name"]))
    
    @classmethod
    def fromDictOfStrings(cls, dictionary):
        return (Illness(name = dictionary["name"]))
