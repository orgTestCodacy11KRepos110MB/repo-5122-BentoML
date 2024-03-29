from typing import Any
from typing_extensions import Literal
from .Image import Image

QImage = Any
QPixmap = Any
qt_versions: Any
qt_is_installed: bool
qt_version: Any

def rgb(r: int, g: int, b: int, a: int = ...) -> int: ...
def fromqimage(im: Image | QImage) -> Image: ...
def fromqpixmap(im: Image | QImage) -> Image: ...
def align8to32(bytes: bytes, width: int, mode: Literal["1", "L", "P"]) -> bytes: ...

class ImageQt(QImage):
    def __init__(self, im: Image) -> None: ...

def toqimage(im: Image) -> ImageQt: ...
def toqpixmap(im: Image) -> QPixmap: ...
