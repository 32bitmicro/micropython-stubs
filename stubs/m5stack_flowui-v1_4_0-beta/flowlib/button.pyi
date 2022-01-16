from typing import Any

class Btn:
    def attach(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    def detach(self, *argv) -> Any: ...
    def multiBtnCb(self, *argv) -> Any: ...
    def restart(self, *argv) -> Any: ...
    def timerCb(self, *argv) -> Any: ...

class BtnChild:
    def deinit(self, *argv) -> Any: ...
    def isPressed(self, *argv) -> Any: ...
    def isReleased(self, *argv) -> Any: ...
    def pressFor(self, *argv) -> Any: ...
    def restart(self, *argv) -> Any: ...
    def upDate(self, *argv) -> Any: ...
    def wasDoublePress(self, *argv) -> Any: ...
    def wasPressed(self, *argv) -> Any: ...
    def wasReleased(self, *argv) -> Any: ...

DOUBLEPRESS: int
LONGPRESS: int
MULTIPRESS: int
PRESS: int
PRESSWAIT: int
RELEASE: int
_state_list: Any
machine: Any
micropython: Any
time: Any