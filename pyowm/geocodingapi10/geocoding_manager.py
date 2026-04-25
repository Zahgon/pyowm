from pyowm.commons.http_client import HttpClient
from pyowm.commons.uris import ROOT_GEOCODING_API_URL, DIRECT_GEOCODING_URI, REVERSE_GEOCODING_URI
from pyowm.constants import GEOCODING_API_VERSION
from pyowm.utils import geo
from pyowm.weatherapi30.location import Location


class GeocodingManager:

    """
    A manager objects that provides a full interface to OWM Geocoding API.

    :param API_key: the OWM API key
    :type API_key: str
    :param config: the configuration dictionary
    :type config: dict
    :returns: an *GeocodingManager* instance
    :raises: *AssertionError* when no API Key is provided

    """

    def __init__(self, API_key, config):
        pass

    def geocoding_api_version(self):
        pass

    def geocode(self, toponym, country=None, state_code=None, limit=None):
        """
        Invokes the direct geocoding API endpoint

        :param toponym: the name of the location
        :type toponym: `str`
        :param country: the 2-chars ISO symbol of the country
        :type country: `str` or `None`
        :param state_code: the 2-chars ISO symbol of state (only useful in case the country is US)
        :type state_code: `str` or `None`
        :param limit: the max number of results to be returned in case of multiple matchings (no limits by default)
        :type limit: `int` or `None`
        :returns: a list of *Location* instances
        :raises: *AssertionError*, *ValueError*, *APIRequestError*

        """
        pass

    def reverse_geocode(self, lat, lon, limit=None):
        pass

    def __repr__(self):
        return '<%s.%s>' % (__name__, self.__class__.__name__)