"""
Module: 'ds18x20' on micropython-v1.24.0-preview-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '42', 'arch': 'armv7emsp', 'ver': '1.24.0-preview-42', 'cpu': 'SAMD51P19A'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

def const(*args, **kwargs) -> Incomplete: ...

class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Incomplete: ...
    def read_temp(self, *args, **kwargs) -> Incomplete: ...
    def write_scratch(self, *args, **kwargs) -> Incomplete: ...
    def convert_temp(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
