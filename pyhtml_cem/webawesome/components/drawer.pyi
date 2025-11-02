"""Type stub for wa-drawer component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class drawer(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        open: bool | None = ...,
        label: str | None = ...,
        placement: Literal["top", "end", "bottom", "start"] | None = ...,
        without_header: bool | None = ...,
        light_dismiss: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...