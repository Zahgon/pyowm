#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.utils import formatting
from pyowm.commons import exceptions


class NationalWeatherAlert:
    """
    A class representing a national weather alert . Alerts are provided by major national
    weather warning systems.

    This is the list of such major warning systems:
    https://openweathermap.org/api/one-call-api#listsource

    :param sender: the warning systems's name
    :type sender: str
    :param title: alert event name
    :type title: str
    :param description: description of the alert
    :type description: str
    :param start_time: UTC UNIXtime telling when the event is to start
    :type start_time: int
    :param end_time: UTC UNIXtime telling when the event is to end
    :type end_time: int
    :param tags: list of labels categorizing the event
    :type tags: list of str

    :returns: a *NationalWeatherAlert* instance
    :raises: *ValueError* if any parameter has wrong type
    """
    def __init__(self, sender, title, description, start_time, end_time, tags=None):
        pass

    def start_time(self, timeformat='unix'):
        """
        Returns the UTC start time of the weather alert event

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str
        :raises: ValueError when negative values are provided

        """
        pass

    def end_time(self, timeformat='unix'):
        """
        Returns the UTC end time of the weather alert event

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
        Parses a *NationalWeatherAlert* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *NationalWeatherAlert* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the data needed to build the result

        """
        pass

    def to_dict(self):
        """Dumps object to a dictionary

        :returns: a `dict`
        """
        pass

    def __repr__(self):
        return "<%s.%s - sender=%s, title=%s, start=%s, end=%s>" % (
            __name__, self.__class__.__name__,
            self.sender, self.title, self.start_time('iso'), self.end_time('iso')
        )
