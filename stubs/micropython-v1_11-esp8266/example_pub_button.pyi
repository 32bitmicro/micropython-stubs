from typing import Any

CLIENT_ID: Any

class MQTTClient:
    def _recv_len(self, *args) -> Any: ...
    def _send_str(self, *args) -> Any: ...
    def check_msg(self, *args) -> Any: ...
    def connect(self, *args) -> Any: ...
    def disconnect(self, *args) -> Any: ...
    def ping(self, *args) -> Any: ...
    def publish(self, *args) -> Any: ...
    def set_callback(self, *args) -> Any: ...
    def set_last_will(self, *args) -> Any: ...
    def subscribe(self, *args) -> Any: ...
    def wait_msg(self, *args) -> Any: ...

class Pin:
    IN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    PULL_UP: int
    def init(self, *args) -> Any: ...
    def irq(self, *args) -> Any: ...
    def off(self, *args) -> Any: ...
    def on(self, *args) -> Any: ...
    def value(self, *args) -> Any: ...

SERVER: str
TOPIC: Any
button: Any
machine: Any

def main(*args) -> Any: ...

time: Any
ubinascii: Any
