
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Timer:
    def deinit() -> None: ...
    def update() -> None: ...
class TimerEx:
    def addTimer() -> None: ...
    def checkInit() -> None: ...
    def deinit() -> None: ...
    def timeCb() -> None: ...