"""
Module: 'io' on micropython-v1.20.0-samd-ADAFRUIT_FEATHER_M4_EXPRESS
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'samd', 'board': 'ADAFRUIT_FEATHER_M4_EXPRESS', 'cpu': 'SAMD51J19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import IO, Optional, Any
import abc
from _typeshed import Incomplete as Incomplete
from stdlib.io import *


def open(name, mode: str = ..., **kwargs) -> Incomplete:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """
    ...


class IOBase:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class StringIO(
    IO,
):
    def write(self, *args, **kwargs) -> Any:
        ...

    def flush(self, *args, **kwargs) -> Any:
        ...

    def getvalue(self, *args, **kwargs) -> Any:
        ...

    def seek(self, *args, **kwargs) -> Any:
        ...

    def tell(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, string: Optional[Any] = ...) -> None:
        ...


class BytesIO(
    IO,
):
    """
    In-memory file-like objects for input/output. `StringIO` is used for
    text-mode I/O (similar to a normal file opened with "t" modifier).
    `BytesIO` is used for binary-mode I/O (similar to a normal file
    opened with "b" modifier). Initial contents of file-like objects
    can be specified with *string* parameter (should be normal string
    for `StringIO` or bytes object for `BytesIO`). All the usual file
    methods like ``read()``, ``write()``, ``seek()``, ``flush()``,
    ``close()`` are available on these objects, and additionally, a
    following method:
    """

    def write(self, *args, **kwargs) -> Any:
        ...

    def flush(self, *args, **kwargs) -> Any:
        ...

    def getvalue(self) -> Incomplete:
        """
        Get the current contents of the underlying buffer which holds data.
        """
        ...

    def seek(self, *args, **kwargs) -> Any:
        ...

    def tell(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, string: Optional[Any] = ...) -> None:
        ...
