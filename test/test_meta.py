#!/usr/bin/python

import unittest

from pyemvtlv.types.tags import *


class TestArguments(unittest.TestCase):
    def test_default(self):
        a = AmountOther(u'abcd')
        self.assertEquals(repr(a), "AmountOther(hexvalue=u'abcd')")

    def test_hexvalue(self):
        a = AmountOther(hexvalue=u'abcd')
        self.assertEquals(repr(a), "AmountOther(hexvalue=u'abcd')")

    def test_value(self):
        a = AmountOther(value=b'abcd')
        self.assertEquals(repr(a), "AmountOther(hexvalue=u'61626364')")

    def test_eq(self):
        a = AmountOther(value=b'abcd')
        self.assertTrue(a == b'abcd')


if __name__ == '__main__':
    unittest.main()
