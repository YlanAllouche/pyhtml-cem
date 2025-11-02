"""Type stub for wa-animation component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class animation(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        name: str | None = ...,
        play: bool | None = ...,
        delay: int | float | None = ...,
        direction: str | bool | None = ...,
        duration: int | float | None = ...,
        easing: str | None = ...,
        end_delay: int | float | None = ...,
        fill: str | bool | None = ...,
        iterations: int | float | None = ...,
        iteration_start: int | float | None = ...,
        playback_rate: int | float | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...