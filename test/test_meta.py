#!/usr/bin/python

import unittest

from pyemvtlv.types.tags import *


class TestAvailability(unittest.TestCase):
    def test_AmountOtherTagID(self):
        a = AmountOther()
        self.assertEquals(a._tagid, '9F03')


class TestArguments(unittest.TestCase):
    def test_default(self):
        a = AmountOther('abcd')
        self.assertEquals(repr(a), "AmountOther(hexvalue='abcd')")

    def test_hexvalue(self):
        a = AmountOther(hexvalue='abcd')
        self.assertEquals(repr(a), "AmountOther(hexvalue='abcd')")

    def test_value(self):
        a = AmountOther(value='abcd')
        self.assertEquals(repr(a), "AmountOther(hexvalue='61626364')")


if __name__ == '__main__':
    unittest.main()
