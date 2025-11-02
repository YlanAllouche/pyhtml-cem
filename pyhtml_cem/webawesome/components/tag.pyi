"""Type stub for wa-tag component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class tag(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        variant: Literal["brand", "neutral", "success", "warning", "danger"] | None = ...,
        appearance: Literal["accent", "filled", "outlined", "filled-outlined"] | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        pill: bool | None = ...,
        with_remove: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...