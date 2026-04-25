#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.alertapi30.alert import AlertChannel


class WeatherParametersEnum:
    """
    Allowed weather parameters for condition checking

    """
    TEMPERATURE = 'temp'  # Kelvin
    PRESSURE = 'pressure'
    HUMIDITY = 'humidity'
    WIND_SPEED = 'wind_speed'
    WIND_DIRECTION = 'wind_direction'
    CLOUDS = 'clouds'  # Coverage %

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of str

        """
        pass


class OperatorsEnum:
    """
    Allowed comparison operators for condition checking upon weather parameters

    """
    GREATER_THAN = '$gt'
    GREATER_THAN_EQUAL = '$gte'
    LESS_THAN = '$lt'
    LESS_THAN_EQUAL = '$lte'
    EQUAL = '$eq'
    NOT_EQUAL = '$ne'

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of str

        """
        pass


class AlertChannelsEnum:
    """
    Allowed alert channels

    """
    OWM_API_POLLING = AlertChannel('OWM API POLLING')

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of str

        """
        pass
