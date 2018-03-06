#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file implements methods for exporting and importing Mathecamp instances to csv files in a specified folder.

###########
# Imports #
###########

from mathecamp_konfigurator.camp import Mathecamp
import csv
import os
from sortedcontainers import SortedDict, SortedList


######
# IO #
######

class IO:
    """
    Implements methods for exporting and importing Mathecamp instances to a specified folder.
    """
    
    def __init__(self, directory):
        """
        Main constructor of an IO class instance.
        
        :param directory: the working directory used for importing and exporting as a string
        """
        self.path = directory
    
    def writeDictToFile(self, filename, dictionary):
        """

        :param filename:
        :param dictionary: a dictionary of the type 'Id : SortedDict'
        :return:
        """
        if dictionary == {}:
            return True  # TODO Should there be an empty file instead of none?
        firstKey = dictionary.keys()[0]
        columnNames = SortedList(dictionary[firstKey].keys())
        try:
            with open(filename, 'w', encoding = 'utf-8-sig') as fileToWrite:
                csvFileWriter = csv.DictWriter(fileToWrite, fieldnames = columnNames + ['Id'], delimiter = ';')
                
                csvFileWriter.writeheader()
                for (k, v) in dictionary.items():
                    csvFileWriter.writerow(dict({'Id': k}, **{l: v[l] for l in columnNames}))
        except Exception as e:
            print(e)
            return e
        else:
            return True
    
    def writeGeneralDataDictToFile(self, filename, dictionary):
        """
        writes the generalData dictionary of a mathcamp to a file
        
        :param filename: the path of the file where to write the dictionary to
        :param dictionary: the generalData dictionary to write to file
        :return: True if successful or an exception
        """
        try:
            with open(filename, 'w', encoding = 'utf-8-sig') as fileToWrite:
                csvFileWriter = csv.DictWriter(fileToWrite, fieldnames = ["Key", "Value"], delimiter = ';')
                
                csvFileWriter.writeheader()
                for (k, v) in dictionary.items():
                    csvFileWriter.writerow({"Key": k, "Value": v})
        except Exception as e:
            print(e)
            return e
        else:
            return True
    
    def readDictFromFile(self, filename):
        """

        :param filename:
        :return:
        """
        try:
            result = {}
            if os.path.isfile(self.path + filename):
                with open(self.path + filename, encoding = 'utf-8-sig') as fileToRead:
                    csvFileReader = csv.DictReader(fileToRead, delimiter = ';')
                    for row in csvFileReader:
                        rowId = row.pop('Id')
                        result[rowId] = SortedDict(row)
            else:
                return ({})
        except Exception as e:
            return e
        else:
            return (result)
    
    def readGeneralDataDictFromFile(self, filename):
        """

        :param filename:
        :return:
        """
        try:
            result = {}
            if os.path.isfile(self.path + filename):
                with open(self.path + filename, encoding = 'utf-8-sig') as fileToRead:
                    csvFileReader = csv.DictReader(fileToRead, delimiter = ';')
                    for row in csvFileReader:
                        result[row["Key"]] = row["Value"]
            else:
                return ({})
        except Exception as e:
            return e
        else:
            return (result)
    
    def writeMathecampToFiles(self, mathecamp):
        """

        :param mathecamp:
        :return:
        """
        dictionaryToWrite = mathecamp.toDict()
        
        for dictName in dictionaryToWrite.keys():
            if dictName != "generalData" and dictName != "schedule" and dictionaryToWrite[dictName] != {}:
                self.writeDictToFile(self.path + dictName + ".csv", dictionaryToWrite[dictName])
            elif dictName == "generalData":
                self.writeGeneralDataDictToFile(self.path + dictName + '.csv', dictionaryToWrite[dictName])
            elif dictName == "schedule":
                self.writeScheduleToFile(self.path + dictName + '.csv', dictionaryToWrite[dictName])
    
    def readMathecampFromFiles(self):
        """

        :return: an instance of a Mathecamp
        """
        dictionary = {
            "generalData": self.readGeneralDataDictFromFile("generalData.csv"),
            "generalRooms": self.readDictFromFile("generalRooms.csv"),
            "privateRooms": self.readDictFromFile("privateRooms.csv"),
            "activities": self.readDictFromFile("activities.csv"),
            "mathCircles": self.readDictFromFile("mathCircles.csv"),
            "expenses": self.readDictFromFile("expenses.csv"),
            "participants": self.readDictFromFile("participants.csv"),
            "counselors": self.readDictFromFile("counselors.csv"),
            "guests": self.readDictFromFile("guests.csv"),
            "spacetimeSlots": self.readDictFromFile("spacetimeSlots.csv"),
            "schedule": self.readScheduleFromFile("schedule.csv")
        }
        
        return (Mathecamp.fromDictOfStrings(dictionary))
    
    def cleanDirectory(self):
        for file in os.listdir(self.path):
            try:
                os.remove(self.path + file)
            except Exception:
                os.rmdir(self.path + file)
    
    def writeScheduleToFile(self, filename, list):
        """
        writes a schedule to a file
        
        :param filename: the path of the file where to write the dictionary to
        :param list: the schedule as a list of dictionaries to write to file
        :return: True if successful or an exception
        """
        try:
            with open(filename, 'w', encoding = 'utf-8-sig') as fileToWrite:
                csvFileWriter = csv.DictWriter(fileToWrite, fieldnames = ['mathCircleID', 'spaceTimeSlotID',
                                                                          'teacherID'], delimiter = ';')
                
                csvFileWriter.writeheader()
                for entry in list:
                    csvFileWriter.writerow({'mathCircleID': entry['mathCircleID'], "spaceTimeSlotID": entry[
                        'spaceTimeSlotID'], 'teacherID' : entry['teacherID']})
        except Exception as e:
            print(e)
            return e
        else:
            return True

    def readScheduleFromFile(self, filename):
        """
        reads a schedule dictionary from a csv file

        :param filename: the name of the csv file where the schedule dictionary is located
        :return: a dictionary of strings corresponding to the data in the csv file
        """
        try:
            result = []
            if os.path.isfile(self.path + filename):
                with open(self.path + filename, encoding = 'utf-8-sig') as fileToRead:
                    csvFileReader = csv.DictReader(fileToRead, delimiter = ';')
                    for row in csvFileReader:
                        result.append({'mathCircleID' : row['mathCircleID'], 'spaceTimeSlotID' : row[
                            'spaceTimeSlotID'], 'teacherID' : row['teacherID']})
            else:
                return ([])
        except Exception as e:
            return e
        else:
            return result
