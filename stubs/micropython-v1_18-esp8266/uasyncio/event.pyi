from typing import Any

class Event:
    def __init__(self, *argv, **kwargs) -> None: ...
    def __init__(self, *args) -> None: ...
    def clear(self, *args) -> Any: ...
    def set(self, *args) -> Any: ...
    def is_set(self, *args) -> Any: ...
    wait: Any

class ThreadSafeFlag:
    def __init__(self, *argv, **kwargs) -> None: ...
    def __init__(self, *args) -> None: ...
    def set(self, *args) -> Any: ...
    def ioctl(self, *args) -> Any: ...
    wait: Any
