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
from pyemvtlv.codec.binary.encoder import encode as pber_enc
from binascii import unhexlify

from builtins import map


class TestEncodePBER(unittest.TestCase):
    def test_encode0x91(self):
        input = IssuerAuthenticationData(hexvalue='90ca8abbfee0be240012')
        res = pber_enc(input)
        self.assertEquals(res, unhexlify('910a90ca8abbfee0be240012'))

    def test_encode0x71(self):
        input = IssuerScriptTemplate1(hexvalue='9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1')
        res = pber_enc(input)
        self.assertEquals(res, unhexlify('711e9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1'))

    def test_encode0x8a(self):
        input = AuthorisationResponseCode(hexvalue='3030')
        res = pber_enc(input)
        self.assertEquals(res, unhexlify('8a023030'))

    def test_chain(self):
        input = [IssuerAuthenticationData(hexvalue='90ca8abbfee0be240012'),
                 IssuerScriptTemplate1(hexvalue='9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1'),
                 AuthorisationResponseCode(hexvalue='3030')]
        res = b''.join(map(pber_enc, input))
        self.assertEquals(res, unhexlify('910a90ca8abbfee0be240012711e9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa18a023030'))


if __name__ == '__main__':
    unittest.main()
