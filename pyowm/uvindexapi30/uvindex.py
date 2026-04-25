#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons import exceptions
from pyowm.utils import formatting, timestamps
from pyowm.weatherapi30 import location


def uv_intensity_to_exposure_risk(uv_intensity):
    # According to figures in: https://en.wikipedia.org/wiki/Ultraviolet_index
    pass


class UVIndex:
    """
    A class representing the UltraViolet Index observed in a certain location
    in the world. The location is represented by the encapsulated *Location* object.

    :param reference_time: GMT UNIXtime telling when the UV data have been measured
    :type reference_time: int
    :param location: the *Location* relative to this UV observation
    :type location: *Location*
    :param value: the observed UV intensity value
    :type value: float
    :param reception_time: GMT UNIXtime telling when the observation has
        been received from the OWM Weather API
    :type reception_time: int
    :returns: an *UVIndex* instance
    :raises: *ValueError* when negative values are provided as reception time or
      UV intensity value

    """

    def __init__(self, reference_time, location, value, reception_time):
        pass

    def reference_time(self, timeformat='unix'):
        """
        Returns the GMT time telling when the UV has been observed
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

    def reception_time(self, timeformat='unix'):
        """
        Returns the GMT time telling when the UV has been received from the API

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError when negative values are provided

        """
        pass

    def get_exposure_risk(self):
        """
        Returns a string stating the risk of harm from unprotected sun exposure
        for the average adult on this UV observation
        :return: str
        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses an *UVIndex* instance out of raw JSON data. Only certain properties of the data are used: if these
        properties are not found or cannot be parsed, an error is issued.

        :param the_dict: the input dict
        :type the_dict: dict
        :returns: an *UVIndex* instance or ``None`` if no data is available
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
        return "<%s.%s - reference time=%s, reception time=%s, location=%s, " \
               "value=%s>" % (
                    __name__,
                    self.__class__.__name__,
                    self.reference_time('iso'),
                    self.reception_time('iso'),
                    str(self.location),
                    str(self.value))
