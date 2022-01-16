from typing import Any

class Struct:
    def pack(self, *argv) -> Any: ...
    def unpack(self, *argv) -> Any: ...

def calcsize() -> None: ...
def pack() -> None: ...
def pack_into() -> None: ...
def unpack() -> None: ...
def unpack_from() -> None: ...