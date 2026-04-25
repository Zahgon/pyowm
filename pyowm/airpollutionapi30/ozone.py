#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons import exceptions
from pyowm.utils import formatting, timestamps
from pyowm.weatherapi30 import location


class Ozone:
    """
    A class representing the Ozone (O3) data observed in a certain location
    in the world. The location is represented by the encapsulated *Location* object.

    :param reference_time: GMT UNIXtime telling when the O3 data have been measured
    :type reference_time: int
    :param location: the *Location* relative to this O3 observation
    :type location: *Location*
    :param du_value: the observed O3 Dobson Units value (reference:
        http://www.theozonehole.com/dobsonunit.htm)
    :type du_value: float
    :param interval: the time granularity of the O3 observation
    :type interval: str
    :param reception_time: GMT UNIXtime telling when the observation has
        been received from the OWM Weather API
    :type reception_time: int
    :returns: an *Ozone* instance
    :raises: *ValueError* when negative values are provided as reception time or
      du_value

    """

    def __init__(self, reference_time, location, interval, du_value, reception_time):
        pass

    def reference_time(self, timeformat='unix'):
        """
        Returns the GMT time telling when the O3 data have been measured

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00:00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError when negative values are provided

        """
        pass

    def reception_time(self, timeformat='unix'):
        """
        Returns the GMT time telling when the O3 observation
        has been received from the OWM Weather API

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00:00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError when negative values are provided

        """
        pass

    def is_forecast(self):
        """
        Tells if the current O3 observation refers to the future with respect
        to the current date
        :return: bool
        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses an *Ozone* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: an *Ozone* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the data needed to build the result

        """
        pass

    def to_dict(self):
        """Dumps object to a dictionary

        :returns: a `dict`

        """
        pass

    def __repr__(self):
        return "<%s.%s - reference time=%s, reception time=%s, location=%s, " \
               "interval=%s, value=%s>" % (
                    __name__,
                    self.__class__.__name__,
                    self.reference_time('iso'),
                    self.reception_time('iso'),
                    str(self.location),
                    self.interval,
                    str(self.du_value))
