from typing import Any

def bitstream(*args, **kwargs) -> Any: ...

class NeoPixel:
    ORDER: tuple
    def write(self, *args, **kwargs) -> Any: ...
    def fill(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...