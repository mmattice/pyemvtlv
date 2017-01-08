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
from pyemvtlv.codec.binary.decoder import decode as pber_dec
from binascii import unhexlify


class TestDecodePBER(unittest.TestCase):
    def test_decode0x91(self):
        input = '910a90ca8abbfee0be240012'
        res, remain = pber_dec(unhexlify(input))
        self.assertEqual(res, IssuerAuthenticationData(hexvalue='90ca8abbfee0be240012'))
        self.assertEqual(remain, b'')

    def test_decode0x71(self):
        input = '711e9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1'
        res, remain = pber_dec(unhexlify(input))
        self.assertEqual(res, IssuerScriptTemplate1(hexvalue='9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1'))
        self.assertEqual(remain, b'')

    def test_decode0x8a(self):
        input = '8a023030'
        res, remain = pber_dec(unhexlify(input))
        self.assertEqual(res, AuthorisationResponseCode(hexvalue='3030'))
        self.assertEqual(remain, b'')

    def test_chain(self):
        input = '910a90ca8abbfee0be240012711e9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa18a023030'
        subs = unhexlify(input)
        l = []
        while subs:
            res, subs = pber_dec(subs)
            if res:
                l.append(res)
        self.assertEqual(l, [IssuerAuthenticationData(hexvalue='90ca8abbfee0be240012'),
                              IssuerScriptTemplate1(hexvalue='9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1'),
                              AuthorisationResponseCode(hexvalue='3030')])

    def test_shortdecodeV(self):
        input = '8a033030'
        self.assertRaisesRegexp(ValueError, 'Insufficient remaining substrate - 1 bytes short', pber_dec, unhexlify(input))

    def test_shortdecodeL(self):
        input = '8a8201'
        self.assertRaisesRegexp(ValueError, 'Short decode on length parsing - 1 bytes short', pber_dec, unhexlify(input))

    def test_shortdecodeT(self):
        input = '9f'
        self.assertRaisesRegexp(ValueError, 'Short octet stream on long tag decoding', pber_dec, unhexlify(input))

    def test_failfind(self):
        input = '0a0101'
        self.assertRaisesRegexp(ValueError, 'Cannot find tagId A', pber_dec, unhexlify(input))

    def test_decodelong(self):
        input = '8a820101' + '00' * 257
        res, remain = pber_dec(unhexlify(input))
        self.assertEqual(res, AuthorisationResponseCode(hexvalue='00' * 257))

if __name__ == '__main__':
    unittest.main()
