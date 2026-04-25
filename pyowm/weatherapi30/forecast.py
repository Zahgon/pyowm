#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from pyowm.commons import  exceptions
from pyowm.utils import timestamps, formatting
from pyowm.weatherapi30 import location
from pyowm.weatherapi30 import weather


class Forecast:
    """
    A class encapsulating weather forecast data for a certain location and
    relative to a specific time interval (forecast for every three hours or
    for every day)

    :param interval: the time granularity of the forecast. May be: *'3h'* for
        three hours forecast or *'daily'* for daily ones
    :type interval: str
    :param reception_time: GMT UNIXtime of the forecast reception from the OWM
        web API
    :type reception_time: int
    :param location: the *Location* object relative to the forecast
    :type location: Location
    :param weathers: the list of *Weather* objects composing the forecast
    :type weathers: list
    :returns:  a *Forecast* instance
    :raises: *ValueError* when negative values are provided

    """

    def __init__(self, interval, reception_time, location, weathers):
        pass

    def get(self, index):
        """
        Lookups up into the *Weather* items list for the item at the specified
        index

        :param index: the index of the *Weather* object in the list
        :type index: int
        :returns: a *Weather* object
        """
        pass

    def reception_time(self, timeformat='unix'):
        """Returns the GMT time telling when the forecast was received
            from the OWM Weather API

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError

        """
        pass

    def actualize(self):
        """
        Removes from this forecast all the *Weather* objects having a reference
        timestamp in the past with respect to the current timestamp
        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses a *Forecast* instance out of a raw data dictionary. Only certain properties of the data are used: if
        these properties are not found or cannot be parsed, an error is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *Forecast* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the
            data needed to build the result, *APIResponseError* if the input dictionary embeds an HTTP status error

        """
        pass

    def to_dict(self):
        """Dumps object to a dictionary

        :returns: a `dict`

        """
        pass

    def __len__(self):
        return len(self.weathers)

    def __iter__(self):
        return iter(self.weathers)

    def __repr__(self):
        return "<%s.%s - reception_time=%s, interval=%s>" % (__name__, \
              self.__class__.__name__, self.reception_time('iso'),
              self.interval)