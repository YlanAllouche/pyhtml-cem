"""Type stub for wa-dropdown component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class dropdown(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        open: bool | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        placement: Literal["top", "top-start", "top-end", "bottom", "bottom-start", "bottom-end", "right", "right-start", "right-end", "left", "left-start", "left-end"] | None = ...,
        distance: int | float | None = ...,
        skidding: int | float | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...