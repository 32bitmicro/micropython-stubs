"""
Module: 'ds18x20' on micropython-esp8266-1.16
"""
# MCU: {'ver': '1.16', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.16', 'name': 'micropython', 'mpy': 9733, 'version': '1.16', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.4.3
from typing import Any

def const(*args) -> Any:
    ...


class DS18X20:
    ''
    def __init__(self, *args) -> None:
        ...

    def scan(self, *args) -> Any:
        ...

    def convert_temp(self, *args) -> Any:
        ...

    def read_scratch(self, *args) -> Any:
        ...

    def write_scratch(self, *args) -> Any:
        ...

    def read_temp(self, *args) -> Any:
        ...
