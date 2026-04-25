#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
from pyowm.utils import formatting


def now(timeformat='date'):
    """
    Returns the current time in the specified timeformat.

    :param timeformat: the target format for the time conversion. May be:
        '*date*' (default - outputs a ``datetime.datetime`` object), '*unix*'
        (outputs a long UNIXtime) or '*iso*' (outputs an ISO8601-formatted
        string with pattern ``YYYY-MM-DD HH:MM:SS+00``)
    :type timeformat: str
    :returns: the current time value
    :raises: ValueError when unknown timeformat switches are provided or
        when negative time values are provided
    """
    pass


def next_hour(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the next hour
    from now or from the specified ``datetime.datetime`` object.

    :param date: the date you want an hour to be added (if left ``None``,
        the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def last_hour(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the last hour
    before now or before the specified ``datetime.datetime`` object.

    :param date: the date you want an hour to be subtracted from (if left
        ``None``, the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def next_three_hours(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the next three
    hours from now or from the specified ``datetime.datetime`` object.

    :param date: the date you want three hours to be added (if left ``None``,
        the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def last_three_hours(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to last three
    hours before now or before the specified ``datetime.datetime`` object.

    :param date: the date you want three hours to be subtracted from (if left
        ``None``, the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def tomorrow(hour=None, minute=None):
    """
    Gives the ``datetime.datetime`` object corresponding to tomorrow. The
    default value for optional parameters is the current value of hour and
    minute. I.e: when called without specifying values for parameters, the
    resulting object will refer to the time = now + 24 hours; when called with
    only hour specified, the resulting object will refer to tomorrow at the
    specified hour and at the current minute.

    :param hour: the hour for tomorrow, in the format *0-23* (defaults to
        ``None``)
    :type hour: int
    :param minute: the minute for tomorrow, in the format *0-59* (defaults to
        ``None``)
    :type minute: int
    :returns: a ``datetime.datetime`` object
    :raises: *ValueError* when hour or minute have bad values

    """
    pass


def yesterday(hour=None, minute=None):
    """
    Gives the ``datetime.datetime`` object corresponding to yesterday. The
    default value for optional parameters is the current value of hour and
    minute. I.e: when called without specifying values for parameters, the
    resulting object will refer to the time = now - 24 hours; when called with
    only hour specified, the resulting object will refer to yesterday at the
    specified hour and at the current minute.

    :param hour: the hour for yesterday, in the format *0-23* (defaults to
        ``None``)
    :type hour: int
    :param minute: the minute for yesterday, in the format *0-59* (defaults to
        ``None``)
    :type minute: int
    :returns: a ``datetime.datetime`` object
    :raises: *ValueError* when hour or minute have bad values
    """
    pass


def next_week(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the next week
    from now or from the specified ``datetime.datetime`` object. A week
    corresponds to 7 days.

    :param date: the date you want a week to be added (if left ``None``,
        the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def last_week(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the last week
    before now or before the specified ``datetime.datetime`` object. A week
    corresponds to 7 days.

    :param date: the date you want a week to be subtracted from (if left
       ``None``, the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def last_month(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the last month
    before now or before the specified ``datetime.datetime`` object. A month
    corresponds to 30 days.

    :param date: the date you want a month to be subtracted from (if left
       ``None``, the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def next_month(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the next month
    after now or after the specified ``datetime.datetime`` object. A month
    corresponds to 30 days.

    :param date: the date you want a month to be added to (if left
       ``None``, the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def last_year(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the last year
    before now or before the specified ``datetime.datetime`` object. A year
    corresponds to 365 days.

    :param date: the date you want a year to be subtracted from (if left
       ``None``, the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def next_year(date=None):
    """
    Gives the ``datetime.datetime`` object corresponding to the next year
    after now or after the specified ``datetime.datetime`` object. A month
    corresponds to 30 days.

    :param date: the date you want a year to be added to (if left
       ``None``, the current date and time will be used)
    :type date: ``datetime.datetime`` object
    :returns: a ``datetime.datetime`` object
    """
    pass


def _timedelta_hours(offset, date=None):
    pass


def _timedelta_days(offset, date=None):
    pass


def _timedelta_months(offset, date=None):
    pass


def _timedelta_years(offset, date=None):
    pass


def millis_offset_between_epochs(reference_epoch, target_epoch):
    """
    Calculates the signed milliseconds delta between the reference unix epoch and the provided target unix epoch
    :param reference_epoch: the unix epoch that the millis offset has to be calculated with respect to
    :type reference_epoch: int
    :param target_epoch: the unix epoch for which the millis offset has to be calculated
    :type target_epoch: int
    :return: int
    """
    pass
