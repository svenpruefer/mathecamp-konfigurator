#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.dictionaries.test_mathecamp import getMathecampExample
from mathecamp_konfigurator.export import IO

def test_writeMathecampToFile():
    mathecamp = getMathecampExample()[0]

    testIO = IO("~/")

    testIO.writeMathecampToFiles(mathecamp)
    assert(True)
