"""
Module: 'uarray' on micropython-v1.20.0-rp2-PIMORONI_PICOLIPO_16MB
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PIMORONI_PICOLIPO_16MB', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.13.7
from typing import List, Optional, Any
from _typeshed import Incomplete as Incomplete


class array(List):
    """
    Create array with elements of given type. Initial contents of the
    array are given by *iterable*. If it is not provided, an empty
    array is created.
    """

    def extend(self, iterable) -> Incomplete:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
        ...

    def append(self, val) -> Incomplete:
        """
        Append new element *val* to the end of array, growing it.
        """
        ...

    def __init__(self, typecode, iterable: Optional[Any] = ...) -> None:
        ...
