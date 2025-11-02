"""Type stub for wa-mutation-observer component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class mutation_observer(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        attr: str | None = ...,
        attr_old_value: bool | None = ...,
        char_data: bool | None = ...,
        char_data_old_value: bool | None = ...,
        child_list: bool | None = ...,
        disabled: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...