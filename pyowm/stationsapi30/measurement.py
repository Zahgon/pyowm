#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pyowm.commons import exceptions
from pyowm.utils import formatting


class AggregatedMeasurement:
    """
    A class representing an aggregation of measurements done by the Stations API
    on a specific time-frame. Values for the aggregation time-frame can be: 'm'
    (minute), 'h' (hour) or 'd' (day)

    :param station_id: unique station identifier
    :type station_id: str
    :param timestamp: reference UNIX timestamp for this measurement
    :type timestamp: int
    :param aggregated_on: aggregation time-frame for this measurement
    :type aggregated_on: string between 'm','h' and 'd'
    :param temp: optional dict containing temperature data
    :type temp: dict or `None`
    :param humidity: optional dict containing humidity data
    :type humidity: dict or `None`
    :param wind: optional dict containing wind data
    :type wind: dict or `None`
    :param pressure: optional dict containing pressure data
    :type pressure: dict or `None`
    :param precipitation: optional dict containing precipitation data
    :type precipitation: dict or `None`
    """

    ALLOWED_AGGREGATION_TIME_FRAMES = ['m', 'h', 'd']

    def __init__(self, station_id, timestamp, aggregated_on, temp=None,
                 humidity=None, wind=None, pressure=None, precipitation=None):
        pass

    def creation_time(self, timeformat='unix'):
        """Returns the UTC time of creation of this aggregated measurement

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
        Parses an *AggregatedMeasurement* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: an *AggregatedMeasurement* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the data needed to build the result

        """
        pass

    def to_dict(self):
        """Dumps object fields into a dict

        :returns: a dict

        """
        pass

    def __repr__(self):
        return '<%s.%s - station_id=%s, created_at=%s>' \
               % (__name__, self.__class__.__name__,
                  self.station_id, self.creation_time())


class Measurement:

    def __init__(self, station_id, timestamp, temperature=None, wind_speed=None,
                 wind_gust=None, wind_deg=None, pressure=None, humidity=None,
                 rain_1h=None, rain_6h=None, rain_24h=None, snow_1h=None,
                 snow_6h=None, snow_24h=None, dew_point=None, humidex=None,
                 heat_index=None, visibility_distance=None, visibility_prefix=None,
                 clouds_distance=None, clouds_condition=None, clouds_cumulus=None,
                 weather_precipitation=None, weather_descriptor=None,
                 weather_intensity=None, weather_proximity=None,
                 weather_obscuration=None, weather_other=None):
        pass

    def creation_time(self, timeformat='unix'):
        """Returns the UTC time of creation of this raw measurement

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
        pass

    def to_dict(self):
        """Dumps object fields into a dictionary

        :returns: a dict

        """
        pass

    def to_JSON(self):
        """Dumps object fields into a JSON formatted string

        :returns: the JSON string

        """
        pass

    def __repr__(self):
        return '<%s.%s - station_id=%s, created_at=%s>' \
               % (__name__, self.__class__.__name__,
                  self.station_id, self.creation_time())
