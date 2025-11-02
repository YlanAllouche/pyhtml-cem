"""Type stub for wa-carousel component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class carousel(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        loop: bool | None = ...,
        slides: int | float | None = ...,
        currentSlide: int | float | None = ...,
        navigation: bool | None = ...,
        pagination: bool | None = ...,
        autoplay: bool | None = ...,
        autoplay_interval: int | float | None = ...,
        slides_per_page: int | float | None = ...,
        slides_per_move: int | float | None = ...,
        orientation: Literal["horizontal", "vertical"] | None = ...,
        mouse_dragging: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...