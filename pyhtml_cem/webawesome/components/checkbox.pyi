"""Type stub for wa-checkbox component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class checkbox(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        title: str | None = ...,
        name: str | None = ...,
        value: str | bool | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        disabled: bool | None = ...,
        indeterminate: bool | None = ...,
        checked: bool | None = ...,
        form: str | bool | None = ...,
        required: bool | None = ...,
        hint: str | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...