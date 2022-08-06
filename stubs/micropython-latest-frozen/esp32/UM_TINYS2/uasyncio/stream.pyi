from . import core as core
from collections.abc import Generator
from typing import Any

class Stream:
    s: Any
    e: Any
    out_buf: bytes
    def __init__(self, s, e=...) -> None: ...
    def get_extra_info(self, v): ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...
    async def read(self, n: int = ...) -> Generator[Any, None, Any]: ...
    async def readinto(self, buf) -> Generator[Any, None, Any]: ...
    async def readexactly(self, n) -> Generator[Any, None, Any]: ...
    async def readline(self) -> Generator[Any, None, Any]: ...
    def write(self, buf) -> None: ...
    async def drain(self) -> Generator[Any, None, Any]: ...

StreamReader = Stream
StreamWriter = Stream

async def open_connection(host, port) -> Generator[Any, None, Any]: ...

class Server:
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...
    async def _serve(self, s, cb) -> Generator[Any, None, None]: ...

async def start_server(cb, host, port, backlog: int = ...): ...
async def stream_awrite(self, buf, off: int = ..., sz: int = ...) -> None: ...
