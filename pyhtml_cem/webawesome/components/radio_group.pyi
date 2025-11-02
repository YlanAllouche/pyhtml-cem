"""Type stub for wa-radio-group component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class radio_group(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        label: str | None = ...,
        hint: str | None = ...,
        name: str | bool | None = ...,
        disabled: bool | None = ...,
        orientation: Literal["horizontal", "vertical"] | None = ...,
        value: str | bool | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        required: bool | None = ...,
        with_label: bool | None = ...,
        with_hint: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...