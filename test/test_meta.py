#!/usr/bin/python
# Copyright (C) 2016 Mike Mattice
#
# This file is part of pyemvtlv.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# (1) Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# (2) Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the
# distribution.
#
# (3)The name of the author may not be used to
# endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

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
