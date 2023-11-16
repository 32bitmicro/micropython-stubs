from typing import Optional, Any
from _typeshed import Incomplete as Incomplete

def isenabled(*args, **kwargs) -> Any: ...
def mem_free() -> int:
    """
    Return the number of bytes of available heap RAM, or -1 if this amount
    is not known.

    Difference to CPython

       This function is MicroPython extension.
    """

def mem_alloc() -> int:
    """
    Return the number of bytes of heap RAM that are allocated.

    Difference to CPython

       This function is MicroPython extension.
    """

def collect() -> None:
    """
    Run a garbage collection.
    """

def enable() -> None:
    """
    Enable automatic garbage collection.
    """

def disable() -> None:
    """
    Disable automatic garbage collection.  Heap memory can still be allocated,
    and garbage collection can still be initiated manually using :meth:`gc.collect`.
    """
