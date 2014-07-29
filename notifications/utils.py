# -*- coding: utf-8 -*-

import sys

def py_str(obj):
    if sys.version_info.major > 2:
        return str(obj)
    else:
        return unicode(obj)

def slug2id(slug):
    return long(slug) - 110909

def id2slug(id):
    return id + 110909
