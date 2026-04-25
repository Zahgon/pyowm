#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons.databoxes import Satellite


class PresetEnum:
    """
    Allowed presets for satellite images on Agro API 1.0

    """
    TRUE_COLOR = 'truecolor'
    FALSE_COLOR = 'falsecolor'
    NDVI = 'ndvi'
    EVI = 'evi'

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of str

        """
        pass

    def __repr__(self):
        return '<%s.%s>' % (__name__, self.__class__.__name__)


class SatelliteEnum:
    """
    Allowed presets for satellite names on Agro API 1.0

    """
    LANDSAT_8 = Satellite('Landsat 8', 'l8')
    SENTINEL_2 = Satellite('Sentinel-2', 's2')

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of str

        """
        pass

    def __repr__(self):
        return '<%s.%s>' % (__name__, self.__class__.__name__)


class PaletteEnum:
    """
    Allowed color palettes for satellite images on Agro API 1.0

    """
    GREEN = '1'   # default Agro API 1.0 palette
    BLACK_AND_WHITE = '2'
    CONTRAST_SHIFTED = '3'
    CONTRAST_CONTINUOUS = '4'

    @classmethod
    def items(cls):
        """
        All values for this enum
        :return: list of str

        """
        pass

    def __repr__(self):
        return '<%s.%s>' % (__name__, self.__class__.__name__)