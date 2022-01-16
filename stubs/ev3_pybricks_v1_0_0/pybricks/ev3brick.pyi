from typing import Any

class Display:
    _font_height: int
    def _next_line(self, *argv) -> Any: ...
    def _reset_text_history(self, *argv) -> Any: ...
    _valid_devices: Any
    def clear(self, *argv) -> Any: ...
    def image(self, *argv) -> Any: ...
    def text(self, *argv) -> Any: ...

class Speaker:
    _valid_devices: Any
    def beep(self, *argv) -> Any: ...
    def beeps(self, *argv) -> Any: ...
    def file(self, *argv) -> Any: ...
    def speech(self, *argv) -> Any: ...
    def tune(self, *argv) -> Any: ...

battery: Any

def buttons() -> None: ...

display: Any

def exit() -> None: ...
def light() -> None: ...

sound: Any
stderr: Any