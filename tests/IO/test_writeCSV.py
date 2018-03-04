#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.dictionaries.test_mathecamp import getMathecampExample
from mathecamp_konfigurator.export import IO
from mathecamp_konfigurator.mktypes import FoodRestriction
import os

def test_writeMathecampToFile():
    mathecamp = getMathecampExample()[0]

    testIO = IO(os.path.realpath(__file__)[:-16])

    testIO.writeMathecampToFiles(mathecamp)
    parsedMathecamp = testIO.readMathecampFromFiles()

    assert(parsedMathecamp.toDict() == mathecamp.toDict())
    testIO.cleanDirectory()

