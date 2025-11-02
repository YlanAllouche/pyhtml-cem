"""Type stub for wa-format-bytes component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class format_bytes(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        value: int | float | None = ...,
        unit: Literal["byte", "bit"] | None = ...,
        display: Literal["long", "short", "narrow"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...