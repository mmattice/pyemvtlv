from pyemvtlv.codec.ingenico.decoder import decode as ing_dec
from pyemvtlv.types.tags import *
import unittest


class OctetStringDecoderTestCase(unittest.TestCase):
    def testT4F(self):
        self.assertEquals(ing_dec('T4F:07:hA0000000031010\x1c'),
                          (ApplicationDedicatedFileName(value=b'\xa0\x00\x00\x00\x03\x10\x10'), ''))

    def testT50(self):
        self.assertEquals(ing_dec('T50:0B:aVisa Credit\x1c'),
                          (ApplicationLabel(value='Visa Credit'), ''))

    def testT57(self):
        self.assertEquals(ing_dec('T57:13:h4888930000000000D12341234432143214321F\x1c'),
                          (Track2EquivalentData(value=b'H\x88\x93\x00\x00\x00\x00\x00\xd1#A#D2\x142\x142\x1f'), ''))


class PassOnDTags(unittest.TestCase):
    def testPass(self):
        s = 'D100E:02:aEN<FS>'.replace('<FS>', '\x1c')
        self.assertEqual(ing_dec(s), (None, ''))

    def testPassMultiple(self):
        subs = 'D1005:02:a00<FS>D100E:02:aEN<FS>D9000:01:aB<FS>D9001:01:aC<FS>'.replace('<FS>', '\x1c')
        self.assertEqual(subs[:5], 'D1005')
        y, subs = ing_dec(subs)
        self.assertEqual(y, None)
        self.assertEqual(subs[:5], 'D100E')
        y, subs = ing_dec(subs)
        self.assertEqual(y, None)
        self.assertEqual(subs[:5], 'D9000')
        y, subs = ing_dec(subs)
        self.assertEqual(y, None)
        self.assertEqual(subs[:5], 'D9001')
        y, subs = ing_dec(subs)
        self.assertEqual(y, None)
        self.assertEqual(subs, '')


class Decode3303TestCase(unittest.TestCase):
    def setUp(self):
        self.teststring = 'T4F:07:hA0000000031010<FS>T50:0B:aVisa Credit<FS>T57:13:h4888930000000000D00000000000000000000F<FS>T82:02:h1C00<FS>T84:07:hA0000000031010<FS>T95:05:h8000000000<FS>T9A:03:h160114<FS>T9B:02:h6800<FS>T9C:01:h00<FS>T5F2A:02:h0840<FS>T5F34:01:h00<FS>T9F02:06:h000000000215<FS>T9F03:06:h000000000000<FS>T9F06:07:hA0000000031010<FS>T9F09:02:h008C<FS>T9F10:07:h06010A03A0A000<FS>T9F11:01:h01<FS>T9F1A:02:h0840<FS>T9F1E:08:a80330127<FS>T9F21:03:h171335<FS>T9F26:08:h2777D84D51E607C4<FS>T9F27:01:h80<FS>T9F33:03:hE0F8C8<FS>T9F34:03:h1E0300<FS>T9F35:01:h22<FS>T9F36:02:h0032<FS>T9F37:04:h980D0885<FS>T9F39:01:h05<FS>T9F40:05:hF000F0A001<FS>T9F41:04:h00000042<FS>T9F53:01:h52<FS>D1005:02:a00<FS>D100E:02:aEN<FS>D9000:01:aB<FS>D9001:01:aC<FS>'.replace('<FS>', '\x1c')

        subs = self.teststring
        self.decodelist = []
        while subs:
            y, subs = ing_dec(subs)
            if y:
                self.decodelist.append(y)

    def testFullDecode(self):
        self.assertEqual(len(self.decodelist), 31)

    def testT4F(self):
        self.assertEqual(self.decodelist[0], b'\xa0\x00\x00\x00\x03\x10\x10')

    def testT50(self):
        self.assertEqual(self.decodelist[1]._value, 'Visa Credit')
        self.assertEqual(self.decodelist[1], 'Visa Credit')

    def testT57(self):
        self.assertEqual(self.decodelist[2], b'\x48\x88\x93\x00\x00\x00\x00\x00\xd0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f')

    def testT82(self):
        self.assertEqual(self.decodelist[3], b'\x1c\x00')

    def testT84(self):
        self.assertEqual(self.decodelist[4], b'\xa0\x00\x00\x00\x03\x10\x10')

    def testT95(self):
        self.assertEqual(self.decodelist[5], b'\x80\x00\x00\x00\x00')

    def testT9A(self):
        self.assertEqual(self.decodelist[6], b'\x16\x01\x14')

    def testT9B(self):
        self.assertEqual(self.decodelist[7], b'\x68\x00')

    def testT9C(self):
        self.assertEqual(self.decodelist[8], b'\x00')

    def testT5F2A(self):
        self.assertEqual(self.decodelist[9], b'\x08\x40')

    def testT5F34(self):
        self.assertEqual(self.decodelist[10], b'\x00')

    ##  one two skip a few

    def testT9F53(self):
        self.assertEqual(self.decodelist[30], b'\x52')


class Decode3305TestCase(unittest.TestCase):
    def setUp(self):
        self.teststring = 'T4F:07:hA0000000031010<FS>T50:0B:aVisa Credit<FS>T57:13:h4888930000000000D00000000000000000000F<FS>T82:02:h1C00<FS>T84:07:hA0000000031010<FS>T8A:02:aZ3<FS>T8E:10:h000000000000000042011E031F034203<FS>T95:05:h8000000000<FS>T9A:03:h160114<FS>T9B:02:h6800<FS>T9C:01:h00<FS>T5F2A:02:h0840<FS>T5F34:01:h00<FS>T9F02:06:h000000000215<FS>T9F03:06:h000000000000<FS>T9F06:07:hA0000000031010<FS>T9F07:02:hFF00<FS>T9F08:02:h008C<FS>T9F09:02:h008C<FS>T9F0D:05:h1040848800<FS>T9F0E:05:h0010000000<FS>T9F0F:05:h10409C9800<FS>T9F10:07:h06010A03A0A000<FS>T9F11:01:h01<FS>T9F1A:02:h0840<FS>T9F1E:08:a80330127<FS>T9F21:03:h171335<FS>T9F26:08:h2777D84D51E607C4<FS>T9F27:01:h80<FS>T9F33:03:hE0F8C8<FS>T9F34:03:h1E0300<FS>T9F35:01:h22<FS>T9F36:02:h0032<FS>T9F37:04:h980D0885<FS>T9F41:04:h00000042<FS>T9F53:01:h52<FS>TDF03:05:hDC4000A800<FS>TDF04:05:h0010000000<FS>TDF05:05:hDC4004F800<FS>D1003:01:aE<FS>D1005:02:a00<FS>D100E:02:aEN<FS>D1010:03:aCAN<FS>'.replace('<FS>', '\x1c')

        subs = self.teststring
        self.decodelist = []
        while subs:
            y, subs = ing_dec(subs)
            if y:
                self.decodelist.append(y)

    def testFullDecode(self):
        self.assertEqual(len(self.decodelist), 39)

    def testT9F53(self):
        self.assertEqual(self.decodelist[38], b'\xdc\x40\x04\xf8\x00')


if __name__ == '__main__':
    unittest.main()
