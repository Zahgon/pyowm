#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons import exceptions


def status_is(weather, status, weather_code_registry):
    """
    Checks if the weather status code of a *Weather* object corresponds to the
    detailed status indicated. The lookup is performed against the provided 
    *WeatherCodeRegistry* object.

    :param weather: the *Weather* object whose status code is to be checked
    :type weather: *Weather*
    :param status: a string indicating a detailed weather status
    :type status: str
    :param weather_code_registry: a *WeatherCodeRegistry* object
    :type weather_code_registry: *WeatherCodeRegistry*
    :returns: ``True`` if the check is positive, ``False`` otherwise

    """
    pass


def any_status_is(weather_list, status, weather_code_registry):
    """
    Checks if the weather status code of any of the *Weather* objects in the
    provided list corresponds to the detailed status indicated. The lookup is
    performed against the provided *WeatherCodeRegistry* object.

    :param weathers: a list of *Weather* objects
    :type weathers: list
    :param status: a string indicating a detailed weather status
    :type status: str
    :param weather_code_registry: a *WeatherCodeRegistry* object
    :type weather_code_registry: *WeatherCodeRegistry*
    :returns: ``True`` if the check is positive, ``False`` otherwise
    
    """
    pass


def filter_by_status(weather_list, status, weather_code_registry):
    """
    Filters out from the provided list of *Weather* objects a sublist of items
    having a status corresponding to the provided one. The lookup is performed
    against the provided *WeatherCodeRegistry* object.

    :param weathers: a list of *Weather* objects
    :type weathers: list
    :param status: a string indicating a detailed weather status
    :type status: str
    :param weather_code_registry: a *WeatherCodeRegistry* object
    :type weather_code_registry: *WeatherCodeRegistry*
    :returns: ``True`` if the check is positive, ``False`` otherwise
    
    """
    pass


def is_in_coverage(unixtime, weathers_list):
    """
    Checks if the supplied UNIX time is contained into the time range
    (coverage) defined by the most ancient and most recent *Weather* objects
    in the supplied list

    :param unixtime: the UNIX time to be searched in the time range
    :type unixtime: int
    :param weathers_list: the list of *Weather* objects to be scanned for
        global time coverage
    :type weathers_list: list
    :returns: ``True`` if the UNIX time is contained into the time range,
        ``False`` otherwise
    """
    pass


def find_closest_weather(weathers_list, unixtime):
    """
    Extracts from the provided list of Weather objects the item which is
    closest in time to the provided UNIXtime.

    :param weathers_list: a list of *Weather* objects
    :type weathers_list: list
    :param unixtime: a UNIX time
    :type unixtime: int
    :returns: the *Weather* object which is closest in time or ``None`` if the
        list is empty
    """
    pass
