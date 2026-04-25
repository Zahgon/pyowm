#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons.enums import ImageTypeEnum
from pyowm.commons.http_client import HttpClient
from pyowm.commons.image import Image
from pyowm.commons.tile import Tile
from pyowm.tiles.uris import ROOT_TILE_URL, NAMED_MAP_LAYER_URL


class TileManager:

    """
    A manager objects that reads OWM map layers tile images .

    :param API_key: the OWM Weather API key
    :type API_key: str
    :param map_layer: the layer for which you want tiles fetched. Allowed map layers are specified by
        the `pyowm.tiles.enum.MapLayerEnum` enumerator class.
    :type map_layer: str
    :param config: the configuration dictionary
    :type config: dict
    :returns: a *TileManager* instance
    :raises: *AssertionError* when no API Key or no map layer is provided, or map layer name is not a string

    """

    def __init__(self, API_key, map_layer, config):
        pass

    def get_tile(self, x, y, zoom):
        """
        Retrieves the tile having the specified coordinates and zoom level

        :param x: horizontal tile number in OWM tile reference system
        :type x: int
        :param y: vertical tile number in OWM tile reference system
        :type y: int
        :param zoom: zoom level for the tile
        :type zoom: int
        :returns: a `pyowm.tiles.Tile` instance

        """
        pass

    def __repr__(self):
        return "<%s.%s - layer_name=%s>" % (__name__, self.__class__.__name__, self.map_layer)
