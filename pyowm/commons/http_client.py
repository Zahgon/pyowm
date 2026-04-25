#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from pyowm.commons import exceptions
from pyowm.commons.enums import ImageTypeEnum


class HttpRequestBuilder:

    URL_TEMPLATE_WITH_SUBDOMAINS = '{}://{}.{}/{}'
    URL_TEMPLATE_WITHOUT_SUBDOMAINS = '{}://{}/{}'

    """
    A stateful HTTP URL, params and headers builder with a fluent interface
    """
    def __init__(self, root_uri_token, api_key, config, has_subdomains=True):
        pass

    def _set_schema(self):
        pass

    def _set_subdomain(self):
        pass

    def _set_proxies(self):
        pass

    def with_path(self, path_uri_token):
        pass

    def with_headers(self, headers):
        pass

    def with_header(self, key, value):
        pass

    def with_query_params(self, query_params):
        pass

    def with_api_key(self):
        pass

    def with_language(self):
        pass

    def build(self):
        pass

    def __repr__(self):
        return "<%s.%s>" % (__name__, self.__class__.__name__)


class HttpClient:

    """
    An HTTP client encapsulating some config data and abstarcting away data raw retrieval

    :param api_key: the OWM API key
    :type api_key: str
    :param config: the configuration dictionary (if not provided, a default one will be used)
    :type config: dict
    :param root_uri: the root URI of the API endpoint
    :type root_uri: str
    :param admits_subdomains: if the root URI of the API endpoint admits subdomains based on the subcription type (default: True)
    :type admits_subdomains: bool
    """

    def __init__(self, api_key, config, root_uri, admits_subdomains=True):
        pass

    def get_json(self, path, params=None, headers=None):
        pass

    def get_png(self, path, params=None, headers=None):
        # check URL fromt the metaimage: if it looks like a complete URL, use that one (I know, it's a hack...)
        pass

    def get_geotiff(self, path, params=None, headers=None):
        # check URL fromt the metaimage: if it looks like a complete URL, use that one (I know, it's a hack...)
        pass

    def post(self, path, params=None, data=None, headers=None):
        pass

    def put(self, path, params=None, data=None, headers=None):
        pass

    def delete(self, path, params=None, data=None, headers=None):
        pass

    @classmethod
    def check_status_code(cls, status_code, payload):
        pass

    def __repr__(self):
        return "<%s.%s - root: %s>" % (__name__, self.__class__.__name__, self.root_uri)
