"""Type stub for wa-relative-time component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class relative_time(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        date: str | bool | None = ...,
        format: Literal["long", "short", "narrow"] | None = ...,
        numeric: Literal["always", "auto"] | None = ...,
        sync: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...