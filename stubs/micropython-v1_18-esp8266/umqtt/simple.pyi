from typing import Any

def hexlify(*args) -> Any: ...

class MQTTException(Exception): ...

class MQTTClient:
    def __init__(self, *argv, **kwargs) -> None: ...
    def __init__(self, *args) -> None: ...
    def connect(self, *args) -> Any: ...
    def disconnect(self, *args) -> Any: ...
    def set_callback(self, *args) -> Any: ...
    def set_last_will(self, *args) -> Any: ...
    def ping(self, *args) -> Any: ...
    def publish(self, *args) -> Any: ...
    def subscribe(self, *args) -> Any: ...
    def wait_msg(self, *args) -> Any: ...
    def check_msg(self, *args) -> Any: ...
