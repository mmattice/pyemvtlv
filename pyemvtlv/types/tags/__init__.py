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
from builtins import object
import sys
from pyemvtlv.types.tags.taglist import doftags


class BaseTag(object):
    _tagid = None
    __type = 'h'

    def __init__(self, hexvalue=None, value=None):
        if hexvalue is not None and value is not None:
            raise ValueError('Cannot specify both initialization values')
        if hexvalue is None and value is None:
            raise ValueError('Must specify initialization value')
        if hexvalue is not None:
            self._value = unhexlify(hexvalue)
        else:
            self._value = value

    def __repr__(self):
        if not self._value:
            return "{}()".format(self.__class__.__name__)
        if self.__type == 'h':
            return "%s(hexvalue=u'%s')" % (self.__class__.__name__,
                                           hexlify(self._value).decode('ascii'))
        else:
            return "{}(hexvalue={})".format(self.__class__.__name__,
                                            str(self._value))

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
