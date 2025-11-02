"""Type stub for wa-dialog component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class dialog(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        open: bool | None = ...,
        label: str | None = ...,
        without_header: bool | None = ...,
        light_dismiss: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...