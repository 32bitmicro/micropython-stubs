"""
Module: 'uasyncio.event' on micropython-v1.23.0-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.23.0', 'cpu': 'SAMD51P19A'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class ThreadSafeFlag:
    def set(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def clear(self, *args, **kwargs) -> Incomplete: ...

    wait: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Event:
    def set(self, *args, **kwargs) -> Incomplete: ...
    def is_set(self, *args, **kwargs) -> Incomplete: ...
    def clear(self, *args, **kwargs) -> Incomplete: ...

    wait: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
