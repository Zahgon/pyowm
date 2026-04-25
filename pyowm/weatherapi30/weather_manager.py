#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone
from typing import Union

from pyowm.commons.http_client import HttpClient
from pyowm.constants import WEATHER_API_VERSION
from pyowm.utils import geo
from pyowm.weatherapi30 import forecaster, historian, observation, forecast, stationhistory, one_call
from pyowm.weatherapi30.uris import ROOT_WEATHER_API, OBSERVATION_URI, GROUP_OBSERVATIONS_URI, FIND_OBSERVATIONS_URI, \
    BBOX_CITY_URI, THREE_HOURS_FORECAST_URI, DAILY_FORECAST_URI, STATION_WEATHER_HISTORY_URI, ONE_CALL_URI, \
    ONE_CALL_HISTORICAL_URI, ONE_CALL_ROOT_URI


class WeatherManager:
    """
    A manager objects that provides a full interface to OWM Weather API.

    :param API_key: the OWM AirPollution API key
    :type API_key: str
    :param config: the configuration dictionary
    :type config: dict
    :returns: a *WeatherManager* instance
    :raises: *AssertionError* when no API Key is provided

    """

    def __init__(self, API_key, config):
        pass

    def weather_api_version(self):
        pass

    def weather_at_place(self, name):
        """
        Queries the OWM Weather API for the currently observed weather at the
        specified toponym (eg: "London,uk")

        :param name: the location's toponym
        :type name: str
        :returns: an *Observation* instance or ``None`` if no weather data is
            available
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed or *APICallException* when OWM Weather API can not be
            reached
        """

        pass

    def weather_at_coords(self, lat, lon):
        """
        Queries the OWM Weather API for the currently observed weather at the
        specified geographic (eg: 51.503614, -0.107331).

        :param lat: the location's latitude, must be between -90.0 and 90.0
        :type lat: int/float
        :param lon: the location's longitude, must be between -180.0 and 180.0
        :type lon: int/float
        :returns: an *Observation* instance or ``None`` if no weather data is
            available
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed or *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def weather_at_zip_code(self, zipcode, country):
        """
        Queries the OWM Weather API for the currently observed weather at the
        specified zip code and country code (eg: 2037, au).

        :param zip: the location's zip or postcode
        :type zip: string
        :param country: the location's country code
        :type country: string
        :returns: an *Observation* instance or ``None`` if no weather data is
            available
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed or *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def weather_at_id(self, id):
        """
        Queries the OWM Weather API for the currently observed weather at the
        specified city ID (eg: 5128581)

        :param id: the location's city ID
        :type id: int
        :returns: an *Observation* instance or ``None`` if no weather data is
            available
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed or *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def weather_at_ids(self, ids_list):
        """
        Queries the OWM Weather API for the currently observed weathers at the
        specified city IDs (eg: [5128581,87182])

        :param ids_list: the list of city IDs
        :type ids_list: list of int
        :returns: a list of *Observation* instances or an empty list if no
            weather data is available
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed or *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def weather_at_places(self, pattern, searchtype, limit=None):
        """
        Queries the OWM Weather API for the currently observed weather in all the
        locations whose name is matching the specified text search parameters.
        A twofold search can be issued: *'accurate'* (exact matching) and
        *'like'* (matches names that are similar to the supplied pattern).

        :param pattern: the string pattern (not a regex) to be searched for the
            toponym
        :type pattern: str
        :param searchtype: the search mode to be used, must be *'accurate'* for
          an exact matching or *'like'* for a likelihood matching
        :type: searchtype: str
        :param limit: the maximum number of *Observation* items in the returned
            list (default is ``None``, which stands for any number of items)
        :param limit: int or ``None``
        :returns: a list of *Observation* objects or ``None`` if no weather
            data is available
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached, *ValueError* when bad value is supplied for the search
            type or the maximum number of items retrieved
        """
        pass

    def weather_at_places_in_bbox(self, lon_left, lat_bottom, lon_right, lat_top,
                                  zoom=10, cluster=False):
        """
        Queries the OWM Weather API for the weather currently observed by
        meteostations inside the bounding box of latitude/longitude coords.

        :param lat_top: latitude for top margin of bounding box, must be
            between -90.0 and 90.0
        :type lat_top: int/float
        :param lon_left: longitude for left margin of bounding box
            must be between -180.0 and 180.0
        :type lon_left: int/float
        :param lat_bottom: latitude for the bottom margin of bounding box, must
            be between -90.0 and 90.0
        :type lat_bottom: int/float
        :param lon_right: longitude for the right margin of bounding box,
            must be between -180.0 and 180.0
        :type lon_right: int/float
        :param zoom: zoom level (defaults to: 10)
        :type zoom: int
        :param cluster: use server clustering of points
        :type cluster: bool
        :returns: a list of *Observation* objects or ``None`` if no weather
            data is available
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached, *ValueError* when coordinates values are out of bounds or
            negative values are provided for limit
        """
        pass

    def weather_around_coords(self, lat, lon, limit=None):
        """
        Queries the OWM Weather API for the currently observed weather in all the
        locations in the proximity of the specified coordinates.

        :param lat: location's latitude, must be between -90.0 and 90.0
        :type lat: int/float
        :param lon: location's longitude, must be between -180.0 and 180.0
        :type lon: int/float
        :param limit: the maximum number of *Observation* items in the returned
            list (default is ``None``, which stands for any number of items)
        :param limit: int or ``None``
        :returns: a list of *Observation* objects or ``None`` if no weather
            data is available
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached, *ValueError* when coordinates values are out of bounds or
            negative values are provided for limit
        """
        pass

    def forecast_at_place(self, name, interval, limit=None):
        """
        Queries the OWM Weather API for weather forecast for the
        specified location (eg: "London,uk") with the given time granularity.
        A *Forecaster* object is returned, containing a *Forecast*: this instance
        encapsulates *Weather* objects corresponding to the provided granularity.

        :param name: the location's toponym
        :type name: str
        :param interval: the granularity of the forecast, among `3h` and 'daily'
        :type interval: str among `3h` and 'daily'
        :param limit: the maximum number of *Weather* items to be retrieved
            (default is ``None``, which stands for any number of items)
        :type limit: int or ``None``
        :returns: a *Forecaster* instance or ``None`` if forecast data is not
            available for the specified location
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def forecast_at_coords(self, lat, lon, interval, limit=None):
        """
        Queries the OWM Weather API for weather forecast for the
        specified geographic coordinates with the given time granularity.
        A *Forecaster* object is returned, containing a *Forecast*: this instance
        encapsulates *Weather* objects corresponding to the provided granularity.

        :param lat: location's latitude, must be between -90.0 and 90.0
        :type lat: int/float
        :param lon: location's longitude, must be between -180.0 and 180.0
        :type lon: int/float
        :param interval: the granularity of the forecast, among `3h` and 'daily'
        :type interval: str among `3h` and 'daily'
        :param limit: the maximum number of *Weather* items to be retrieved
            (default is ``None``, which stands for any number of items)
        :type limit: int or ``None``
        :returns: a *Forecaster* instance or ``None`` if forecast data is not
            available for the specified location
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def forecast_at_id(self, id, interval, limit=None):
        """
        Queries the OWM Weather API for weather forecast for the
        specified city ID (eg: 5128581) with the given time granularity.
        A *Forecaster* object is returned, containing a *Forecast*: this instance
        encapsulates *Weather* objects corresponding to the provided granularity.

        :param id: the location's city ID
        :type id: int
        :param interval: the granularity of the forecast, among `3h` and 'daily'
        :type interval: str among `3h` and 'daily'
        :param limit: the maximum number of *Weather* items to be retrieved
            (default is ``None``, which stands for any number of items)
        :type limit: int or ``None``
        :returns: a *Forecaster* instance or ``None`` if forecast data is not
            available for the specified location
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def station_tick_history(self, station_ID, limit=None):
        """
        Queries the OWM Weather API for historic weather data measurements for the
        specified meteostation (eg: 2865), sampled once a minute (tick).
        A *StationHistory* object instance is returned, encapsulating the
        measurements: the total number of data points can be limited using the
        appropriate parameter

        :param station_ID: the numeric ID of the meteostation
        :type station_ID: int
        :param limit: the maximum number of data points the result shall
            contain (default is ``None``, which stands for any number of data
            points)
        :type limit: int or ``None``
        :returns: a *StationHistory* instance or ``None`` if data is not
            available for the specified meteostation
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached, *ValueError* if the limit value is negative

        """
        pass

    def station_hour_history(self, station_ID, limit=None):
        """
        Queries the OWM Weather API for historic weather data measurements for the
        specified meteostation (eg: 2865), sampled once a hour.
        A *Historian* object instance is returned, encapsulating a
        *StationHistory* objects which contains the measurements. The total
        number of retrieved data points can be limited using the appropriate
        parameter

        :param station_ID: the numeric ID of the meteostation
        :type station_ID: int
        :param limit: the maximum number of data points the result shall
            contain (default is ``None``, which stands for any number of data
            points)
        :type limit: int or ``None``
        :returns: a *Historian* instance or ``None`` if data is not
            available for the specified meteostation
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached, *ValueError* if the limit value is negative

        """
        pass

    def station_day_history(self, station_ID, limit=None):
        """
        Queries the OWM Weather API for historic weather data measurements for the
        specified meteostation (eg: 2865), sampled once a day.
        A *Historian* object instance is returned, encapsulating a
        *StationHistory* objects which contains the measurements. The total
        number of retrieved data points can be limited using the appropriate
        parameter

        :param station_ID: the numeric ID of the meteostation
        :type station_ID: int
        :param limit: the maximum number of data points the result shall
            contain (default is ``None``, which stands for any number of data
            points)
        :type limit: int or ``None``
        :returns: a *Historian* instance or ``None`` if data is not
            available for the specified meteostation
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached, *ValueError* if the limit value is negative

        """
        pass

    def _retrieve_station_history(self, station_ID, limit, interval):
        """
        Helper method for station_X_history functions.
        """
        pass

    def one_call(self, lat: Union[int, float], lon: Union[int, float], **kwargs) -> one_call.OneCall:
        """
        Queries the OWM Weather API with one call for current weather information and forecast for the
        specified geographic coordinates.
        One Call API provides the following weather data for any geographical coordinate:
        - Current weather
        - Hourly forecast for 48 hours
        - Daily forecast for 7 days

        A *OneCall* object is returned with the current data and the two forecasts.

        :param lat: location's latitude, must be between -90.0 and 90.0
        :type lat: int/float
        :param lon: location's longitude, must be between -180.0 and 180.0
        :type lon: int/float
        :returns: a *OneCall* instance or ``None`` if the data is not
            available for the specified location
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def one_call_history(self, lat: Union[int, float], lon: Union[int, float], dt: int = None):
        """
        Queries the OWM Weather API with one call for historical weather information for the
        specified geographic coordinates.

        A *OneCall* object is returned with the current data and the two forecasts.

        :param lat: location's latitude, must be between -90.0 and 90.0
        :type lat: int/float
        :param lon: location's longitude, must be between -180.0 and 180.0
        :type lon: int/float
        :param dt: timestamp from when the historical data starts. Cannot be less then now - 5 days.
                    Default = None means now - 5 days
        :type dt: int
        :returns: a *OneCall* instance or ``None`` if the data is not
            available for the specified location
        :raises: *ParseResponseException* when OWM Weather API responses' data
            cannot be parsed, *APICallException* when OWM Weather API can not be
            reached
        """
        pass

    def __repr__(self):
        return '<%s.%s>' % (__name__, self.__class__.__name__)
