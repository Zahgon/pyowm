from typing import Union, Optional, List

from pyowm.commons import exceptions
from pyowm.utils import geo
from pyowm.weatherapi30.weather import Weather
from pyowm.weatherapi30.national_weather_alert import NationalWeatherAlert


class OneCall:

    def __init__(self,
                 lat: Union[int, float],
                 lon: Union[int, float],
                 timezone: str,
                 current: Weather,
                 forecast_minutely: Optional[List[Weather]] = None,
                 forecast_hourly: Optional[List[Weather]] = None,
                 forecast_daily: Optional[List[Weather]] = None,
                 national_weather_alerts: Optional[list] = None
                 ) -> None:
        pass

    def __repr__(self):
        return "<%s.%s - lat=%s, lon=%s, retrieval_time=%s>" % (
            __name__, self.__class__.__name__, self.lat, self.lon,
            self.current.reference_time() if self.current else None)

    def to_geopoint(self):
        """
        Returns the geoJSON compliant representation of the place for this One Call

        :returns: a ``pyowm.utils.geo.Point`` instance

        """
        pass


    @classmethod
    def from_dict(cls, the_dict: dict):
        """
        Parses a *OneCall* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *OneCall* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the
            data needed to build the result, *APIResponseError* if the input dict embeds an HTTP status error

        """

        pass
