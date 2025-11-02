"""Type stub for wa-callout component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class callout(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        variant: Literal["brand", "neutral", "success", "warning", "danger"] | None = ...,
        appearance: Literal["accent", "filled", "outlined", "plain", "filled-outlined"] | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...