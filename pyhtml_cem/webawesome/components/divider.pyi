"""Type stub for wa-divider component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class divider(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        orientation: Literal["horizontal", "vertical"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...