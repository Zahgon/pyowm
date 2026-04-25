#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime as dt
from pyowm.commons import exceptions
from pyowm.utils import formatting


class Station:
    """
    A class representing a meteostation in Stations API.
    A reference about OWM stations can be found at:
    http://openweathermap.org/stations

    :param id: unique OWM identifier for the station
    :type id: str
    :param created_at: UTC timestamp marking the station registration.
    :type created_at: str in format %Y-%m-%dT%H:%M:%S.%fZ
    :param updated_at: UTC timestamp marking the last update to this station
    :type updated_at: str in format %Y-%m-%dT%H:%M:%S.%fZ
    :param external_id: user-given identifier for the station
    :type external_id: str
    :param name: user-given name for the station
    :type name: str
    :param lon: longitude of the station
    :type lon: float
    :param lat: latitude of the station
    :type lat: float
    :param alt: altitude of the station
    :type alt: float
    :param rank: station rank
    :type rank: int
    """

    def __init__(self, id, created_at, updated_at, external_id, name,
                 lon, lat, alt, rank):
        pass

    def _format_micros(self, datestring):
        pass

    def creation_time(self, timeformat='unix'):
        """Returns the UTC time of creation of this station

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time, '*iso*' for ISO8601-formatted
            string in the format ``YYYY-MM-DD HH:MM:SS+00`` or `date` for
            a ``datetime.datetime`` object
        :type timeformat: str
        :returns: an int or a str or a ``datetime.datetime`` object or None
        :raises: ValueError

        """
        pass

    def last_update_time(self, timeformat='unix'):
        """Returns the UTC time of the last update on this station's metadata

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time, '*iso*' for ISO8601-formatted
            string in the format ``YYYY-MM-DD HH:MM:SS+00`` or `date` for
            a ``datetime.datetime`` object
        :type timeformat: str
        :returns: an int or a str or a ``datetime.datetime`` object or None
        :raises: ValueError

        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses a *Station* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *Station* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the data needed to build the result

        """
        pass

    def to_dict(self):
        """Dumps object to a dictionary

        :returns: a `dict`

        """
        pass

    def __repr__(self):
        return '<%s.%s - id=%s, external_id=%s, name=%s>' \
               % (__name__, self.__class__.__name__,
                  self.id, self.external_id, self.name)
