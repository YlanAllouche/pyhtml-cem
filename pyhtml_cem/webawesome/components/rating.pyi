"""Type stub for wa-rating component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class rating(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        label: str | None = ...,
        value: int | float | None = ...,
        max: int | float | None = ...,
        precision: int | float | None = ...,
        readonly: bool | None = ...,
        disabled: bool | None = ...,
        getSymbol: str | bool | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...