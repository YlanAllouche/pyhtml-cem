"""Type stub for wa-split-panel component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class split_panel(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        position: int | float | None = ...,
        position_in_pixels: int | float | None = ...,
        orientation: Literal["horizontal", "vertical"] | None = ...,
        disabled: bool | None = ...,
        primary: Literal["start", "end"] | None = ...,
        snap: str | bool | None = ...,
        snap_threshold: int | float | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...