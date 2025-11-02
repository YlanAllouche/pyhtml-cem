"""Type stub for wa-slider component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class slider(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        label: str | None = ...,
        hint: str | None = ...,
        name: str | None = ...,
        min_value: int | float | None = ...,
        max_value: int | float | None = ...,
        value: int | float | None = ...,
        range: bool | None = ...,
        disabled: bool | None = ...,
        readonly: bool | None = ...,
        orientation: Literal["horizontal", "vertical"] | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        indicator_offset: int | float | None = ...,
        form: str | bool | None = ...,
        min: int | float | None = ...,
        max: int | float | None = ...,
        step: int | float | None = ...,
        required: bool | None = ...,
        autofocus: bool | None = ...,
        tooltip_distance: int | float | None = ...,
        tooltip_placement: Literal["top", "right", "bottom", "left"] | None = ...,
        with_markers: bool | None = ...,
        with_tooltip: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...