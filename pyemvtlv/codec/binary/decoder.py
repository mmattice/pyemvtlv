from pyemvtlv.types import tags

td = {getattr(getattr(tags, n), '_tagid', None): getattr(tags, n)
      for n in dir(tags) if getattr(getattr(tags, n), '_tagid', None)}


def parsetag(x):
    substrate = x
    firstOctet = substrate[0]
    substrate = substrate[1:]
    t = ord(firstOctet)
    tagClass = t & 0xC0
    tagFormat = t & 0x20
    tagId = t
    if (tagId & 0x1F) == 0x1F:
        while 1:
            if not substrate:
                raise Exception(
                    'Short octet stream on long tag decoding'
                )
            t = ord(substrate[0])
            tagId = tagId << 8 | t
            substrate = substrate[1:]
            if not t & 0x80:
                break
    return (tagClass, tagFormat, tagId, substrate)


def bytestringtoint(s):
    add = lambda x, y : x + y
    return reduce(add, [ord(x) * 256 ** y
                        for x, y in zip(list(s),
                                        range(len(s) - 1, -1, -1))])


def parselen(x):
    substrate = x
    firstOctet = substrate[0]
    substrate = substrate[1:]
    t = ord(firstOctet)
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
        cl, f, tag, substrate = parsetag(value)
        tagid = "%X" % tag
        if tagid not in self.__taghash:
            raise ValueError('Cannot find tagId {}'.format(tagid))
        t = self.__taghash[tagid]
        l, substrate = parselen(substrate)
        v = substrate[:l]
        substrate = substrate[l:]
        return (t(value=v), substrate)


decode = Decoder(td)
