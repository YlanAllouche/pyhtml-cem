"""Type stub for wa-breadcrumb component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class breadcrumb(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        label: str | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...