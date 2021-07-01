
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Calibrate:
    def __init__(self, tft: Any) -> None: ...
    def drawCrossHair(self, x: Any, y: Any, clr: Any) -> None: ...
    def readCoordinates(self) -> Union[Tuple[, ], Tuple[Any, Any]]: ...
    def calibrate(self, x: Any, y: Any, i: int) -> None: ...
    def calibError(self) -> None: ...
    def tpcalib(self, save: Any=) -> Optional[Tuple[Any, Any]]: ...