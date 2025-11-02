"""Type stub for wa-qr-code component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class qr_code(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        value: str | None = ...,
        label: str | None = ...,
        size: int | float | None = ...,
        fill: str | None = ...,
        background: str | None = ...,
        radius: int | float | None = ...,
        error_correction: Literal["L", "M", "Q", "H"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...