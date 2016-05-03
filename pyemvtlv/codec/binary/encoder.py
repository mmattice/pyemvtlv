from binascii import unhexlify


class Encoder(object):
    def __call__(self, tag):
        tagId = tag._tagid
        l = len(tag._value)
        return ''.join((unhexlify(tagId),
                        chr(l),
                        tag._value))


encode = Encoder()
