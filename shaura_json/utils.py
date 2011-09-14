# -*- coding: utf-8 -*-
"""Serialize and deserialize zope.schema-modeled objects in JSON"""

import simplejson

from zope.schema import getFieldNamesInOrder

from pyramid.threadlocal import get_current_registry

from shaura_json.interfaces import IFieldValue, IJSONValue


def values(obj):
    registry = get_current_registry()
    values = {}
    for interface in obj.__provides__.interfaces():
        for name in getFieldNamesInOrder(interface):
            field = interface[name]
            bound = field.bind(obj)
            value = bound.get(obj)
            values[name] = registry.queryMultiAdapter(
                (field, value), IJSONValue, default=value)
    return values


def encode(obj):
    return simplejson.dumps(values(obj))


def decode(dump, target=None, target_class=None):
    data = simplejson.loads(dump)
    registry = get_current_registry()

    fields = {}

    # collect all target's fields by their name
    if target:
        for interface in target.__provides__.interfaces():
            for name in getFieldNamesInOrder(interface):
                fields[name] = interface[name]

    # collect all target_class' fields by their name
    if target_class:
        for interface in target_class.__implemented__.interfaces():
            for name in getFieldNamesInOrder(interface):
                fields[name] = interface[name]

    values = {}
    for k, v in data.iteritems():
        # convert dictionary keys from unicode to str
        if isinstance(k, unicode):
            k = k.encode("utf-8")
        # convert dictionary values to proper field values
        if k in fields:
            v = registry.queryMultiAdapter(
                (fields[k], v), IFieldValue, default=v)
        values[k] = v

    return values
