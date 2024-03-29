import sys
from io import BytesIO
from typing import (
    IO,
    Any,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Text,
    Type,
    TypeVar,
    Union,
    overload,
)
from yaml.dumper import *
from yaml.error import *
from yaml.events import *
from yaml.loader import *
from yaml.nodes import *
from yaml.representer import BaseRepresenter
from yaml.tokens import *
from . import resolver as resolver
from .cyaml import *

if sys.version_info >= (3, 0):
    _Str = str
else: ...
_Yaml = Any
__with_libyaml__: Any
__version__: str
_T = ...
_R = ...

def scan(stream, Loader=...): ...
def parse(stream, Loader=...): ...
def compose(stream, Loader=...): ...
def compose_all(stream, Loader=...): ...
def load(stream: Union[bytes, IO[bytes], Text, IO[Text]], Loader=...) -> Any: ...
def load_all(
    stream: Union[bytes, IO[bytes], Text, IO[Text]], Loader=...
) -> Iterator[Any]: ...
def full_load(stream: Union[bytes, IO[bytes], Text, IO[Text]]) -> Any: ...
def full_load_all(stream: Union[bytes, IO[bytes], Text, IO[Text]]) -> Iterator[Any]: ...
def safe_load(stream: Union[bytes, IO[bytes], Text, IO[Text]]) -> Any: ...
def safe_load_all(stream: Union[bytes, IO[bytes], Text, IO[Text]]) -> Iterator[Any]: ...
def unsafe_load(stream: Union[bytes, IO[bytes], Text, IO[Text]]) -> Any: ...
def unsafe_load_all(
    stream: Union[bytes, IO[bytes], Text, IO[Text]]
) -> Iterator[Any]: ...
def emit(
    events,
    stream=...,
    Dumper=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
): ...
@overload
def serialize_all(
    nodes,
    stream: IO[str],
    Dumper=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding=...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...,
) -> None: ...
@overload
def serialize_all(
    nodes,
    stream: None = ...,
    Dumper=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding: Optional[_Str] = ...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...,
) -> _Yaml: ...
@overload
def serialize(
    node,
    stream: IO[str],
    Dumper=...,
    *,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding=...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...
) -> None: ...
@overload
def serialize(
    node,
    stream: None = ...,
    Dumper=...,
    *,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding: Optional[_Str] = ...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...
) -> _Yaml: ...
@overload
def dump_all(
    documents: Sequence[Any],
    stream: IO[str],
    Dumper=...,
    default_style=...,
    default_flow_style=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding=...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...,
    sort_keys: bool = ...,
) -> None: ...
@overload
def dump_all(
    documents: Sequence[Any],
    stream: None = ...,
    Dumper=...,
    default_style=...,
    default_flow_style=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding: Optional[_Str] = ...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...,
    sort_keys: bool = ...,
) -> _Yaml: ...
@overload
def dump(
    data: Any,
    stream: IO[str],
    Dumper=...,
    *,
    default_style=...,
    default_flow_style=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding=...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...,
    sort_keys: bool = ...
) -> None: ...
@overload
def dump(
    data: Any,
    stream: None = ...,
    Dumper=...,
    *,
    default_style=...,
    default_flow_style=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding: Optional[_Str] = ...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...,
    sort_keys: bool = ...
) -> _Yaml: ...
@overload
def safe_dump_all(
    documents: Sequence[Any],
    stream: IO[str],
    *,
    default_style=...,
    default_flow_style=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding=...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...,
    sort_keys: bool = ...
) -> None: ...
@overload
def safe_dump_all(
    documents: Sequence[Any],
    stream: None = ...,
    *,
    default_style=...,
    default_flow_style=...,
    canonical=...,
    indent=...,
    width=...,
    allow_unicode=...,
    line_break=...,
    encoding: Optional[_Str] = ...,
    explicit_start=...,
    explicit_end=...,
    version=...,
    tags=...,
    sort_keys: bool = ...
) -> _Yaml: ...
@overload
def safe_dump(
    data: Any,
    stream: Optional[BytesIO],
    *,
    default_style: Optional[str] = ...,
    default_flow_style: bool = ...,
    canonical: Optional[bool] = ...,
    indent: Optional[int] = ...,
    width: Optional[int] = ...,
    allow_unicode: Optional[bool] = ...,
    line_break: Optional[str] = ...,
    encoding: Optional[str] = ...,
    explicit_start: Optional[bool] = ...,
    explicit_end: Optional[bool] = ...,
    version: Optional[bool] = ...,
    tags: Optional[bool] = ...,
    sort_keys: bool = ...
) -> None: ...
@overload
def safe_dump(
    data: Any,
    stream: None = ...,
    *,
    default_style: Optional[str] = ...,
    default_flow_style: bool = ...,
    canonical: Optional[bool] = ...,
    indent: Optional[int] = ...,
    width: Optional[int] = ...,
    allow_unicode: Optional[bool] = ...,
    line_break: Optional[str] = ...,
    encoding: Optional[str] = ...,
    explicit_start: Optional[bool] = ...,
    explicit_end: Optional[bool] = ...,
    version: Optional[bool] = ...,
    tags: Optional[bool] = ...,
    sort_keys: bool = ...
) -> BytesIO: ...
def add_implicit_resolver(tag, regexp, first=..., Loader=..., Dumper=...): ...
def add_path_resolver(tag, path, kind=..., Loader=..., Dumper=...): ...
def add_constructor(
    tag: _Str, constructor: Callable[[Loader, Node], Any], Loader: Loader = ...
): ...
def add_multi_constructor(tag_prefix, multi_constructor, Loader=...): ...
def add_representer(
    data_type: Type[_T], representer: Callable[[_R, _T], Node], Dumper: Type[_R] = ...
) -> None: ...
def add_multi_representer(
    data_type: Type[_T],
    multi_representer: Callable[[_R, _T], Node],
    Dumper: Type[_R] = ...,
) -> None: ...

class YAMLObjectMetaclass(type):
    def __init__(self, name, bases, kwds) -> None: ...

class YAMLObject(metaclass=YAMLObjectMetaclass):
    yaml_loader: Any
    yaml_dumper: Any
    yaml_tag: Any
    yaml_flow_style: Any
    @classmethod
    def from_yaml(cls, loader, node): ...
    @classmethod
    def to_yaml(cls, dumper, data): ...
