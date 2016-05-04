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
from builtins import zip
from builtins import range
from builtins import object
from builtins import bytes
from pyemvtlv.types import tags
from functools import reduce

td = {getattr(getattr(tags, n), '_tagid', None): getattr(tags, n)
      for n in dir(tags) if getattr(getattr(tags, n), '_tagid', None)}


def parsetag(x):
    substrate = x
    firstOctet = substrate[0]
    substrate = substrate[1:]
    t = firstOctet
    tagClass = t & 0xC0
    tagFormat = t & 0x20
    tagId = t
    if (tagId & 0x1F) == 0x1F:
        while 1:
            if not substrate:
                raise Exception(
                    'Short octet stream on long tag decoding'
                )
            t = substrate[0]
            tagId = tagId << 8 | t
            substrate = substrate[1:]
            if not t & 0x80:
                break
    return (tagClass, tagFormat, tagId, substrate)


def bytestringtoint(s):
    add = lambda x, y : x + y
    return reduce(add, [ord(x) * 256 ** y
                        for x, y in zip(list(s),
                                        list(range(len(s) - 1, -1, -1)))])


def parselen(x):
    substrate = x
    firstOctet = substrate[0]
    substrate = substrate[1:]
    t = firstOctet
    if t & 0x80:
        l = t & 0x7f
        if len(substrate) < l:
            raise ValueError('Short decode on length parsing - {} bytes short'.format(l - len(substrate)))
        lens = substrate[:l]
        substrate = substrate[l:]
        t = bytestringtoint(lens)
    if t > len(substrate):
        raise ValueError('Insufficient remaining substrate - {} bytes short'.format(t - len(substrate)))
    return (t, substrate)


class Decoder(object):
    def __init__(self, taghash):
        self.__taghash = taghash

    def __call__(self, value):
        cl, f, tag, substrate = parsetag(bytes(value))
        tagid = "%X" % tag
        if tagid not in self.__taghash:
            raise ValueError('Cannot find tagId {}'.format(tagid))
        t = self.__taghash[tagid]
        l, substrate = parselen(substrate)
        v = substrate[:l]
        substrate = substrate[l:]
        return (t(value=v), substrate)


decode = Decoder(td)
