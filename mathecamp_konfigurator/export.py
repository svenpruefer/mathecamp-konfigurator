#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file implements methods for exporting and importing Mathecamp instances to csv files in a specified folder.

###########
# Imports #
###########

from mathecamp_konfigurator.camp import Mathecamp
import csv

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
        :param dictionary:
        :return:
        """
        pass

    def readDictFromFile(self, filename):
        """

        :param filename:
        :return:
        """
        pass

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
