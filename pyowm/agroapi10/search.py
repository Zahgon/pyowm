#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.agroapi10.enums import PresetEnum
from pyowm.agroapi10.imagery import MetaPNGImage, MetaTile, MetaGeoTiffImage
from pyowm.commons.databoxes import ImageType
from pyowm.utils import formatting


class SatelliteImagerySearchResultSet:
    """
    Class representing a filterable result set by a satellite imagery search against the Agro API 1.0. Each result
    is a `pyowm.agroapi10.imagery.MetaImage` subtype instance

    """

    def __init__(self, polygon_id, list_of_dict, query_timestamp):
        """
        Parses raw data dict into a list of `pyowm.agroapi10.imagery.MetaImage` subtypes instances and stores that
        list internally for further filtering

        :param polygon_id: the ID of the polygon that has been searched for images
        :type polygon_id: str
        :param list_of_dict: the input data dictionary
        :type list_of_dict: list
        :param query_timestamp: UNIX timestamp of the query
        :type query_timestamp: int
        :returns: a `pyowm.agroapi10.imagery.SatelliteImagerySearchResultSet` instance or an exception is parsing fails

        """
        pass

    def issued_on(self, timeformat='unix'):
        """Returns the UTC time telling when the query was performed against the OWM Agro API

        :param timeformat: the format for the time value. May be:
            '*unix*' (default) for UNIX time
            '*iso*' for ISO8601-formatted string in the format ``YYYY-MM-DD HH:MM:SS+00``
            '*date* for ``datetime.datetime`` object instance
        :type timeformat: str
        :returns: an int or a str

        """
        pass

    def __len__(self):
        return len(self.metaimages)

    def __repr__(self):
        return '<%s.%s - %s results for query issued on polygon_id=%s at %s>' % (
            __name__, self.__class__.__name__,
            len(self), self.polygon_id, self.issued_on(timeformat='iso'))

    def all(self):
        """
        Returns all search results

        :returns: a list of `pyowm.agroapi10.imagery.MetaImage` instances

        """
        pass

    def with_img_type(self, image_type):
        """
        Returns the search results having the specified image type

        :param image_type: the desired image type (valid values are provided by the
            `pyowm.commons.enums.ImageTypeEnum` enum)
        :type image_type: `pyowm.commons.databoxes.ImageType` instance
        :returns: a list of `pyowm.agroapi10.imagery.MetaImage` instances

        """
        pass

    def with_preset(self, preset):
        """
        Returns the search results having the specified preset

        :param preset: the desired image preset (valid values are provided by the
            `pyowm.agroapi10.enums.PresetEnum` enum)
        :type preset: str
        :returns: a list of `pyowm.agroapi10.imagery.MetaImage` instances

        """
        pass

    def with_img_type_and_preset(self, image_type, preset):
        """
        Returns the search results having both the specified image type and preset

        :param image_type: the desired image type (valid values are provided by the
            `pyowm.commons.enums.ImageTypeEnum` enum)
        :type image_type: `pyowm.commons.databoxes.ImageType` instance
        :param preset: the desired image preset (valid values are provided by the
            `pyowm.agroapi10.enums.PresetEnum` enum)
        :type preset: str
        :returns: a list of `pyowm.agroapi10.imagery.MetaImage` instances

        """
        pass
