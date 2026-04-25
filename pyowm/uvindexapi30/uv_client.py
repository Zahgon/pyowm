#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.uvindexapi30.uris import UV_INDEX_URL, UV_INDEX_FORECAST_URL, \
    UV_INDEX_HISTORY_URL


class UltraVioletHttpClient:

    """
    An HTTP client class for the OWM UV web API, which is a subset of the
    overall OWM API.

    :param API_key: a Unicode object representing the OWM UV web API key
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

    def get_uvi(self, params_dict):
        """
        Invokes the UV Index endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def get_uvi_forecast(self, params_dict):
        """
        Invokes the UV Index Forecast endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def get_uvi_history(self, params_dict):
        """
        Invokes the UV Index History endpoint

        :param params_dict: dict of parameters
        :returns: a string containing raw JSON data
        :raises: *ValueError*, *APIRequestError*

        """
        pass

    def __repr__(self):
        return "<%s.%s - httpclient=%s>" % \
               (__name__, self.__class__.__name__, str(self._client))