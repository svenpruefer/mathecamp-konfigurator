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

from mathecamp_konfigurator import db, Base

curriculum = db.Table('curriculum', Base.metadata,
                      db.Column('mathcircle_id', db.Integer, db.ForeignKey('mathcircles.id')),
                      db.Column('topic_id', db.Integer, db.ForeignKey('topics.id')))

teachingMaterials = db.Table('teachingmaterials', Base.metadata,
                             db.Column('topic_id', db.Integer, db.ForeignKey('topics.id')),
                             db.Column('equipment_id', db.Integer, db.ForeignKey('equipment.id')))

roomEquipment = db.Table('roomequipment', Base.metadata,
                         db.Column('generalroom_id', db.Integer, db.ForeignKey('generalrooms.id')),
                         db.Column('equipment_id', db.Integer, db.ForeignKey('equipment.id')))

interests = db.Table('interests', Base.metadata,
                     db.Column('participant_id', db.Integer, db.ForeignKey('participants.id')),
                     db.Column('topic_id', db.Integer, db.ForeignKey('topics.id')))

parentsEmail = db.Table('parentsemail', Base.metadata,
                        db.Column('participant_id', db.Integer, db.ForeignKey('participants.id')),
                        db.Column('emailaddress_id', db.Integer, db.ForeignKey('emailaddresses.id')))

humanEmail = db.Table('humanemail', Base.metadata,
                      db.Column('human_id', db.Integer, db.ForeignKey('humans.id')),
                      db.Column('emailaddress_id', db.Integer, db.ForeignKey('emailaddresses.id')))

humanPhoneNumbers = db.Table('humanphonenumbers', Base.metadata,
                             db.Column('human_id', db.Integer, db.ForeignKey('humans.id')),
                             db.Column('phonenumber_id', db.Integer, db.ForeignKey('phonenumbers.id')))

intolerances = db.Table('intolerances', Base.metadata,
                        db.Column('human_id', db.Integer, db.ForeignKey('humans.id')),
                        db.Column('foodrestriction_id', db.Integer, db.ForeignKey('foodrestrictions.id')))


class EmergencyNumbers(db.Model):
    __tablename__ = 'emergencynumbers'

    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), primary_key=True)
    emergencynumber_id = db.Column(db.Integer, db.ForeignKey('phonenumbers.id'), primary_key=True)
    name = db.Column(db.String)

    emergencynumber = db.relationship("PhoneNumber")


musicians = db.Table('musicians', Base.metadata,
                     db.Column('participant_id', db.Integer, db.ForeignKey('participants.id')),
                     db.Column('instrument_id', db.Integer, db.ForeignKey('instruments.id')))

sickPeople = db.Table('sickpeople', Base.metadata,
                      db.Column('participant_id', db.Integer, db.ForeignKey('participants.id')),
                      db.Column('illness_id', db.Integer, db.ForeignKey('illness.id')))

friendships = db.Table('friendships', Base.metadata,
                       db.Column('friend_id', db.Integer, db.ForeignKey('participants.id')),
                       db.Column('islikedfriend_id', db.Integer, db.ForeignKey('participants.id')))

gradePreferences = db.Table('grade', Base.metadata,
                            db.Column('counselor_id', db.Integer, db.ForeignKey('counselors.id')),
                            db.Column('grade_id', db.Integer, db.ForeignKey('grades.id')))
