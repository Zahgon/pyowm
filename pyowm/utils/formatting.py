#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calendar import timegm
from datetime import datetime, timedelta, timezone, tzinfo

ZERO = timedelta(0)


class UTC(tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        pass

    def tzname(self, dt):
        pass

    def dst(self, dt):
        pass


def timeformat(timeobject, timeformat):
    """
    Formats the specified time object to the target format type.

    :param timeobject: the object conveying the time value
    :type timeobject: int, ``datetime.datetime`` or ISO8601-formatted
        string with pattern ``YYYY-MM-DD HH:MM:SS+00:00``
    :param timeformat: the target format for the time conversion. May be:
        '*unix*' (outputs an int UNIXtime), '*date*' (outputs a
        ``datetime.datetime`` object) or '*iso*' (outputs an ISO8601-formatted
        string with pattern ``YYYY-MM-DD HH:MM:SS+00:00``)
    :type timeformat: str
    :returns: the formatted time
    :raises: ValueError when unknown timeformat switches are provided or
        when negative time values are provided
    """
    pass


def to_date(timeobject):
    """
    Returns the ``datetime.datetime`` object corresponding to the time value
    conveyed by the specified object, which can be either a UNIXtime, a
    ``datetime.datetime`` object or an ISO8601-formatted string in the format
    `YYYY-MM-DD HH:MM:SS+00:00``.

    :param timeobject: the object conveying the time value
    :type timeobject: int, ``datetime.datetime`` or ISO8601-formatted
        string
    :returns: a ``datetime.datetime`` object
    :raises: *TypeError* when bad argument types are provided, *ValueError*
        when negative UNIXtimes are provided
    """
    pass


def to_ISO8601(timeobject):
    """
    Returns the ISO8601-formatted string corresponding to the time value
    conveyed by the specified object, which can be either a UNIXtime, a
    ``datetime.datetime`` object or an ISO8601-formatted string in the format
    `YYYY-MM-DD HH:MM:SS+00:00``.

    :param timeobject: the object conveying the time value
    :type timeobject: int, ``datetime.datetime`` or ISO8601-formatted
        string
    :returns: an ISO8601-formatted string with pattern
        `YYYY-MM-DD HH:MM:SS+00:00``
    :raises: *TypeError* when bad argument types are provided, *ValueError*
        when negative UNIXtimes are provided
    """
    pass


def to_UNIXtime(timeobject):
    """
    Returns the UNIXtime corresponding to the time value conveyed by the
    specified object, which can be either a UNIXtime, a
    ``datetime.datetime`` object or an ISO8601-formatted string in the format
    `YYYY-MM-DD HH:MM:SS+00:00``.

    :param timeobject: the object conveying the time value
    :type timeobject: int, ``datetime.datetime`` or ISO8601-formatted
        string
    :returns: an int UNIXtime
    :raises: *TypeError* when bad argument types are provided, *ValueError*
        when negative UNIXtimes are provided
    """
    pass


def ISO8601_to_UNIXtime(iso):
    """
    Converts an ISO8601-formatted string in the format
    ``YYYY-MM-DD HH:MM:SS+00:00`` to the correspondent UNIXtime

    :param iso: the ISO8601-formatted string
    :type iso: string
    :returns: an int UNIXtime
    :raises: *TypeError* when bad argument types are provided, *ValueError*
        when the ISO8601 string is badly formatted

    """
    pass


def datetime_to_UNIXtime(date):
    """
    Converts a ``datetime.datetime`` object to its correspondent UNIXtime

    :param date: the ``datetime.datetime`` object
    :type date: ``datetime.datetime``
    :returns: an int UNIXtime
    :raises: *TypeError* when bad argument types are provided
    """
    pass
