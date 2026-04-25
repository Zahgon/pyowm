#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.airpollutionapi30.uris import CO_INDEX_URL, OZONE_URL, NO2_INDEX_URL, SO2_INDEX_URL, AIR_POLLUTION_URL, \
    AIR_POLLUTION_FORECAST_URL, AIR_POLLUTION_HISTORY_URL
from pyowm.utils import formatting


class AirPollutionHttpClient:

    """
    A class representing the OWM Air Pollution web API, which is a subset of the
    overall OWM API.

    :param API_key: a Unicode object representing the OWM Air Pollution web API key
    :type API_key: Unicode
    :param httpclient: an *httpclient.HttpClient* instance that will be used to \
         send requests to the OWM Air Pollution web API.
    :type httpclient: an *httpclient.HttpClient* instance

    """

    def __init__(self, API_key, httpclient):
        self._API_key = API_key
        self._client = httpclient

    def _trim_to(self, date_object, interval):
        pass

    def get_coi(self, params_dict):
        """
        Invokes the CO Index endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def get_o3(self, params_dict):
        """
        Invokes the O3 Index endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def get_no2(self, params_dict):
        """
        Invokes the NO2 Index endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def get_so2(self, params_dict):
        """
        Invokes the SO2 Index endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def get_air_pollution(self, params_dict):
        """
        Invokes the new AirPollution API endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def get_forecast_air_pollution(self, params_dict):
        """
        Invokes the new AirPollution API forecast endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def get_historical_air_pollution(self, params_dict):
        """
        Invokes the new AirPollution API history endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def __repr__(self):
        return "<%s.%s - httpclient=%s>" % \
               (__name__, self.__class__.__name__, str(self._client))