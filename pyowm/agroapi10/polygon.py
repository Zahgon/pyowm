#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.utils.geo import GeometryBuilder
from pyowm.utils.geo import Point as GeoPoint
from pyowm.utils.geo import Polygon as GeoPolygon


class Polygon:

    """
    A Polygon feature, foundational element for all Agro API operations

    :param id: the polygon's ID
    :type id: str
    :param name: the polygon's name
    :type namr: str
    :param geopolygon: the `pyowm.utils.geo.Polygon` instance that represents this polygon
    :type geopolygon: `pyowm.utils.geo.Polygon`
    :param center: the `pyowm.utils.geo.Point` instance that represents the central point of the polygon
    :type center: `pyowm.utils.geo.Point`
    :param area: the area of the polygon in hectares
    :type area: float or int
    :param user_id: the ID of the user owning this polygon
    :type user_id: str
    :returns: a `Polygon` instance
    :raises: `AssertionError` when either id is `None` or geopolygon, center or area have wrong type
    """

    def __init__(self, id, name=None, geopolygon=None, center=None, area=None, user_id=None):

        pass

    @property
    def area_km(self):
        pass

    @classmethod
    def from_dict(cls, the_dict):
        pass

    def __repr__(self):
        return "<%s.%s - id=%s, name=%s, area=%s>" % (__name__, self.__class__.__name__, self.id, self.name, str(self.area))
