"""Type stub for wa-breadcrumb-item component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class breadcrumb_item(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        href: str | bool | None = ...,
        target: Literal["_blank", "_parent", "_self", "_top"] | None = ...,
        rel: str | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...