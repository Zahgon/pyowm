#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
import warnings


def deprecated(will_be=None, on_version=None, name=None):
    """
    Function decorator that warns about deprecation upon function invocation.
    :param will_be: str representing the target action on the deprecated function
    :param on_version: tuple representing a SW version
    :param name: name of the entity to be deprecated (useful when decorating
    __init__ methods so you can specify the deprecated class name)
    :return: callable
    """

    def outer_function(function):
        return function

    return outer_function
