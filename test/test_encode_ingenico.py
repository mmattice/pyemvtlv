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
