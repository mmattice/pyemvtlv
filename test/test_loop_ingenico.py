from pyemvtlv.codec.ingenico import decoder as ingdec
from pyemvtlv.codec.ingenico import encoder as ingenc
from pyemvtlv.codec.binary import decoder as berdec
from pyemvtlv.codec.binary import encoder as berenc

from binascii import hexlify

import unittest


class RecodeTestCase(unittest.TestCase):
    def testFull(self):
        return None
        self.startstring = 'T4F:07:hA0000000031010<FS>T57:13:h4888930000000000D00000000000000000000F<FS>T82:02:h1C00<FS>T84:07:hA0000000031010<FS>T95:05:h8000000000<FS>T9A:03:h160114<FS>T9B:02:h6800<FS>T9C:01:h00<FS>T5F2A:02:h0840<FS>T5F34:01:h00<FS>T9F02:06:h000000000215<FS>T9F03:06:h000000000000<FS>T9F06:07:hA0000000031010<FS>T9F09:02:h008C<FS>T9F10:07:h06010A03A0A000<FS>T9F11:01:h01<FS>T9F1A:02:h0840<FS>T9F21:03:h171335<FS>T9F26:08:h2777D84D51E607C4<FS>T9F27:01:h80<FS>T9F33:03:hE0F8C8<FS>T9F34:03:h1E0300<FS>T9F35:01:h22<FS>T9F36:02:h0032<FS>T9F37:04:h980D0885<FS>T9F39:01:h05<FS>T9F40:05:hF000F0A001<FS>T9F41:04:h00000042<FS>T9F53:01:h52<FS>'.replace('<FS>', '\x1c')  # T50:0B:aVisa Credit<FS>T9F1E:08:a80330127<FS>

        subs = self.startstring
        ingdecodelist = []
        while subs:
            y, subs = ingdec.decode(subs)
            ingdecodelist.append(y)

        berencodelist = []
        for y in ingdecodelist:
            berencodelist.append(berenc.encode(y))

        subs = ''.join(berencodelist)
        berdecodelist = []
        while subs:
            y, subs = berdec.decode(subs)
            berdecodelist.append(y)

        ingencodelist = []
        for y in berdecodelist:
            ingencodelist.append(ingenc.encode(y))

        teststring = ''.join(ingencodelist)
        self.assertEqual(self.startstring, teststring)

    def testSingle(self):
        self.startstring = 'T4F:07:hA0000000031010<FS>T57:13:h4888930000000000D00000000000000000000F<FS>T82:02:h1C00<FS>T84:07:hA0000000031010<FS>T95:05:h8000000000<FS>T9A:03:h160114<FS>T9B:02:h6800<FS>T9C:01:h00<FS>T5F2A:02:h0840<FS>T5F34:01:h00<FS>T9F02:06:h000000000215<FS>T9F03:06:h000000000000<FS>T9F06:07:hA0000000031010<FS>T9F09:02:h008C<FS>T9F10:07:h06010A03A0A000<FS>T9F11:01:h01<FS>T9F1A:02:h0840<FS>T9F21:03:h171335<FS>T9F26:08:h2777D84D51E607C4<FS>T9F27:01:h80<FS>T9F33:03:hE0F8C8<FS>T9F34:03:h1E0300<FS>T9F35:01:h22<FS>T9F36:02:h0032<FS>T9F37:04:h980D0885<FS>T9F39:01:h05<FS>T9F40:05:hF000F0A001<FS>T9F41:04:h00000042<FS>T9F53:01:h52<FS>'.replace('<FS>', '\x1c')  # T50:0B:aVisa Credit<FS>T9F1E:08:a80330127<FS>
        sep = '\x1c'

        substrates = (x + sep for x in self.startstring.split(sep))
        for subs in substrates:
            if subs == sep:
                continue
            results = []
            a, remainder = ingdec.decode(subs)
            results.append(a)
            self.assertEquals(remainder, '')
            b = berenc.encode(a)
            results.append(hexlify(b))
            c, remainder = berdec.decode(b)
            results.append(c)
            self.assertEquals(remainder, '')
            d = ingenc.encode(c)
            results.append(d)
            if subs != d:
                print results
            self.assertEqual(subs, d)

if __name__ == '__main__':
    unittest.main()
