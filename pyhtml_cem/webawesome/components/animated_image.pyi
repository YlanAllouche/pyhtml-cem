"""Type stub for wa-animated-image component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class animated_image(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        src: str | None = ...,
        alt: str | None = ...,
        play: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...