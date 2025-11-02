"""Type stub for wa-intersection-observer component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class intersection_observer(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        root: str | bool | None = ...,
        root_margin: str | None = ...,
        threshold: str | None = ...,
        intersect_class: str | None = ...,
        once: bool | None = ...,
        disabled: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...