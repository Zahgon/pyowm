#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.alertapi30.alert import Alert
from pyowm.alertapi30.trigger import Trigger
from pyowm.alertapi30.uris import ROOT_ALERT_API_URL, TRIGGERS_URI, NAMED_TRIGGER_URI, ALERTS_URI, NAMED_ALERT_URI
from pyowm.commons.http_client import HttpClient
from pyowm.constants import ALERT_API_VERSION
from pyowm.utils import formatting, timestamps


class AlertManager:

    """
    A manager objects that provides a full interface to OWM Alert API. It implements CRUD methods on Trigger entities
    and read/deletion of related Alert objects

    :param API_key: the OWM Weather API key
    :type API_key: str
    :param config: the configuration dictionary
    :type config: dict
    :returns: an *AlertManager* instance
    :raises: *AssertionError* when no API Key is provided

    """

    def __init__(self, API_key, config):
        pass

    def alert_api_version(self):
        pass

    # TRIGGER methods

    def create_trigger(self,  start, end, conditions, area, alert_channels=None):
        """
        Create a new trigger on the Alert API with the given parameters
        :param start: time object representing the time when the trigger begins to be checked
        :type start: int, ``datetime.datetime`` or ISO8601-formatted string
        :param end: time object representing the time when the trigger ends to be checked
        :type end: int, ``datetime.datetime`` or ISO8601-formatted string
        :param conditions: the `Condition` objects representing the set of checks to be done on weather variables
        :type conditions: list of `pyowm.utils.alertapi30.Condition` instances
        :param area: the geographic are over which conditions are checked: it can be composed by multiple geoJSON types
        :type area: list of geoJSON types
        :param alert_channels: the alert channels through which alerts originating from this `Trigger` can be consumed.
        Defaults to OWM API polling
        :type alert_channels: list of `pyowm.utils.alertapi30.AlertChannel` instances
        :returns:  a *Trigger* instance
        :raises: *ValueError* when start or end epochs are `None` or when end precedes start or when conditions or area
        are empty collections
        """
        pass

    def get_triggers(self):
        """
        Retrieves all of the user's triggers that are set on the Weather Alert API.

        :returns: list of `pyowm.alertapi30.trigger.Trigger` objects

        """
        pass

    def get_trigger(self, trigger_id):
        """
        Retrieves the named trigger from the Weather Alert API.

        :param trigger_id: the ID of the trigger
        :type trigger_id: str
        :return: a `pyowm.alertapi30.trigger.Trigger` instance
        """
        pass

    def update_trigger(self, trigger):
        """
        Updates on the Alert API the trigger record having the ID of the specified Trigger object: the remote record is
        updated with data from the local Trigger object.

        :param trigger: the Trigger with updated data
        :type trigger: `pyowm.alertapi30.trigger.Trigger`
        :return: ``None`` if update is successful, an error otherwise
        """
        pass

    def delete_trigger(self, trigger):
        """
        Deletes from the Alert API the trigger record identified by the ID of the provided
        `pyowm.alertapi30.trigger.Trigger`, along with all related alerts

        :param trigger: the `pyowm.alertapi30.trigger.Trigger` object to be deleted
        :type trigger: `pyowm.alertapi30.trigger.Trigger`
        :returns: `None` if deletion is successful, an exception otherwise
        """
        pass

    # ALERTS methods

    def get_alerts_for(self, trigger):
        """
        Retrieves all of the alerts that were fired for the specified Trigger
        :param trigger: the trigger
        :type trigger: `pyowm.alertapi30.trigger.Trigger`
        :return: list of `pyowm.alertapi30.alert.Alert` objects
        """
        pass

    def get_alert(self, alert_id, trigger):
        """
        Retrieves info about the alert record on the Alert API that has the specified ID and belongs to the specified
        parent Trigger object
        :param trigger: the parent trigger
        :type trigger: `pyowm.alertapi30.trigger.Trigger`
        :param alert_id: the ID of the alert
        :type alert_id `pyowm.alertapi30.alert.Alert`
        :return: an `pyowm.alertapi30.alert.Alert` instance
        """
        pass

    def delete_all_alerts_for(self, trigger):
        """
        Deletes all of the alert that were fired for the specified Trigger
        :param trigger: the trigger whose alerts are to be cleared
        :type trigger: `pyowm.alertapi30.trigger.Trigger`
        :return: `None` if deletion is successful, an exception otherwise
        """
        pass

    def delete_alert(self, alert):
        """
        Deletes the specified alert from the Alert API
        :param alert: the alert to be deleted
        :type alert: pyowm.alertapi30.alert.Alert`
        :return: ``None`` if the deletion was successful, an error otherwise
        """
        pass

    def __repr__(self):
        return '<%s.%s>' % (__name__, self.__class__.__name__)