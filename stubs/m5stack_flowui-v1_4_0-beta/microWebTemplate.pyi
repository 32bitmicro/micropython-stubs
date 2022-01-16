from typing import Any

class MicroWebTemplate:
    def Execute(self, *argv) -> Any: ...
    INSTRUCTION_ELIF: str
    INSTRUCTION_ELSE: str
    INSTRUCTION_END: str
    INSTRUCTION_FOR: str
    INSTRUCTION_IF: str
    INSTRUCTION_INCLUDE: str
    INSTRUCTION_PYTHON: str
    TOKEN_CLOSE: str
    TOKEN_CLOSE_LEN: int
    TOKEN_OPEN: str
    TOKEN_OPEN_LEN: int
    def Validate(self, *argv) -> Any: ...
    def _parseBloc(self, *argv) -> Any: ...
    def _parseCode(self, *argv) -> Any: ...
    def _processInstructionELIF(self, *argv) -> Any: ...
    def _processInstructionELSE(self, *argv) -> Any: ...
    def _processInstructionEND(self, *argv) -> Any: ...
    def _processInstructionFOR(self, *argv) -> Any: ...
    def _processInstructionIF(self, *argv) -> Any: ...
    def _processInstructionINCLUDE(self, *argv) -> Any: ...
    def _processInstructionPYTHON(self, *argv) -> Any: ...
    def _processToken(self, *argv) -> Any: ...

re: Any