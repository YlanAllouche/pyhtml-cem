"""Type stub for wa-tab-group component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class tab_group(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        active: str | None = ...,
        placement: Literal["top", "bottom", "start", "end"] | None = ...,
        activation: Literal["auto", "manual"] | None = ...,
        without_scroll_controls: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...