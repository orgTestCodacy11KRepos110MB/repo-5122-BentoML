import typing
from typing import FrozenSet, Set, Union
import six
from ._typing import Text

if typing.TYPE_CHECKING: ...
__all__ = ["Mode", "check_readable", "check_writable", "validate_openbin_mode"]

@six.python_2_unicode_compatible
class Mode(typing.Container[Text]):
    def __init__(self, mode: Text) -> None: ...
    def __repr__(self) -> Text: ...
    def __str__(self) -> Text: ...
    def __contains__(self, character: object) -> bool: ...
    def to_platform(self) -> Text: ...
    def to_platform_bin(self) -> Text: ...
    def validate(
        self, _valid_chars: Union[Set[Text], FrozenSet[Text]] = ...
    ) -> None: ...
    def validate_bin(self) -> None: ...
    @property
    def create(self) -> bool: ...
    @property
    def reading(self) -> bool: ...
    @property
    def writing(self) -> bool: ...
    @property
    def appending(self) -> bool: ...
    @property
    def updating(self) -> bool: ...
    @property
    def truncate(self) -> bool: ...
    @property
    def exclusive(self) -> bool: ...
    @property
    def binary(self) -> bool: ...
    @property
    def text(self) -> bool: ...

def check_readable(mode: Text) -> bool: ...
def check_writable(mode: Text) -> bool: ...
def validate_open_mode(mode: Text) -> None: ...
def validate_openbin_mode(
    mode: Text, _valid_chars: Union[Set[Text], FrozenSet[Text]] = ...
) -> None: ...
