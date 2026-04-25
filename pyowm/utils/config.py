#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from pyowm.commons import exceptions
from pyowm.config import DEFAULT_CONFIG
from pyowm.commons.enums import SubscriptionTypeEnum


def get_config_from(path_to_file):
    """
    Loads configuration data from the supplied file and returns it.

    :param path_to_file: path to the configuration file
    :type path_to_file: str
    :returns: the configuration `dict`
    :raises: `ConfigurationNotFoundError` when the supplied filepath is not a regular file; `ConfigurationParseError`
        when the supplied file cannot be parsed
    """
    pass


def get_default_config():
    """
    Returns the default PyOWM configuration.

    :returns: the configuration `dict`
    """
    pass


def get_default_config_for_subscription_type(name):
    """
    Returns the PyOWM configuration for a specific OWM API Plan subscription type

    :param name: name of the subscription type
    :type name: str
    :returns: the configuration `dict`
    """
    pass


def get_default_config_for_proxy(http_url, https_url):
    """
    Returns the PyOWM configuration to be used behind a proxy server

    :param http_url: URL connection string for HTTP protocol
    :type http_url: str
    :param https_url: URL connection string for HTTPS protocol
    :type https_url: str
    :returns: the configuration `dict`
    """
    pass
