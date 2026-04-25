#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons.http_client import HttpClient
from pyowm.constants import STATIONS_API_VERSION
from pyowm.stationsapi30.measurement import AggregatedMeasurement
from pyowm.stationsapi30.station import Station
from pyowm.stationsapi30.uris import ROOT_STATIONS_API_URL, STATIONS_URI, NAMED_STATION_URI, MEASUREMENTS_URI


class StationsManager:

    """
    A manager objects that provides a full interface to OWM Stations API. Mainly
    it implements CRUD methods on Station entities and the corresponding
    measured datapoints.

    :param API_key: the OWM Weather API key
    :type API_key: str
    :param config: the configuration dictionary
    :type config: dict
    :returns: a *StationsManager* instance
    :raises: *AssertionError* when no API Key is provided

    """

    def __init__(self, API_key, config):
        pass

    def stations_api_version(self):
        pass

    # STATIONS Methods

    def get_stations(self):
        """
        Retrieves all of the user's stations registered on the Stations API.

        :returns: list of *pyowm.stationsapi30.station.Station* objects

        """
        pass

    def get_station(self, id):
        """
        Retrieves a named station registered on the Stations API.

        :param id: the ID of the station
        :type id: str
        :returns: a *pyowm.stationsapi30.station.Station* object

        """
        pass

    def create_station(self, external_id, name, lat, lon, alt=None):
        """
        Create a new station on the Station API with the given parameters

        :param external_id: the user-given ID of the station
        :type external_id: str
        :param name: the name of the station
        :type name: str
        :param lat: latitude of the station
        :type lat: float
        :param lon: longitude of the station
        :type lon: float
        :param alt: altitude of the station
        :type alt: float
        :returns: the new *pyowm.stationsapi30.station.Station* object
        """
        pass

    def update_station(self, station):
        """
        Updates the Station API record identified by the ID of the provided
        *pyowm.stationsapi30.station.Station* object with all of its fields

        :param station: the *pyowm.stationsapi30.station.Station* object to be updated
        :type station: *pyowm.stationsapi30.station.Station*
        :returns: `None` if update is successful, an exception otherwise
        """
        pass

    def delete_station(self, station):
        """
        Deletes the Station API record identified by the ID of the provided
        *pyowm.stationsapi30.station.Station*, along with all its related
        measurements

        :param station: the *pyowm.stationsapi30.station.Station* object to be deleted
        :type station: *pyowm.stationsapi30.station.Station*
        :returns: `None` if deletion is successful, an exception otherwise
        """
        pass

    # Measurements-related methods

    def send_measurement(self, measurement):
        """
        Posts the provided Measurement object's data to the Station API.

        :param measurement: the *pyowm.stationsapi30.measurement.Measurement*
          object to be posted
        :type measurement: *pyowm.stationsapi30.measurement.Measurement* instance
        :returns: `None` if creation is successful, an exception otherwise
        """
        pass

    def send_measurements(self, list_of_measurements):
        """
        Posts data about the provided list of Measurement objects to the
        Station API. The objects may be related to different station IDs.

        :param list_of_measurements: list of *pyowm.stationsapi30.measurement.Measurement*
          objects to be posted
        :type list_of_measurements: list of *pyowm.stationsapi30.measurement.Measurement*
          instances
        :returns: `None` if creation is successful, an exception otherwise
        """
        pass

    def get_measurements(self, station_id, aggregated_on, from_timestamp,
                         to_timestamp, limit=100):
        """
        Reads measurements of a specified station recorded in the specified time
        window and aggregated on minute, hour or day. Optionally, the number of
        resulting measurements can be limited.

        :param station_id: unique station identifier
        :type station_id: str
        :param aggregated_on: aggregation time-frame for this measurement
        :type aggregated_on: string between 'm','h' and 'd'
        :param from_timestamp: Unix timestamp corresponding to the beginning of
          the time window
        :type from_timestamp: int
        :param to_timestamp: Unix timestamp corresponding to the end of the
          time window
        :type to_timestamp: int
        :param limit: max number of items to be returned. Defaults to 100
        :type limit: int
        :returns: list of *pyowm.stationsapi30.measurement.AggregatedMeasurement*
          objects
        """
        pass

    def send_buffer(self, buffer):
        """
        Posts to the Stations API data about the Measurement objects contained
        into the provided Buffer instance.

        :param buffer: the *pyowm.stationsapi30.buffer.Buffer* instance whose
          measurements are to be posted
        :type buffer: *pyowm.stationsapi30.buffer.Buffer* instance
        :returns: `None` if creation is successful, an exception otherwise
        """
        pass

    def _structure_dict(self, measurement):
        pass

    def __repr__(self):
        return '<%s.%s>' % (__name__, self.__class__.__name__)