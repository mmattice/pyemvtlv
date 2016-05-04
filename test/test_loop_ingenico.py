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
from __future__ import print_function
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

        subs = b''.join(berencodelist)
        berdecodelist = []
        while subs:
            y, subs = berdec.decode(subs)
            berdecodelist.append(y)

        ingencodelist = []
        for y in berdecodelist:
            ingencodelist.append(ingenc.encode(y))

        teststring = b''.join(ingencodelist)
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
            self.assertEquals(remainder, b'')
            d = ingenc.encode(c)
            results.append(d)
            if subs != d:
                print(results)
            self.assertEqual(subs, d)

if __name__ == '__main__':
    unittest.main()
