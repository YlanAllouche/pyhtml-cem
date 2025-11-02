"""Type stub for wa-tree component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class tree(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        selection: Literal["single", "multiple", "leaf"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...