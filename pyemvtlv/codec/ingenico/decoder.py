from binascii import hexlify

from pyemvtlv.types import tags

td = {getattr(getattr(tags, n), '_tagid', None): getattr(tags, n)
      for n in dir(tags) if getattr(getattr(tags, n), '_tagid', None)}

FS = '\x1c'


class Decoder(object):
    def __init__(self, taghash):
        self.__taghash = taghash

    def __call__(self, substrate):
        i = substrate.index(FS)
        tlv, substrate = substrate[:i], substrate[i+1:]
        tag, length, value = tlv.split(':')
        if tag[0] == 'D':
            return None, substrate
        tagid = tag[1:]
        if tagid not in self.__taghash:
            raise ValueError('Cannot find tagId {}'.format(tagid))
        if value[0] == 'a':
            return (self.__taghash[tagid](value=value[1:]), substrate)
        else:
            return (self.__taghash[tagid](hexvalue=value[1:]), substrate)


decode = Decoder(td)
