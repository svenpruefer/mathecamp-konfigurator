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
            return True # TODO Should there be an empty file instead of none?
        firstKey = dictionary.keys()[0]
        columnNames = SortedList(dictionary[firstKey].keys())
        try:
            with open(filename, 'w', encoding = 'utf-8-sig') as fileToWrite:
                csvFileWriter = csv.DictWriter(fileToWrite, fieldnames = columnNames + ['Id'], delimiter = ';')

                csvFileWriter.writeheader()
                for (k,v) in dictionary.items():
                    csvFileWriter.writerow(dict({'Id' : k}, **{l : v[l] for l in columnNames}))
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
            with open(self.path + filename) as fileToRead:
                csvFileReader = csv.DictReader(fileToRead, delimiter =';')
                for row in csvFileReader:
                    rowId = row.pop('Id')
                    result[rowId] = SortedDict(row)
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
                self.writeDictToFile(dictName + ".csv",dictionaryToWrite[dictName])

    def readMathecampFromFiles(self):
        """

        :return: an instance of a Mathecamp
        """
        # TODO Implement this
        pass

    def cleanDirectory(self):
        for file in os.listdir(self.path):
            try:
                os.remove(file)
            except Exception:
                os.rmdir(file)
