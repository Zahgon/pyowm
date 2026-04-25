#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons import exceptions
from pyowm.utils import formatting, timestamps
from pyowm.weatherapi30 import location


class AirStatus:
    """
    A class representing a dataset about air quality

    :param reference_time: GMT UNIXtime telling when the data has been measured
    :type reference_time: int
    :param location: the *Location* relative to this measurement
    :type location: *Location*
    :param interval: the time granularity of the CO observation
    :type interval: str
    :param air_quality_data: the dataset
    :type air_quality_data: dict
    :param reception_time: GMT UNIXtime telling when the CO observation has
        been received from the OWM Weather API
    :type reception_time: int
    :returns: an *COIndex* instance
    :raises: *ValueError* when negative values are provided as reception time,
      CO samples are not provided in a list

    """

    def __init__(self, reference_time, location, air_quality_data, reception_time):
        pass

    def reference_time(self, timeformat="unix"):
        """
        Returns the GMT time telling when the air quality data have been measured

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00:00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError when negative values are provided

        """
        pass

    def reception_time(self, timeformat="unix"):
        """
        Returns the GMT time telling when the air quality data has been received
        from the OWM Weather API

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00:00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError when negative values are provided

        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses an *AirStatus* instance or `list` of instances out of a data dictionary.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *AirStatus* instance or ``list` of such instances
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the data needed to build the result

        """
        pass
