#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons import exceptions
from pyowm.utils import geo


class Location:
    """
    A class representing a location in the world. A location is defined through
    a toponym, a couple of geographic coordinates such as longitude and
    latitude and a numeric identifier assigned by the OWM Weather API that uniquely
    spots the location in the world. Optionally, the country specification may
    be provided.

    Further reference about OWM city IDs can be found at:
    http://bugs.openweathermap.org/projects/api/wiki/Api_2_5_weather#3-By-city-ID

    :param name: the location's toponym
    :type name: Unicode
    :param lon: the location's longitude, must be between -180.0 and 180.0
    :type lon: int/float
    :param lat: the location's latitude, must be between -90.0 and 90.0
    :type lat: int/float
    :param _id: the location's OWM city ID
    :type ID: int
    :param country: the location's country (``None`` by default)
    :type country: Unicode
    :returns: a *Location* instance
    :raises: *ValueError* if lon or lat values are provided out of bounds
    """

    def __init__(self, name, lon, lat, _id, country=None):
        pass

    def to_geopoint(self):
        """
        Returns the geoJSON compliant representation of this location

        :returns: a ``pyowm.utils.geo.Point`` instance

        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses a *Location* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *Location* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the data needed to build the result

        """
        pass

    def to_dict(self):
        """Dumps object to a dictionary

        :returns: a `dict`

        """
        pass

    def __repr__(self):
        return "<%s.%s - id=%s, name=%s, lon=%s, lat=%s>" % (__name__, \
                                                             self.__class__.__name__, self.id, self.name, str(self.lon), \
                                                             str(self.lat))