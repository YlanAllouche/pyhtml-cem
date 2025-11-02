"""Type stub for wa-button-group component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class button_group(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        label: str | None = ...,
        orientation: Literal["horizontal", "vertical"] | None = ...,
        variant: Literal["neutral", "brand", "success", "warning", "danger"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...