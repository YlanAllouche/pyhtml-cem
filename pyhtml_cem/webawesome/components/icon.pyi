"""Type stub for wa-icon component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class icon(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        name: str | bool | None = ...,
        family: str | None = ...,
        variant: str | None = ...,
        auto_width: bool | None = ...,
        swap_opacity: bool | None = ...,
        src: str | bool | None = ...,
        label: str | None = ...,
        library: str | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...