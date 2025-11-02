"""Type stub for wa-tab-panel component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class tab_panel(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        name: str | None = ...,
        active: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...