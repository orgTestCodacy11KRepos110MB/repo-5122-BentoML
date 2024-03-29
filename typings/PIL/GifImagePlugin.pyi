from typing import Any
from .ImageFile import ImageFile

class GifImageFile(ImageFile):
    format: str
    format_description: str
    global_palette: Any
    def data(self): ...
    @property
    def n_frames(self): ...
    @property
    def is_animated(self): ...
    im: Any
    def seek(self, frame) -> None: ...
    def tell(self): ...

RAWMODE: Any

def get_interlace(im): ...
def getheader(im, palette: Any | None = ..., info: Any | None = ...): ...
def getdata(im, offset=..., **params): ...
