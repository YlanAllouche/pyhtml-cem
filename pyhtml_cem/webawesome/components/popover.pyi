"""Type stub for wa-popover component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class popover(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        placement: Literal["top", "top-start", "top-end", "right", "right-start", "right-end", "bottom", "bottom-start", "bottom-end", "left", "left-start", "left-end"] | None = ...,
        open: bool | None = ...,
        distance: int | float | None = ...,
        skidding: int | float | None = ...,
        for_: str | bool | None = ...,
        without_arrow: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...