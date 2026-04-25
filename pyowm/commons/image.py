#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyowm.commons.databoxes import ImageType
from pyowm.commons.enums import ImageTypeEnum


class Image:

    """
    Wrapper class for a generic image

    :param data: raw image data
    :type data: bytes
    :param image_type: the type of the image, if known
    :type image_type: `pyowm.commons.databoxes.ImageType` or `None`
    """

    def __init__(self, data, image_type=None):
        pass

    def persist(self, path_to_file):
        """
        Saves the image to disk on a file

        :param path_to_file: path to the target file
        :type path_to_file: str
        :return: `None`
        """
        pass

    @classmethod
    def load(cls, path_to_file):
        """
        Loads the image data from a file on disk and tries to guess the image MIME type

        :param path_to_file: path to the source file
        :type path_to_file: str
        :return: a `pyowm.image.Image` instance
        """
        pass

    def __repr__(self):
        return "<%s.%s - type=%s>" % (__name__, self.__class__.__name__, str(self.image_type))
