from typing import Any
from .Image import Image, _Box

def grab(
    bbox: _Box | None = ...,
    include_layered_windows: bool = ...,
    all_screens: bool = ...,
    xdisplay: Any | None = ...,
) -> Image: ...
def grabclipboard() -> Image | None: ...
