"""
Module: 'os' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any


def rmdir(*args, **kwargs) -> Any:
    ...


def stat(*args, **kwargs) -> Any:
    ...


def urandom(*args, **kwargs) -> Any:
    ...


def rename(*args, **kwargs) -> Any:
    ...


def mount(*args, **kwargs) -> Any:
    ...


def uname(*args, **kwargs) -> Any:
    ...


def unlink(*args, **kwargs) -> Any:
    ...


def statvfs(*args, **kwargs) -> Any:
    ...


def umount(*args, **kwargs) -> Any:
    ...


def sync(*args, **kwargs) -> Any:
    ...


def mkdir(*args, **kwargs) -> Any:
    ...


def dupterm(*args, **kwargs) -> Any:
    ...


def chdir(*args, **kwargs) -> Any:
    ...


def remove(*args, **kwargs) -> Any:
    ...


def dupterm_notify(*args, **kwargs) -> Any:
    ...


def listdir(*args, **kwargs) -> Any:
    ...


def ilistdir(*args, **kwargs) -> Any:
    ...


def getcwd(*args, **kwargs) -> Any:
    ...


class VfsFat:
    def rename(self, *args, **kwargs) -> Any:
        ...

    def mkfs(self, *args, **kwargs) -> Any:
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class VfsLfs2:
    def rename(self, *args, **kwargs) -> Any:
        ...

    def mkfs(self, *args, **kwargs) -> Any:
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
