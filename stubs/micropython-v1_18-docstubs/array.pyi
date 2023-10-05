"""
Efficient arrays of numeric data.

MicroPython module: https://docs.micropython.org/en/v1.18/library/array.html

CPython module: :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).
"""

# source version: v1_18
# origin module:: repos/micropython/docs/library/array.rst
from typing import Any, Optional
from _typeshed import Incomplete

class array:
    """
    Create array with elements of given type. Initial contents of the
    array are given by *iterable*. If it is not provided, an empty
    array is created.
    """

    def __init__(self, typecode, iterable: Optional[Any] = None) -> None: ...
    def append(self, val) -> Incomplete:
        """
        Append new element *val* to the end of array, growing it.
        """
        ...
    def extend(self, iterable) -> Incomplete:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
        ...
