"""Type stub for wa-popup component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class popup(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        anchor: str | bool | None = ...,
        active: bool | None = ...,
        placement: Literal["top", "top-start", "top-end", "bottom", "bottom-start", "bottom-end", "right", "right-start", "right-end", "left", "left-start", "left-end"] | None = ...,
        boundary: Literal["viewport", "scroll"] | None = ...,
        distance: int | float | None = ...,
        skidding: int | float | None = ...,
        arrow: bool | None = ...,
        arrow_placement: Literal["start", "end", "center", "anchor"] | None = ...,
        arrow_padding: int | float | None = ...,
        flip: bool | None = ...,
        flip_fallback_placements: str | None = ...,
        flip_fallback_strategy: Literal["best-fit", "initial"] | None = ...,
        flipBoundary: str | bool | None = ...,
        flip_padding: int | float | None = ...,
        shift: bool | None = ...,
        shiftBoundary: str | bool | None = ...,
        shift_padding: int | float | None = ...,
        auto_size: Literal["horizontal", "vertical", "both"] | None = ...,
        sync: Literal["width", "height", "both"] | None = ...,
        autoSizeBoundary: str | bool | None = ...,
        auto_size_padding: int | float | None = ...,
        hover_bridge: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...