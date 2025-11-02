"""Type stub for wa-avatar component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class avatar(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        image: str | None = ...,
        label: str | None = ...,
        initials: str | None = ...,
        loading: Literal["eager", "lazy"] | None = ...,
        shape: Literal["circle", "square", "rounded"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...