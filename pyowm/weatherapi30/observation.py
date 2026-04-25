#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from pyowm.commons import exceptions
from pyowm.utils import formatting
from pyowm.weatherapi30 import location
from pyowm.weatherapi30 import weather


class Observation:
    """
    A class representing the weather which is currently being observed in a
    certain location in the world. The location is represented by the
    encapsulated *Location* object while the observed weather data are held by
    the encapsulated *Weather* object.

    :param reception_time: GMT UNIXtime telling when the weather obervation has
        been received from the OWM Weather API
    :type reception_time: int
    :param location: the *Location* relative to this observation
    :type location: *Location*
    :param weather: the *Weather* relative to this observation
    :type weather: *Weather*
    :returns: an *Observation* instance
    :raises: *ValueError* when negative values are provided as reception time

    """

    def __init__(self, reception_time, location, weather):
        pass

    def reception_time(self, timeformat='unix'):
        """
        Returns the GMT time telling when the observation has been received
          from the OWM Weather API

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError when negative values are provided

        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses an *Observation* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: an *Observation* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the
            data needed to build the result, *APIResponseError* if the input dict embeds an HTTP status error

        """
        pass

    def to_dict(self):
        """Dumps object to a dictionary

        :returns: a `dict`

        """
        pass

    def __repr__(self):
        return "<%s.%s - reception_time=%s>" % (__name__, self.__class__.__name__,
                                                self.reception_time('iso'))

    @classmethod
    def from_dict_of_lists(self, the_dict):
        """
        Parses a list of *Observation* instances out of raw input dict containing a list. Only certain properties of
        the data are used: if these properties are not found or cannot be parsed, an error is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a `list` of *Observation* instances or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the
            data needed to build the result, *APIResponseError* if the OWM API returns an HTTP status error

        """
        pass
