#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons.databoxes import ImageType, SubscriptionType


class SubscriptionTypeEnum:
    """
    Allowed OpenWeatherMap subscription types

    """
    FREE = SubscriptionType('free', 'api', False)
    STARTUP = SubscriptionType('startup', 'api', True)
    DEVELOPER = SubscriptionType('developer', 'api', True)
    PROFESSIONAL = SubscriptionType('professional', 'api', True)
    ENTERPRISE = SubscriptionType('enterprise', 'api', True)

    @classmethod
    def lookup_by_name(cls, name):
        pass

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of `pyowm.commons.enums.SubscriptionType`

        """
        pass

    def __repr__(self):
        return "<%s.%s>" % (__name__, self.__class__.__name__)


class ImageTypeEnum:
    """
    Allowed image types on OWM APIs

    """
    PNG = ImageType('PNG', 'image/png')
    GEOTIFF = ImageType('GEOTIFF', 'image/tiff')

    @classmethod
    def lookup_by_mime_type(cls, mime_type):
        pass

    @classmethod
    def lookup_by_name(cls, name):
        pass

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of `pyowm.commons.enums.ImageType`

        """
        pass

    def __repr__(self):
        return "<%s.%s>" % (__name__, self.__class__.__name__)
