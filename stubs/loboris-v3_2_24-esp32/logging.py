"""
Module: 'logging' on esp32_LoBo
MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.24', version='ESP32_LoBo_v3.2.24 on 2018-09-06', machine='ESP32 board with ESP32')
Stubber: 1.0.0
"""
CRITICAL = 50
DEBUG = 10
ERROR = 40
INFO = 20


class Logger:
    """"""

    def _level_str(self, *args) -> Any:
        pass

    def critical(self, *args) -> Any:
        pass

    def debug(self, *args) -> Any:
        pass

    def error(self, *args) -> Any:
        pass

    def exc(self, *args) -> Any:
        pass

    def exception(self, *args) -> Any:
        pass

    def info(self, *args) -> Any:
        pass

    def isEnabledFor(self, *args) -> Any:
        pass

    level = 0

    def log(self, *args) -> Any:
        pass

    def setLevel(self, *args) -> Any:
        pass

    def warning(self, *args) -> Any:
        pass


NOTSET = 0
WARNING = 30
_level = 20
_level_dict = None
_loggers = None
_stream = None


def basicConfig(*args) -> Any:
    pass


def debug(*args) -> Any:
    pass


def getLogger(*args) -> Any:
    pass


def info(*args) -> Any:
    pass


sys = None
