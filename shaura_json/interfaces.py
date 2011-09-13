# -*- coding: utf-8 -*-
"""Related interfaces"""

from zope.interface import Interface


class IFieldValue(Interface):
    """Adapts field value to JSON-encodeable value"""


class IJSONValue(Interface):
    """Adapts JSON-decoded value to field value"""
