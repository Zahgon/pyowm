#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.alertapi30.condition import Condition
from pyowm.commons import exceptions
from pyowm.utils import formatting


class AlertChannel:
    """
    Base class representing a channel through which one can acknowledge that a weather alert has been issued.
    Examples: OWM API polling, push notifications, email notifications, etc.
    This feature is yet to be implemented by the OWM API.
    :param name: name of the channel
    :type name: str
    :returns: an *AlertChannel* instance

    """
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        pass

    def __repr__(self):
        return '<%s.%s - name: %s>' % (__name__, self.__class__.__name__, self.name)


class Alert:
    """
    Represents the situation happening when any of the conditions bound to a `Trigger` is met. Whenever this happens, an
    `Alert` object is created (or updated) and is bound to its parent `Trigger`. The trigger can then be polled to check
    what alerts have been fired on it.
    :param id: unique alert identifier
    :type name: str
    :param trigger_id: link back to parent `Trigger`
    :type trigger_id: str
    :param met_conditions: list of dict, each one referring to a `Condition` obj bound to the parent `Trigger` and reporting
    the actual measured values that made this `Alert` fire
    :type met_conditions: list of dict
    :param coordinates: dict representing the geocoordinates where the `Condition` triggering the `Alert` was met
    :type coordinates: dict
    :param last_update: epoch of the last time when this `Alert` has been fired
    :type last_update: int

    """
    def __init__(self, id, trigger_id, met_conditions, coordinates, last_update=None):
        pass

    @classmethod
    def from_dict(cls, the_dict):
        """
        Parses a *Alert* instance out of a data dictionary. Only certain properties of the data dictionary
        are used: if these properties are not found or cannot be parsed, an exception is issued.

        :param the_dict: the input dictionary
        :type the_dict: `dict`
        :returns: a *Alert* instance or ``None`` if no data is available
        :raises: *ParseAPIResponseError* if it is impossible to find or parse the data needed to build the result

        """
        pass

    def to_dict(self):
        """Dumps object to a dictionary

        :returns: a `dict`

        """
        pass

    def __repr__(self):
        return "<%s.%s - id=%s, trigger id=%s, last update=%s>" % (
            __name__,
            self.__class__.__name__,
            self.id,
            self.trigger_id,
            formatting.to_ISO8601(self.last_update))
