#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons.enums import ImageTypeEnum
from pyowm.commons.image import Image
from pyowm.commons.tile import Tile
from pyowm.utils import formatting


class MetaImage:
    """
    A class representing metadata for a satellite-acquired image

    :param url: the public URL of the image
    :type url: str
    :param preset: the preset of the image (supported values are listed by `pyowm.agroapi10.enums.PresetEnum`)
    :type preset: str
    :param satellite_name: the name of the satellite that acquired the image (supported values are listed
        by `pyowm.agroapi10.enums.SatelliteEnum`)
    :type satellite_name: str
    :param acquisition_time: the UTC Unix epoch when the image was acquired
    :type acquisition_time: int
    :param valid_data_percentage: approximate percentage of valid data coverage
    :type valid_data_percentage: float
    :param cloud_coverage_percentage: approximate percentage of cloud coverage on the scene
    :type cloud_coverage_percentage: float
    :param sun_azimuth: sun azimuth angle at scene acquisition time
    :type sun_azimuth: float
    :param sun_elevation: sun zenith angle at scene acquisition time
    :type sun_elevation: float
    :param polygon_id: optional id of the polygon the image refers to
    :type polygon_id: str
    :param stats_url: the public URL of the image statistics, if available
    :type stats_url: str or `None`
    :returns: an `MetaImage` object
    """

    image_type = None

    def __init__(self, url, preset, satellite_name, acquisition_time,
                 valid_data_percentage, cloud_coverage_percentage, sun_azimuth, sun_elevation, polygon_id=None,
                 stats_url=None):
        pass

    def acquisition_time(self, timeformat='unix'):
        """Returns the UTC time telling when the image data was acquired by the satellite

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str

        """
        pass

    def __repr__(self):
        return "<%s.%s - %s %s image acquired at %s by %s on polygon with id=%s>" % (
            __name__, self.__class__.__name__,
            self.image_type.name if self.image_type is not None else '',
            self.preset, self.acquisition_time('iso'), self.satellite_name,
            self.polygon_id if self.polygon_id is not None else 'None')


class MetaPNGImage(MetaImage):
    """
    Class representing metadata for a satellite image of a polygon in PNG format
    """
    image_type = ImageTypeEnum.PNG


class MetaTile(MetaImage):
    """
    Class representing metadata for a tile in PNG format
    """
    image_type = ImageTypeEnum.PNG


class MetaGeoTiffImage(MetaImage):
    """
    Class representing metadata for a satellite image of a polygon in GeoTiff format
    """
    image_type = ImageTypeEnum.GEOTIFF


class SatelliteImage:
    """
    Class representing a downloaded satellite image, featuring both metadata and data

    :param metadata: the metadata for this satellite image
    :type metadata: a `pyowm.agro10.imagery.MetaImage` subtype instance
    :param data: the actual data for this satellite image
    :type data: either `pyowm.commons.image.Image` or `pyowm.commons.tile.Tile` object
    :param downloaded_on: the UNIX epoch this satellite image was downloaded at
    :type downloaded_on: int or `None`
    :param palette: ID of the color palette of the downloaded images. Values are provided by `pyowm.agroapi10.enums.PaletteEnum`
    :type palette: str or `None`
    :returns: a `pyowm.agroapi10.imagery.SatelliteImage` instance
    """

    def __init__(self, metadata, data, downloaded_on=None, palette=None):
        pass

    def downloaded_on(self, timeformat='unix'):
        """Returns the UTC time telling when the satellite image was downloaded from the OWM Agro API

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str

        """
        pass

    def persist(self, path_to_file):
        """
        Saves the satellite image to disk on a file

        :param path_to_file: path to the target file
        :type path_to_file: str
        :return: `None`
        """
        pass

    def __repr__(self):
        return "<%s.%s - %s %s satellite image downloaded on: %s>" % (
            __name__, self.__class__.__name__,
            self.metadata.preset, self.metadata.satellite_name,
            self.downloaded_on('iso') if self._downloaded_on is not None else 'None')
