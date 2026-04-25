#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import bz2
import sqlite3
import sys
import tempfile

if sys.version_info >= (3, 12):
    from importlib.resources import as_file, files
else:
    from importlib_resources import as_file, files

from pyowm.weatherapi30.location import Location

CITY_ID_DB_PATH = 'cityids/cities.db.bz2'


class CityIDRegistry:

    MATCHINGS = {
        'exact': "SELECT city_id, name, country, state, lat, lon FROM city WHERE name=?",
        'like': r"SELECT city_id, name, country, state, lat, lon FROM city WHERE name LIKE ?"
    }

    def __init__(self, sqlite_db_path: str):
        self.connection = self.__decompress_db_to_memory(sqlite_db_path)

    @classmethod
    def get_instance(cls):
        """
        Factory method returning the default city ID registry
        :return: a `CityIDRegistry` instance
        """
        return CityIDRegistry(CITY_ID_DB_PATH)

    def __decompress_db_to_memory(self, sqlite_db_path: str):
        """
        Decompresses to memory the SQLite database at the provided path
        :param sqlite_db_path: str
        :return: None
        """
        pass

    def __query(self, sql_query: str, *args):
        """
        Queries the DB with the specified SQL query
        :param sql_query: str
        :return: list of tuples
        """
        pass

    def ids_for(self, city_name, country=None, state=None, matching='like'):
        """
        Returns a list of tuples in the form (city_id, name, country, state, lat, lon )
        The rule for querying follows the provided `matching` parameter value.
        If `country` is provided, the search is restricted to the cities of
        the specified country, and an even stricter search when `state` is provided as well
        :param city_name: the string toponym of the city to search
        :param country: two character str representing the country where to
        search for the city. Defaults to `None`, which means: search in all
        countries.
        :param state: two character str representing the state where to
        search for the city. Defaults to `None`. When not `None` also `state` must be specified
        :param matching: str. Default is `like`. Possible values:
        `exact` - literal, case-sensitive matching
        `like` - matches cities whose name contains, as a substring, the string
        fed to the function, case-insensitive,
        :raises ValueError if the value for `matching` is unknown
        :return: list of tuples
        """
        pass

    def locations_for(self, city_name, country=None, state=None, matching='like'):
        """
        Returns a list of `Location` objects
        The rule for querying follows the provided `matching` parameter value.
        If `country` is provided, the search is restricted to the cities of
        the specified country, and an even stricter search when `state` is provided as well
        :param city_name: the string toponym of the city to search
        :param country: two character str representing the country where to
        search for the city. Defaults to `None`, which means: search in all
        countries.
        :param state: two character str representing the state where to
        search for the city. Defaults to `None`. When not `None` also `state` must be specified
        :param matching: str. Default is `like`. Possible values:
        `exact` - literal, case-sensitive matching
        `like` - matches cities whose name contains, as a substring, the string
        fed to the function, case-insensitive,
        :raises ValueError if the value for `matching` is unknown
        :return: list of `Location` objects
        """
        pass

    def geopoints_for(self, city_name, country=None, state=None, matching='like'):
        """
        Returns a list of ``pyowm.utils.geo.Point`` objects corresponding to
        the int IDs and relative toponyms and 2-chars country of the cities
        matching the provided city name.
        The rule for identifying matchings is according to the provided
        `matching` parameter value.
        If `country` is provided, the search is restricted to the cities of
        the specified country.
        :param city_name: the string toponym of the city to search
        :param country: two character str representing the country where to
        search for the city. Defaults to `None`, which means: search in all
        countries.
        :param state: two character str representing the state where to
        search for the city. Defaults to `None`. When not `None` also `state` must be specified
        :param matching: str. Default is `nocase`. Possible values:
        `exact` - literal, case-sensitive matching
        `like` - matches cities whose name contains, as a substring, the string
        fed to the function, case-insensitive,
        :raises ValueError if the value for `matching` is unknown
        :return: list of `pyowm.utils.geo.Point` objects
        """
        pass
