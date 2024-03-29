import typing
from typing import IO, List, Optional, Text
from .base import FS

if typing.TYPE_CHECKING: ...

def remove_empty(fs: FS, path: Text) -> None: ...
def copy_file_data(
    src_file: IO, dst_file: IO, chunk_size: Optional[int] = ...
) -> None: ...
def get_intermediate_dirs(fs: FS, dir_path: Text) -> List[Text]: ...
def is_thread_safe(*filesystems: FS) -> bool: ...
