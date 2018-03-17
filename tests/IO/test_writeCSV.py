#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.dictionaries.test_mathecamp import getMathecampExample
from mathecamp_konfigurator.export import IO
import os

def test_writeMathecampToFile():
    mathecamp = getMathecampExample()[0]

    path = os.path.realpath(__file__)[:-16] + "testData/"
    if not os.path.isdir(path):
        os.mkdir(path)
    testIO = IO(path)

    testIO.writeMathecampToFiles(mathecamp)
    parsedMathecamp = testIO.readMathecampFromFiles()

    assert(parsedMathecamp.toDict() == mathecamp.toDict())
    testIO.cleanDirectory()

