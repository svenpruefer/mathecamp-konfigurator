#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file implements methods for exporting and importing Mathecamp instances to csv files in a specified folder.

###########
# Imports #
###########

from mathecamp_konfigurator.camp import Mathecamp
import csv
import codecs
from sortedcontainers import SortedDict


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
    
    def writeDictToFile(self, filename, dictionary, columnNames):
        """

        :param filename:
        :param dictionary: a dictionary of the type 'Id : SortedDict'
        :param columnNames: a list of column names besides Id for the keys of the dictionary
        :return:
        """
        try:
            with codecs.open(self.path + filename, 'wb', 'utf-8-sig') as fileToWrite:
                csvFileWriter = csv.DictWriter(fileToWrite, fieldnames = ['Id'].append(columnNames), delimiter = ';')
                
                csvFileWriter.writeheader()
                for (k,v) in dictionary.items():
                    csvFileWriter.writerow({'Id' : k}.update({l : v[l] for l in columnNames}))
        except Exception as e:
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
        pass
    
    def readMathecampFromFiles(self, mathecamp):
        """

        :param mathecamp:
        :return:
        """
        pass
