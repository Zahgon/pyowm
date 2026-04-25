#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.utils import formatting, measurables


class Soil:

    """
    Soil data over a specific Polygon

    :param reference_time: UTC UNIX time of soil data measurement
    :type reference_time: int
    :param surface_temp: soil surface temperature in Kelvin degrees
    :type surface_temp: float
    :param ten_cm_temp: soil temperature at 10 cm depth in Kelvin degrees
    :type ten_cm_temp: float
    :param moisture: soil moisture in m^3/m^3
    :type moisture: float
    :param polygon_id: ID of the polygon this soil data was measured upon
    :type polygon_id: str
    :returns: a `Soil` instance
    :raises: `AssertionError` when any of the mandatory fields is `None` or has wrong type
    """

    def __init__(self, reference_time, surface_temp, ten_cm_temp, moisture, polygon_id=None):
        pass

    def reference_time(self, timeformat='unix'):
        """Returns the UTC time telling when the soil data was measured

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str

        """
        pass

    def surface_temp(self, unit='kelvin'):
        """Returns the soil surface temperature

        :param unit: the unit of measure for the temperature value. May be:
            '*kelvin*' (default), '*celsius*' or '*fahrenheit*'
        :type unit: str
        :returns: a float
        :raises: ValueError when unknown temperature units are provided

        """
        pass

    def ten_cm_temp(self, unit='kelvin'):
        """Returns the soil temperature measured 10 cm below surface

        :param unit: the unit of measure for the temperature value. May be:
            '*kelvin*' (default), '*celsius*' or '*fahrenheit*'
        :type unit: str
        :returns: a float
        :raises: ValueError when unknown temperature units are provided

        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        pass

    def to_dict(self):
        pass

    def __repr__(self):
        return "<%s.%s - polygon_id=%s,reference time=%s,>" % (__name__, self.__class__.__name__,
                                                               self.polygon_id, self.reference_time('iso'))
