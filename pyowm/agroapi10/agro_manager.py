#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.agroapi10.enums import PresetEnum, PaletteEnum
from pyowm.agroapi10.imagery import MetaTile, MetaGeoTiffImage, MetaPNGImage, SatelliteImage
from pyowm.agroapi10.polygon import Polygon, GeoPolygon
from pyowm.agroapi10.search import SatelliteImagerySearchResultSet
from pyowm.agroapi10.soil import Soil
from pyowm.agroapi10.uris import ROOT_AGRO_API, ROOT_DOWNLOAD_PNG_API, ROOT_DOWNLOAD_GEOTIFF_API, POLYGONS_URI, \
    NAMED_POLYGON_URI, SOIL_URI, SATELLITE_IMAGERY_SEARCH_URI
from pyowm.commons.http_client import HttpClient
from pyowm.commons.image import Image
from pyowm.commons.tile import Tile
from pyowm.constants import AGRO_API_VERSION
from pyowm.utils import timestamps


class AgroManager:

    """
    A manager objects that provides a full interface to OWM Agro API.

    :param API_key: the OWM Weather API key
    :type API_key: str
    :param config: the configuration dictionary
    :type config: dict
    :returns: an `AgroManager` instance
    :raises: `AssertionError` when no API Key is provided

    """

    def __init__(self, API_key, config):
        assert isinstance(API_key, str), 'You must provide a valid API Key'
        self.API_key = API_key
        assert isinstance(config, dict)
        self.http_client = HttpClient(API_key, config, ROOT_AGRO_API)
        self.geotiff_downloader_http_client = HttpClient(self.API_key, config, ROOT_DOWNLOAD_GEOTIFF_API)
        self.png_downloader_http_client = HttpClient(self.API_key, config, ROOT_DOWNLOAD_PNG_API)

    def agro_api_version(self):
        pass

    # POLYGON API subset methods

    def create_polygon(self, geopolygon, name=None):
        """
        Create a new polygon on the Agro API with the given parameters

        :param geopolygon: the geopolygon representing the new polygon
        :type geopolygon: `pyowm.utils.geo.Polygon` instance
        :param name: optional mnemonic name for the new polygon
        :type name: str
        :return: a `pyowm.agro10.polygon.Polygon` instance
        """
        pass

    def get_polygons(self):
        """
        Retrieves all of the user's polygons registered on the Agro API.

        :returns: list of `pyowm.agro10.polygon.Polygon` objects

        """
        pass

    def get_polygon(self, polygon_id):
        """
        Retrieves a named polygon registered on the Agro API.

        :param id: the ID of the polygon
        :type id: str
        :returns: a `pyowm.agro10.polygon.Polygon` object

        """
        pass

    def update_polygon(self, polygon):
        """
        Updates on the Agro API the Polygon identified by the ID of the provided polygon object.
        Currently this only changes the mnemonic name of the remote polygon

        :param polygon: the `pyowm.agro10.polygon.Polygon` object to be updated
        :type polygon: `pyowm.agro10.polygon.Polygon` instance
        :returns: `None` if update is successful, an exception otherwise
        """
        pass

    def delete_polygon(self, polygon):
        """
        Deletes on the Agro API the Polygon identified by the ID of the provided polygon object.

        :param polygon: the `pyowm.agro10.polygon.Polygon` object to be deleted
        :type polygon: `pyowm.agro10.polygon.Polygon` instance
        :returns: `None` if deletion is successful, an exception otherwise
        """
        pass

    # SOIL API subset methods

    def soil_data(self, polygon):
        """
        Retrieves the latest soil data on the specified polygon

        :param polygon: the reference polygon you want soil data for
        :type polygon: `pyowm.agro10.polygon.Polygon` instance
        :returns: a `pyowm.agro10.soil.Soil` instance

        """
        pass

    # Satellite Imagery subset methods

    def search_satellite_imagery(self, polygon_id, acquired_from, acquired_to, img_type=None, preset=None,
                                 min_resolution=None, max_resolution=None, acquired_by=None, min_cloud_coverage=None,
                                 max_cloud_coverage=None, min_valid_data_coverage=None, max_valid_data_coverage=None):
        """
        Searches on the Agro API the metadata for all available satellite images that contain the specified polygon and
        acquired during the specified time interval; and optionally matching the specified set of filters:
        - image type (eg. GeoTIF)
        - image preset (eg. false color, NDVI, ...)
        - min/max acquisition resolution
        - acquiring satellite
        - min/max cloud coverage on acquired scene
        - min/max valid data coverage on acquired scene

        :param polygon_id: the ID of the reference polygon
        :type polygon_id: str
        :param acquired_from: lower edge of acquisition interval, UNIX timestamp
        :type acquired_from: int
        :param acquired_to: upper edge of acquisition interval, UNIX timestamp
        :type acquired_to: int
        :param img_type: the desired file format type of the images. Allowed values are given by `pyowm.commons.enums.ImageTypeEnum`
        :type img_type: `pyowm.commons.databoxes.ImageType`
        :param preset: the desired preset of the images. Allowed values are given by `pyowm.agroapi10.enums.PresetEnum`
        :type preset: str
        :param min_resolution: minimum resolution for images, px/meters
        :type min_resolution: int
        :param max_resolution: maximum resolution for images, px/meters
        :type max_resolution: int
        :param acquired_by: short symbol of the satellite that acquired the image (eg. "l8")
        :type acquired_by: str
        :param min_cloud_coverage: minimum cloud coverage percentage on acquired images
        :type min_cloud_coverage: int
        :param max_cloud_coverage: maximum cloud coverage percentage on acquired images
        :type max_cloud_coverage: int
        :param min_valid_data_coverage: minimum valid data coverage percentage on acquired images
        :type min_valid_data_coverage: int
        :param max_valid_data_coverage: maximum valid data coverage percentage on acquired images
        :type max_valid_data_coverage: int
        :return: a list of `pyowm.agro10.imagery.MetaImage` subtypes instances
        """
        pass

    def download_satellite_image(self, metaimage, x=None, y=None, zoom=None, palette=None):
        """
        Downloads the satellite image described by the provided metadata. In case the satellite image is a tile, then
        tile coordinates and zoom must be provided. An optional palette ID can be provided, if supported by the
        downloaded preset (currently only NDVI is supported)

        :param metaimage: the satellite image's metadata, in the form of a `MetaImage` subtype instance
        :type metaimage: a `pyowm.agroapi10.imagery.MetaImage` subtype
        :param x: x tile coordinate (only needed in case you are downloading a tile image)
        :type x: int or `None`
        :param y: y tile coordinate (only needed in case you are downloading a tile image)
        :type y: int or `None`
        :param zoom: zoom level (only needed in case you are downloading a tile image)
        :type zoom: int or `None`
        :param palette: ID of the color palette of the downloaded images. Values are provided by `pyowm.agroapi10.enums.PaletteEnum`
        :type palette: str or `None`
        :return: a `pyowm.agroapi10.imagery.SatelliteImage` instance containing both image's metadata and data
        """
        pass

    def stats_for_satellite_image(self, metaimage):
        """
        Retrieves statistics for the satellite image described by the provided metadata.
        This is currently only supported 'EVI' and 'NDVI' presets

        :param metaimage: the satellite image's metadata, in the form of a `MetaImage` subtype instance
        :type metaimage: a `pyowm.agroapi10.imagery.MetaImage` subtype
        :return: dict
        """
        pass

    # Utilities
    def _fill_url(self, url_template, x, y, zoom):
        pass

    def __repr__(self):
        return '<%s.%s>' % (__name__, self.__class__.__name__)
