from typing import Any

class ADC:
    ATTN_0DB: int
    ATTN_11DB: int
    ATTN_2_5DB: int
    ATTN_6DB: int
    HALL: int
    WIDTH_10BIT: int
    WIDTH_11BIT: int
    WIDTH_12BIT: int
    WIDTH_9BIT: int
    def atten(self, *argv) -> Any: ...
    def collect(self, *argv) -> Any: ...
    def collected(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    def progress(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def read_timed(self, *argv) -> Any: ...
    def readraw(self, *argv) -> Any: ...
    def stopcollect(self, *argv) -> Any: ...
    def vref(self, *argv) -> Any: ...
    def width(self, *argv) -> Any: ...

class PWM:
    def deinit(self, *argv) -> Any: ...
    def duty(self, *argv) -> Any: ...
    def freq(self, *argv) -> Any: ...
    def init(self, *argv) -> Any: ...
    def list(self, *argv) -> Any: ...
    def pause(self, *argv) -> Any: ...
    def resume(self, *argv) -> Any: ...

class Pin:
    IN: int
    INOUT: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    OUT_OD: int
    PULL_DOWN: int
    PULL_FLOAT: int
    PULL_HOLD: int
    PULL_UP: int
    WAKE_HIGH: int
    WAKE_LOW: int
    def deinit(self, *argv) -> Any: ...
    def init(self, *argv) -> Any: ...
    def irq(self, *argv) -> Any: ...
    def off(self, *argv) -> Any: ...
    def on(self, *argv) -> Any: ...
    def value(self, *argv) -> Any: ...

_adc_map: Any

def _deinitIO() -> None: ...

_io_map: Any
_pwm_map: Any

def analogRead() -> None: ...
def analogWrite() -> None: ...
def digitalRead() -> None: ...
def digitalWrite() -> None: ...
def map_value() -> None: ...
def toggleIO() -> None: ...