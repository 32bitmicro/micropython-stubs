from _typeshed import Incomplete as Incomplete

FLAG_NOTIFY: int
FLAG_READ: int
FLAG_WRITE: int
FLAG_INDICATE: int
FLAG_WRITE_NO_RESPONSE: int

class UUID:
    def __init__(self, *argv, **kwargs) -> None: ...

class BLE:
    def gatts_read(self, *args, **kwargs) -> Incomplete: ...
    def gatts_set_buffer(self, *args, **kwargs) -> Incomplete: ...
    def gatts_register_services(self, *args, **kwargs) -> Incomplete: ...
    def gattc_write(self, *args, **kwargs) -> Incomplete: ...
    def gatts_notify(self, *args, **kwargs) -> Incomplete: ...
    def gatts_indicate(self, *args, **kwargs) -> Incomplete: ...
    def l2cap_send(self, *args, **kwargs) -> Incomplete: ...
    def l2cap_listen(self, *args, **kwargs) -> Incomplete: ...
    def gatts_write(self, *args, **kwargs) -> Incomplete: ...
    def l2cap_recvinto(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def l2cap_disconnect(self, *args, **kwargs) -> Incomplete: ...
    def l2cap_connect(self, *args, **kwargs) -> Incomplete: ...
    def gap_connect(self, *args, **kwargs) -> Incomplete: ...
    def gap_pair(self, *args, **kwargs) -> Incomplete: ...
    def gap_disconnect(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def gap_advertise(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def gattc_read(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_services(self, *args, **kwargs) -> Incomplete: ...
    def gap_passkey(self, *args, **kwargs) -> Incomplete: ...
    def gattc_exchange_mtu(self, *args, **kwargs) -> Incomplete: ...
    def gap_scan(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_descriptors(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_characteristics(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
