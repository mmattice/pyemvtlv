from builtins import map
from pyemvtlv.codec.binary.decoder import decode as pber_dec
from pyemvtlv.codec.ingenico.encoder import encode as ing_enc
import unittest

from base64 import b64decode


class IssuerScriptEncoderTestCase(unittest.TestCase):
    def setUp(self):
        ber = b64decode('kQqQyoq7/uC+JAAScR6fGAQAAAABhhWEJAACECLDCJ81BkwUJEfxH6LsCqGKAjAw')
        el = []
        while ber:
            y, ber = pber_dec(ber)
            if y:
                el.append(y)
        self.el = el

    def testEncodeIssuerScript(self):
        dr = ['T91:0A:h90CA8ABBFEE0BE240012\x1c',
              'T71:1E:h9F1804000000018615842400021022C3089F35064C142447F11FA2EC0AA1\x1c',
              'T8A:02:h3030\x1c']
        tlvs = list(map(ing_enc, self.el))

        self.assertEqual(dr, tlvs)


if __name__ == '__main__':
    unittest.main()
