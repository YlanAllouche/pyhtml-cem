"""Type stub for wa-switch component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class switch(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        title: str | None = ...,
        name: str | bool | None = ...,
        value: str | bool | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        disabled: bool | None = ...,
        checked: bool | None = ...,
        form: str | bool | None = ...,
        required: bool | None = ...,
        hint: str | None = ...,
        with_hint: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...