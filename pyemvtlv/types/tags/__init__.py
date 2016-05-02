import sys
from pyemvtlv.types.tags.taglist import doftags


class BaseTag(object):
    _tagid = None


class TagModule(object):
    def __init__(self, doftags):
        self.__doftags = doftags
        self.__all__ = list(doftags.iterkeys())
        self.__path__ = __path__
        for item in doftags:
            self.__dict__[item] = self.createTagClass(item, doftags[item])

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        raise AttributeError('no attribute named {}'.format(item))

    def createTagClass(self, name, tagid):
        return type(name, (BaseTag, ), {"_tagid": tagid})

sys.modules[__name__] = TagModule(doftags)
