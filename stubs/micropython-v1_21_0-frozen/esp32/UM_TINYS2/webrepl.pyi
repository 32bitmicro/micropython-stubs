from _typeshed import Incomplete
from micropython import const as const

listen_s: Incomplete
client_s: Incomplete
DEBUG: int
_DEFAULT_STATIC_HOST: str
static_host = _DEFAULT_STATIC_HOST

def server_handshake(cl): ...
def send_html(cl) -> None: ...
def setup_conn(port, accept_handler): ...
def accept_conn(listen_sock): ...
def stop() -> None: ...
def start(port: int = ..., password: Incomplete | None = ..., accept_handler=...) -> None: ...
def start_foreground(port: int = ..., password: Incomplete | None = ...) -> None: ...
