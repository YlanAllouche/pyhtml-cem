"""Type stub for wa-scroller component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class scroller(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        orientation: Literal["horizontal", "vertical"] | None = ...,
        without_scrollbar: bool | None = ...,
        without_shadow: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...