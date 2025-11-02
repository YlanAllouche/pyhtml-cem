"""Type stub for wa-progress-ring component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class progress_ring(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        value: int | float | None = ...,
        label: str | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...