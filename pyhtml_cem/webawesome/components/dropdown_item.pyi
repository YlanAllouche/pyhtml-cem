"""Type stub for wa-dropdown-item component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class dropdown_item(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        variant: Literal["danger", "default"] | None = ...,
        value: str | None = ...,
        type: Literal["normal", "checkbox"] | None = ...,
        checked: bool | None = ...,
        disabled: bool | None = ...,
        submenuOpen: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...