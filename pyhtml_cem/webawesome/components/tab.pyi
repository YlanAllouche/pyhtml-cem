"""Type stub for wa-tab component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class tab(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        panel: str | None = ...,
        disabled: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...