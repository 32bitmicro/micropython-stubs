"""
Module: 'ds18x20' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def const(*args, **kwargs) -> Incomplete:
    ...


class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Incomplete:
        ...

    def write_scratch(self, *args, **kwargs) -> Incomplete:
        ...

    def read_temp(self, *args, **kwargs) -> Incomplete:
        ...

    def convert_temp(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...