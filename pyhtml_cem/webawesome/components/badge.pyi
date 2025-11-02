"""Type stub for wa-badge component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class badge(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        variant: Literal["brand", "neutral", "success", "warning", "danger"] | None = ...,
        appearance: Literal["accent", "filled", "outlined", "filled-outlined"] | None = ...,
        pill: bool | None = ...,
        attention: Literal["none", "pulse", "bounce"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...