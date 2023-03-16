from _typeshed import Incomplete
from senml.senml_base import SenmlBase as SenmlBase

class SenmlRecord(SenmlBase):
    __parent: Incomplete
    _unit: Incomplete
    _value: Incomplete
    _time: Incomplete
    _sum: Incomplete
    _update_time: Incomplete
    name: Incomplete
    unit: Incomplete
    actuate: Incomplete
    def __init__(self, name, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def _check_value_type(self, value) -> None: ...
    def _check_number_type(self, value, field_name) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    @property
    def time(self): ...
    @time.setter
    def time(self, value) -> None: ...
    @property
    def update_time(self): ...
    @update_time.setter
    def update_time(self, value) -> None: ...
    @property
    def sum(self): ...
    @sum.setter
    def sum(self, value) -> None: ...
    @property
    def _parent(self): ...
    @_parent.setter
    def _parent(self, value) -> None: ...
    def _build_rec_dict(self, naming_map, appendTo) -> None: ...
    def _from_raw(self, raw, naming_map) -> None: ...
    def do_actuate(self, raw, naming_map) -> None: ...