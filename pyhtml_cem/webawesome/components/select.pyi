"""Type stub for wa-select component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class select(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        name: str | None = ...,
        value: str | bool | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        placeholder: str | None = ...,
        multiple: bool | None = ...,
        max_options_visible: int | float | None = ...,
        disabled: bool | None = ...,
        with_clear: bool | None = ...,
        open: bool | None = ...,
        appearance: Literal["filled", "outlined", "filled-outlined"] | None = ...,
        pill: bool | None = ...,
        label: str | None = ...,
        placement: Literal["top", "bottom"] | None = ...,
        hint: str | None = ...,
        with_label: bool | None = ...,
        with_hint: bool | None = ...,
        form: str | bool | None = ...,
        required: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...