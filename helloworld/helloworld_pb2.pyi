from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RequestDate(_message.Message):
    __slots__ = ("day", "month", "year")
    DAY_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    day: int
    month: int
    year: int
    def __init__(self, day: _Optional[int] = ..., month: _Optional[int] = ..., year: _Optional[int] = ...) -> None: ...

class ReplyDate(_message.Message):
    __slots__ = ("day", "month", "year")
    DAY_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    day: int
    month: int
    year: int
    def __init__(self, day: _Optional[int] = ..., month: _Optional[int] = ..., year: _Optional[int] = ...) -> None: ...

class RequestAddDay(_message.Message):
    __slots__ = ("day", "month", "year", "dayToAdd")
    DAY_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    DAYTOADD_FIELD_NUMBER: _ClassVar[int]
    day: int
    month: int
    year: int
    dayToAdd: int
    def __init__(self, day: _Optional[int] = ..., month: _Optional[int] = ..., year: _Optional[int] = ..., dayToAdd: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CentroDianaResponse(_message.Message):
    __slots__ = ("speed",)
    SPEED_FIELD_NUMBER: _ClassVar[int]
    speed: float
    def __init__(self, speed: _Optional[float] = ...) -> None: ...

class DisparoRequest(_message.Message):
    __slots__ = ("username", "angle", "speed")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    username: str
    angle: float
    speed: float
    def __init__(self, username: _Optional[str] = ..., angle: _Optional[float] = ..., speed: _Optional[float] = ...) -> None: ...

class DisparoResponse(_message.Message):
    __slots__ = ("difference",)
    DIFFERENCE_FIELD_NUMBER: _ClassVar[int]
    difference: float
    def __init__(self, difference: _Optional[float] = ...) -> None: ...

class MejorDisparoResponse(_message.Message):
    __slots__ = ("username", "speed")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    username: str
    speed: float
    def __init__(self, username: _Optional[str] = ..., speed: _Optional[float] = ...) -> None: ...
