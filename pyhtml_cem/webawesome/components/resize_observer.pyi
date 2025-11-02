"""Type stub for wa-resize-observer component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class resize_observer(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        disabled: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...