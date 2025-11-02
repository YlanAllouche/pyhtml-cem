"""Type stub for wa-radio component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class radio(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        form: str | bool | None = ...,
        value: str | None = ...,
        appearance: Literal["default", "button"] | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        disabled: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...