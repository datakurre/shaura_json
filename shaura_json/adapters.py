# -*- coding: utf-8 -*-
"""Serialization adapters"""

import re

from datetime import datetime


def encodeFromUnicode(field, value):
    return value.encode("utf-8")


def parseToDatetime(field, value):
    # expects RFC3339 in UTC like 1985-04-12T23:20:50.52Z
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


def datetimeToRFC3339(field, value):
    if not value.microsecond:
        return value.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        return re.sub("0*Z$", "Z", value.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
