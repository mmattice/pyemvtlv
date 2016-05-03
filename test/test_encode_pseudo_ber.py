#!/usr/bin/python

import unittest

from pyemvtlv.types.tags import *
from pyemvtlv.codec.binary.encoder import encode as pber_enc
from binascii import unhexlify


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
        res = ''.join(map(pber_enc, input))
        self.assertEquals(res, unhexlify('910a90ca8abbfee0be240012711e9f1804000000018615842400021022c3089f35064c142447f11fa2ec0aa18a023030'))


if __name__ == '__main__':
    unittest.main()
