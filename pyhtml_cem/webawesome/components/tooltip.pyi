"""Type stub for wa-tooltip component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class tooltip(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        placement: Literal["top", "top-start", "top-end", "right", "right-start", "right-end", "bottom", "bottom-start", "bottom-end", "left", "left-start", "left-end"] | None = ...,
        disabled: bool | None = ...,
        distance: int | float | None = ...,
        open: bool | None = ...,
        skidding: int | float | None = ...,
        show_delay: int | float | None = ...,
        hide_delay: int | float | None = ...,
        trigger: str | None = ...,
        without_arrow: bool | None = ...,
        for_: str | bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...