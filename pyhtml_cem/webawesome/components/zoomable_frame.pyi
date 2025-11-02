"""Type stub for wa-zoomable-frame component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class zoomable_frame(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        src: str | None = ...,
        srcdoc: str | None = ...,
        allowfullscreen: bool | None = ...,
        loading: Literal["eager", "lazy"] | None = ...,
        referrerpolicy: str | None = ...,
        sandbox: str | None = ...,
        zoom: int | float | None = ...,
        zoom_levels: str | None = ...,
        without_controls: bool | None = ...,
        without_interaction: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...