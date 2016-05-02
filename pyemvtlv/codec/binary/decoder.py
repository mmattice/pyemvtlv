from pyemvtlv.types import tags

tl = [getattr(tags, n) for n in dir(tags)
      if getattr(getattr(tags, n), '_tagid', None)]


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
    return (tagClass, tagFormat, tagId)


class Decoder(object):
    def __init__(self, taglist):
        self.__taglist = taglist

    def __call__(self, value):
        pass


decode = Decoder(tl)
