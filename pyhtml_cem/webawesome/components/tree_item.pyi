"""Type stub for wa-tree-item component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class tree_item(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        expanded: bool | None = ...,
        selected: bool | None = ...,
        disabled: bool | None = ...,
        lazy: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...