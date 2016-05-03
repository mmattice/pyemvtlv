import sys
from pyemvtlv.types.tags.taglist import doftags


class BaseTag(object):
    _tagid = None
    __type = 'h'

    def __init__(self, hexvalue=None, value=None):
        if hexvalue is not None and value is not None:
            raise ValueError('Cannot specify both initialization values')
        if hexvalue:
            self._value = unhexlify(hexvalue)
        else:
            self._value = value

    def __repr__(self):
        if not self._value:
            return "{}()".format(self.__class__.__name__)
        if self.__type == 'h':
            return "{}(hexvalue='{}')".format(self.__class__.__name__,
                                              hexlify(self._value))
        else:
            return "{}(hexvalue={})".format(self.__class__.__name__,
                                            self._value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._tagid, self._value) == (other._tagid, other._value)
        else:
            return self._value == other


class TagModule(object):
    def __init__(self, doftags):
        # store the tags, jic
        self.__doftags = doftags
        # define the list of exported attributes
        self.__all__ = list(doftags.keys())
        # copy our name from this module's name
        self.__name__ = __name__
        # create our classes
        for item in doftags:
            self.__dict__[item] = self.createTagClass(item, doftags[item])

    def createTagClass(self, name, tagid):
        """
        Creates a class named `name` with a tagid of `tagid`
        """
        return type(name, (BaseTag, ), {"_tagid": tagid})

sys.modules[__name__] = TagModule(doftags)

# imports we want to be available after we flush sys.modules[__name__].__dict__
# with the override above
from binascii import hexlify, unhexlify
