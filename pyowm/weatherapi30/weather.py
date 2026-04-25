#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from pyowm.commons import exceptions
from pyowm.utils import formatting, measurables
from pyowm.weatherapi30.uris import ICONS_BASE_URI


class Weather:
    """
    A class encapsulating raw weather data.
    A reference about OWM weather codes and icons can be found at:
    https://openweathermap.org/weather-conditions

    :param reference_time: GMT UNIX time of weather measurement
    :type reference_time: int
    :param sunset_time: GMT UNIX time of sunset or None on polar days
    :type sunset_time: int or None
    :param sunrise_time: GMT UNIX time of sunrise or None on polar nights
    :type sunrise_time: int or None
    :param clouds: cloud coverage percentage
    :type clouds: int
    :param rain: precipitation info
    :type rain: dict
    :param snow: snow info
    :type snow: dict
    :param wind: wind info
    :type wind: dict
    :param humidity: atmospheric humidity percentage
    :type humidity: int
    :param pressure: atmospheric pressure info
    :type pressure: dict
    :param temperature: temperature info
    :type temperature: dict
    :param status: short weather status
    :type status: Unicode
    :param detailed_status: detailed weather status
    :type detailed_status: Unicode
    :param weather_code: OWM weather condition code
    :type weather_code: int
    :param weather_icon_name: weather-related icon name
    :type weather_icon_name: str
    :param visibility_distance: visibility distance
    :type visibility_distance: float
    :param dewpoint: dewpoint
    :type dewpoint: float
    :param humidex: Canadian humidex
    :type humidex: float
    :param heat_index: heat index
    :type heat_index: float
    :param utc_offset: offset with UTC time zone in seconds
    :type utc_offset: int or None
    :param uvi: UV index
    :type uvi: int, float or None
    :param precipitation_probability: Probability of precipitation (forecast only)
    :type precipitation_probability: float or None
    :returns:  a *Weather* instance
    :raises: *ValueError* when negative values are provided for non-negative quantities

    """

    def __init__(self, reference_time, sunset_time, sunrise_time, clouds, rain,
                 snow, wind, humidity, pressure, temperature, status,
                 detailed_status, weather_code, weather_icon_name,
                 visibility_distance, dewpoint, humidex, heat_index,
                 utc_offset=None, uvi=None, precipitation_probability=None):
        pass
        
    def reference_time(self, timeformat='unix'):
        """Returns the GMT time telling when the weather was measured

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date*' for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str or a `datetime.datetime` object
        :raises: ValueError when negative values are provided

        """
        pass

    def sunset_time(self, timeformat='unix'):
        """Returns the GMT time of sunset. Can be `None` in case of polar days.

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date*' for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: 'None`, an int, a str or a `datetime.datetime` object
        :raises: ValueError

        """
        pass

    def sunrise_time(self, timeformat='unix'):
        """Returns the GMT time of sunrise. Can be `None` in case of polar nights.

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date*' for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: 'None`, an int, a str or a `datetime.datetime` object
        :raises: ValueError

        """
        pass

    def wind(self, unit='meters_sec'):
        """Returns a dict containing wind info

        :param unit: the unit of measure for the wind values. May be:
            '*meters_sec*' (default), '*miles_hour*, '*km_hour*',
            '*knots*' or '*beaufort*'
        :type unit: str
        :returns: a dict containing wind info

        """
        pass

    def temperature(self, unit='kelvin'):
        """Returns a dict with temperature info

        :param unit: the unit of measure for the temperature values. May be:
            '*kelvin*' (default), '*celsius*' or '*fahrenheit*'
        :type unit: str
        :returns: a dict containing temperature values.
        :raises: ValueError when unknown temperature units are provided

        """
        # This is due to the fact that the OWM Weather API responses are mixing
        # absolute temperatures and temperature deltas together
        pass

    def barometric_pressure(self, unit='hPa'):
        """
        Returns a dict with pressure info

        :param unit: the unit of measure for the temperature values. May be:
            '*hPa' (default), '*inHg*'
        :type unit: str
        :returns: a dict containing pressure values.
        :raises: ValueError when unknown pressure units are provided

        """
        pass

    def visibility(self, unit='meters'):
        """
        Returns a new value for visibility distance with specified unit

        :param unit: the unit of measure for the temperature values. May be:
            '*meters' (default), '*kilometers*', or '*miles*'
        :type unit: str
        :returns: a converted visibility distance value (float)
        :raises: ValueError when unknown visibility units are provided

        """
        pass

    def weather_icon_url(self, size=""):
        """Returns weather-related icon URL as a string.

        :param size: the size of the icon, normal (default, like the old ones), 2x or 4x
        :type size: str

        :returns: the icon URL.

        """
        pass

    def __repr__(self):
        return "<%s.%s - reference_time=%s, status=%s, detailed_status=%s>" % (
            __name__, self.__class__.__name__, self.reference_time('iso'), self.status.lower(),
            self.detailed_status.lower())

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses a *Weather* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *Weather* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the
            data needed to build the result, *APIResponseError* if the input dict embeds an HTTP status error

        """
        pass

    @classmethod
    def from_dict_of_lists(cls, the_dict):
        """
        Parses a list of *Weather* instances out of an input dict. Only certain properties of the data are used: if
        these properties are not found or cannot be parsed, an error is issued.

        :param the_dict: the input dict
        :type the_dict: dict
        :returns: a list of *Weather* instances or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the data needed to build the result,
            *APIResponseError* if the input dict an HTTP status error

        """
        pass

    def to_dict(self):
        """Dumps object to a dictionary

        :returns: a `dict`

        """
        pass
