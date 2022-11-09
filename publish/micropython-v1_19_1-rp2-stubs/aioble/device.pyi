from typing import Any

def register_irq_handler(*args, **kwargs) -> Any: ...
def log_error(*args, **kwargs) -> Any: ...
def const(*args, **kwargs) -> Any: ...

class DeviceConnection:
    def timeout(self, *args, **kwargs) -> Any: ...
    def services(self, *args, **kwargs) -> Any: ...
    def is_connected(self, *args, **kwargs) -> Any: ...
    service: Any
    pair: Any
    exchange_mtu: Any
    l2cap_accept: Any
    disconnected: Any
    disconnect: Any
    l2cap_connect: Any
    device_task: Any
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Any

class DeviceTimeout:
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceDisconnectedError(Exception): ...