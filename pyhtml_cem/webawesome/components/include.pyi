"""Type stub for wa-include component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class include(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        src: str | None = ...,
        mode: Literal["cors", "no-cors", "same-origin"] | None = ...,
        allow_scripts: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...