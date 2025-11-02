"""Type stub for wa-card component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class card(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        appearance: Literal["accent", "filled", "outlined", "plain"] | None = ...,
        with_header: bool | None = ...,
        with_media: bool | None = ...,
        with_footer: bool | None = ...,
        orientation: Literal["horizontal", "vertical"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...