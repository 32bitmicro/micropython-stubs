from typing import Any

class FrameBuffer:
    def __init__(self, *argv, **kwargs) -> None: ...
    def blit(self, *args) -> Any: ...
    def fill(self, *args) -> Any: ...
    def fill_rect(self, *args) -> Any: ...
    def hline(self, *args) -> Any: ...
    def line(self, *args) -> Any: ...
    def pixel(self, *args) -> Any: ...
    def rect(self, *args) -> Any: ...
    def scroll(self, *args) -> Any: ...
    def text(self, *args) -> Any: ...
    def vline(self, *args) -> Any: ...

def FrameBuffer1(*args) -> Any: ...

GS2_HMSB: int
GS4_HMSB: int
GS8: int
MONO_HLSB: int
MONO_HMSB: int
MONO_VLSB: int
MVLSB: int
RGB565: int
