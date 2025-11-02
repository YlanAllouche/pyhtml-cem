"""Type stub for wa-color-picker component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class color_picker(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        value: str | bool | None = ...,
        with_label: bool | None = ...,
        with_hint: bool | None = ...,
        label: str | None = ...,
        hint: str | None = ...,
        format: Literal["hex", "rgb", "hsl", "hsv"] | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        without_format_toggle: bool | None = ...,
        name: str | bool | None = ...,
        disabled: bool | None = ...,
        open: bool | None = ...,
        opacity: bool | None = ...,
        uppercase: bool | None = ...,
        swatches: str | bool | None = ...,
        form: str | bool | None = ...,
        required: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...