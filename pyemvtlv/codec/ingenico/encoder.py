from builtins import object
from binascii import hexlify

FS = '\x1c'


def printable(s):
    for c in s:
        if not (c.isalnum() or c.isspace()):
            return False
    return True


class Encoder(object):
    def __call__(self, tag):
        tagId = tag._tagid
        l = len(tag._value)
        ls = "%4.4X" % (l,)
        if l < 256:
            ls = ls[2:]
        return 'T{}:{}:h{}{}'.format(tagId,
                                     ls,
                                     hexlify(tag._value).upper().decode('ascii'),
                                     FS)

encode = Encoder()
