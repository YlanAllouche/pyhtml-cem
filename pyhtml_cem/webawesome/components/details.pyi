"""Type stub for wa-details component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class details(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        open: bool | None = ...,
        summary: str | None = ...,
        name: str | None = ...,
        disabled: bool | None = ...,
        appearance: Literal["filled", "outlined", "filled-outlined", "plain"] | None = ...,
        icon_placement: Literal["start", "end"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...