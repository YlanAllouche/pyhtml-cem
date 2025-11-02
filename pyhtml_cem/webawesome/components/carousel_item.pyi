"""Type stub for wa-carousel-item component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class carousel_item(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...