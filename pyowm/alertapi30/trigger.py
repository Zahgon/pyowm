#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyowm.commons.exceptions
from pyowm.alertapi30.alert import Alert
from pyowm.alertapi30.condition import Condition
from pyowm.alertapi30.enums import AlertChannelsEnum
from pyowm.utils import formatting
from pyowm.utils.geo import GeometryBuilder


class Trigger:
    """
    Object representing a the check if a set of weather conditions are met on a given geographical area: each condition
    is a rule on the value of a given weather parameter (eg. humidity, temperature, etc). Whenever a condition from a
    `Trigger` is met, the OWM API crates an alert and binds it to the the `Trigger`.
    A `Trigger` is the local proxy for the corresponding entry on the OWM API, therefore it can get ouf of sync as
    time goes by and conditions are met: it's up to you to "refresh" the local trigger by using a
    `pyowm.utils.alertapi30.AlertManager` instance.
    :param start_after_millis: how many milliseconds after the trigger creation the trigger begins to be checked
    :type start_after_millis: int
    :param end_after_millis: how many milliseconds after the trigger creation the trigger ends to be checked
    :type end_after_millis: int
    :param alerts: the `Alert` objects representing the alerts that have been fired for this `Trigger` so far. Defaults
    to `None`
    :type alerts: list of `pyowm.utils.alertapi30.Alert` instances
    :param conditions: the `Condition` objects representing the set of checks to be done on weather variables
    :type conditions: list of `pyowm.utils.alertapi30.Condition` instances
    :param area: the geographic are over which conditions are checked: it can be composed by multiple geoJSON types
    :type area: list of geoJSON types
    :param alert_channels: the alert channels through which alerts originating from this `Trigger` can be consumed.
    Defaults to OWM API polling
    :type alert_channels: list of `pyowm.utils.alertapi30.AlertChannel` instances
    :param id: optional unique ID for this `Trigger` instance
    :type id: str
    :returns:  a *Trigger* instance
    :raises: *ValueError* when start or end epochs are `None` or when end precedes start or when conditions or area
    are empty collections

    """
    def __init__(self, start_after_millis, end_after_millis, conditions, area, alerts=None, alert_channels=None, id=None):
        pass

    def get_alerts(self):
        """
        Returns all of the alerts for this `Trigger`
        :return: a list of `Alert` objects
        """
        pass

    def get_alert(self, alert_id):
        """
        Returns the `Alert` of this `Trigger` having the specified ID
        :param alert_id: str, the ID of the alert
        :return: `Alert` instance
        """
        pass

    def get_alerts_since(self, timestamp):
        """
        Returns all the `Alert` objects of this `Trigger` that were fired since the specified timestamp.
        :param timestamp: time object representing the point in time since when alerts have to be fetched
        :type timestamp: int, ``datetime.datetime`` or ISO8601-formatted string
        :return: list of `Alert` instances
        """
        pass

    def get_alerts_on(self, weather_param):
        """
        Returns all the `Alert` objects of this `Trigger` that refer to the specified weather parameter (eg. 'temp',
        'pressure', etc.). The allowed weather params are the ones enumerated by class
        `pyowm.alertapi30.enums.WeatherParametersEnum`
        :param weather_param: str, values in `pyowm.alertapi30.enums.WeatherParametersEnum`
        :return: list of `Alert` instances
        """
        pass

    @classmethod
    def from_dict(cls, the_dict):
        pass

    def to_dict(self):
        pass

    def __repr__(self):
        return "<%s.%s - id=%s, start_after_mills=%s, end_after_mills=%s, alerts=%s>" % (
                    __name__,
                    self.__class__.__name__,
                    self.id if self.id is not None else 'None',
                    self.start_after_millis,
                    self.end_after_millis,
                    str(len(self.alerts)))
