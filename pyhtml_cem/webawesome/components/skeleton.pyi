"""Type stub for wa-skeleton component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class skeleton(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        effect: Literal["pulse", "sheen", "none"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...