from _typeshed import Incomplete
from micropython import const as const

_PACKAGE_INDEX: str
_CHUNK_SIZE: int

def _ensure_path_exists(path) -> None: ...
def _chunk(src, dest) -> None: ...
def _check_exists(path, short_hash): ...
def _rewrite_url(url, branch: Incomplete | None = ...): ...
def _download_file(url, dest): ...
def _install_json(package_json_url, index, target, version, mpy): ...
def _install_package(package, index, target, version, mpy): ...
def install(
    package, index: Incomplete | None = ..., target: Incomplete | None = ..., version: Incomplete | None = ..., mpy: bool = ...
) -> None: ...
