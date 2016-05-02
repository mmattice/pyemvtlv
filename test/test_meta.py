#!/usr/bin/python

import unittest

from pyemvtlv.types.tags import *


class TestAvailability(unittest.TestCase):
    def test1(self):
        a = AmountOther()
        self.assertEquals(a._tagid, '9F03')

if __name__ == '__main__':
    unittest.main()
