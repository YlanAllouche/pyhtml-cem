"""Type stub for wa-copy-button component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class copy_button(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        value: str | None = ...,
        from_: str | None = ...,
        disabled: bool | None = ...,
        copy_label: str | None = ...,
        success_label: str | None = ...,
        error_label: str | None = ...,
        feedback_duration: int | float | None = ...,
        tooltip_placement: Literal["top", "right", "bottom", "left"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...