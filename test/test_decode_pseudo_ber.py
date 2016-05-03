#!/usr/bin/python

import unittest

from pyemvtlv.types.tags import *
from pyemvtlv.codec.binary.decoder import decode as pber_dec
from binascii import unhexlify


class TestDecodePBER(unittest.TestCase):
    def test_decode0x91(self):
        input = '910a90ca8abbfee0be240012'
        res, remain = pber_dec(unhexlify(input))
        self.assertEquals(res, IssuerAuthenticationData(hexvalue='90ca8abbfee0be240012'))
        self.assertEquals(remain, b'')

    def test_decode0x71(self):
        input = '711e9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1'
        res, remain = pber_dec(unhexlify(input))
        self.assertEquals(res, IssuerScriptTemplate1(hexvalue='9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1'))
        self.assertEquals(remain, b'')

    def test_decode0x8a(self):
        input = '8a023030'
        res, remain = pber_dec(unhexlify(input))
        self.assertEquals(res, AuthorisationResponseCode(hexvalue='3030'))
        self.assertEquals(remain, b'')

    def test_chain(self):
        input = '910a90ca8abbfee0be240012711e9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa18a023030'
        subs = unhexlify(input)
        l = []
        while subs:
            res, subs = pber_dec(subs)
            if res:
                l.append(res)
        self.assertEquals(l, [IssuerAuthenticationData(hexvalue='90ca8abbfee0be240012'),
                              IssuerScriptTemplate1(hexvalue='9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa1'),
                              AuthorisationResponseCode(hexvalue='3030')])

    def test_shortdecodeV(self):
        input = '8a033030'
        self.assertRaisesRegexp(ValueError, 'Insufficient remaining substrate - 1 bytes short', pber_dec, unhexlify(input))

    def test_shortdecodeL(self):
        input = '8a8201'
        self.assertRaisesRegexp(ValueError, 'Short decode on length parsing - 1 bytes short', pber_dec, unhexlify(input))

    def test_failfind(self):
        input = '0a0101'
        self.assertRaisesRegexp(ValueError, 'Cannot find tagId A', pber_dec, unhexlify(input))


if __name__ == '__main__':
    unittest.main()
