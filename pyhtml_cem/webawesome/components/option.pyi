"""Type stub for wa-option component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class option(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        value: str | None = ...,
        disabled: bool | None = ...,
        selected: bool | None = ...,
        label: str | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...