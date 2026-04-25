#!/usr/bin/env python
# -*- coding: utf-8 -*-"""

# Temperature conversion constants
KELVIN_OFFSET = 273.15
FAHRENHEIT_OFFSET = 32.0
FAHRENHEIT_DEGREE_SCALE = 1.8

# Wind speed conversion constants
MILES_PER_HOUR_FOR_ONE_METER_PER_SEC = 2.23694
KM_PER_HOUR_FOR_ONE_METER_PER_SEC = 3.6
KNOTS_FOR_ONE_METER_PER_SEC = 1.94384

# Barometric conversion constants
HPA_FOR_ONE_INHG = 33.8639

# Visibility distance conversion constants
MILE_FOR_ONE_METER = 0.000621371
KMS_FOR_ONE_METER = .001

# Decimal precision
ROUNDED_TO = 2


def kelvin_dict_to(d, target_temperature_unit):
    """
    Converts all the values in a dict from Kelvin temperatures to the
    specified temperature format.

    :param d: the dictionary containing Kelvin temperature values
    :type d: dict
    :param target_temperature_unit: the target temperature unit, may be:
        'celsius' or 'fahrenheit'
    :type target_temperature_unit: str
    :returns: a dict with the same keys as the input dict and converted
        temperature values as values
    :raises: *ValueError* when unknown target temperature units are provided

    """
    pass


def kelvin_to_celsius(kelvintemp):
    """
    Converts a numeric temperature from Kelvin degrees to Celsius degrees

    :param kelvintemp: the Kelvin temperature
    :type kelvintemp: int/long/float
    :returns: the float Celsius temperature
    :raises: *TypeError* when bad argument types are provided

    """
    pass


def kelvin_to_fahrenheit(kelvintemp):
    """
    Converts a numeric temperature from Kelvin degrees to Fahrenheit degrees

    :param kelvintemp: the Kelvin temperature
    :type kelvintemp: int/long/float
    :returns: the float Fahrenheit temperature

    :raises: *TypeError* when bad argument types are provided
    """
    pass


def metric_wind_dict_to_imperial(d):
    """
    Converts all the wind values in a dict from meters/sec (metric measurement
    system) to miles/hour (imperial measurement system)
    .

    :param d: the dictionary containing metric values
    :type d: dict
    :returns: a dict with the same keys as the input dict and values converted
        to miles/hour

    """
    pass


def metric_wind_dict_to_km_h(d):
    """
    Converts all the wind values in a dict from meters/sec
    to km/hour.

    :param d: the dictionary containing metric values
    :type d: dict
    :returns: a dict with the same keys as the input dict and values converted
        to km/hour

    """
    pass


def metric_wind_dict_to_knots(d):
    """
    Converts all the wind values in a dict from meters/sec
    to knots

    :param d: the dictionary containing metric values
    :type d: dict
    :returns: a dict with the same keys as the input dict and values converted
        to km/hour

    """
    pass


def metric_wind_dict_to_beaufort(d):
    """
    Converts all the wind values in a dict from meters/sec
    to the corresponding Beaufort scale level (which is not an exact number but rather
    represents a range of wind speeds - see: https://en.wikipedia.org/wiki/Beaufort_scale).
    Conversion table: https://www.windfinder.com/wind/windspeed.htm

    :param d: the dictionary containing metric values
    :type d: dict
    :returns: a dict with the same keys as the input dict and values converted
        to Beaufort level

    """
    pass


def metric_pressure_dict_to_inhg(d):
    """
    Converts all barometric pressure values in a dict to "inches of mercury."

    :param d: the dictionary containing metric values
    :type d: dict
    :returns: a dict with the same keys as the input dict and values converted
        to "Hg or inHg (inches of mercury)

    Note what OWM says about pressure: "Atmospheric pressure [is given in hPa]
    (on the sea level, if there is no sea_level or grnd_level data)"
    """
    pass


def visibility_distance_to(v, target_visibility_unit='kilometers'):
    """
    Converts visibility distance (in meters) to kilometers or miles
    Defaults to kilometer conversion

    :param distance: the value of visibility_distance
    :type distance: int
    :param target_visibility_unit: the unit of conversion
    :type target_visibility_unit: str
    :returns: a converted value for visibility_distance (float)
    """
    pass
