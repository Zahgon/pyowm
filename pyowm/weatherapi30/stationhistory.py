#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from pyowm.commons import exceptions
from pyowm.utils import formatting


class StationHistory:

    """
    A class representing historic weather measurements collected by a
    meteostation. Three types of historic meteostation data can be obtained by
    the OWM Weather API: ticks (one data chunk per minute) data, hourly and daily
    data.

    :param station_id: the numeric ID of the meteostation
    :type station_id: int
    :param interval: the time granularity of the meteostation data history
    :type interval: str
    :param reception_time: GMT UNIXtime of the data reception from the OWM web
         API
    :type reception_time: int
    :param measurements: a dictionary containing raw weather measurements
    :type measurements: dict
    :returns: a *StationHistory* instance
    :raises: *ValueError* when the supplied value for reception time is
        negative
    """

    def __init__(self, station_id, interval, reception_time, measurements):
        pass

    def reception_time(self, timeformat='unix'):
        """Returns the GMT time telling when the meteostation history data was
           received from the OWM Weather API

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError

        """
        pass

    @classmethod
    def from_dict(cls, d):
        """
        Parses a *StationHistory* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *StationHistory* instance or ``None`` if no data is available
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
        return "<%s.%s - station_id=%s, interval=%s>" % (__name__, self.__class__.__name__, self.station_id, self.interval)