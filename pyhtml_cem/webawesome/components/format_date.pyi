"""Type stub for wa-format-date component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class format_date(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        date: str | bool | None = ...,
        weekday: Literal["narrow", "short", "long"] | None = ...,
        era: Literal["narrow", "short", "long"] | None = ...,
        year: Literal["numeric", "2-digit"] | None = ...,
        month: Literal["numeric", "2-digit", "narrow", "short", "long"] | None = ...,
        day: Literal["numeric", "2-digit"] | None = ...,
        hour: Literal["numeric", "2-digit"] | None = ...,
        minute: Literal["numeric", "2-digit"] | None = ...,
        second: Literal["numeric", "2-digit"] | None = ...,
        time_zone_name: Literal["short", "long"] | None = ...,
        time_zone: str | None = ...,
        hour_format: Literal["auto", "12", "24"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...