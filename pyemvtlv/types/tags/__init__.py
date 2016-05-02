import sys
from pyemvtlv.types.tags.taglist import doftags


class BaseTag(object):
    _tagid = None


class TagModule(object):
    def __init__(self, doftags):
        # store the tags, jic
        self.__doftags = doftags
        # define the list of exported attributes
        self.__all__ = list(doftags.iterkeys())
        # create our classes
        for item in doftags:
            self.__dict__[item] = self.createTagClass(item, doftags[item])

    def createTagClass(self, name, tagid):
        """
        Creates a class named `name` with a tagid of `tagid`
        """
        return type(name, (BaseTag, ), {"_tagid": tagid})

sys.modules[__name__] = TagModule(doftags)
