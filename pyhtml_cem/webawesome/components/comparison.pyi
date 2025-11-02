"""Type stub for wa-comparison component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class comparison(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        position: int | float | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...