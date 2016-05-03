from builtins import object
from binascii import unhexlify
from builtins import bytes


class Encoder(object):
    def __call__(self, tag):
        tlv = [bytes(unhexlify(tag._tagid)), bytes([len(tag._value)]), tag._value]
        etlv = b''.join(tlv)
        return etlv


encode = Encoder()
