"""Type stub for wa-format-number component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class format_number(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        value: int | float | None = ...,
        type: Literal["currency", "decimal", "percent"] | None = ...,
        without_grouping: bool | None = ...,
        currency: str | None = ...,
        currency_display: Literal["symbol", "narrowSymbol", "code", "name"] | None = ...,
        minimum_integer_digits: int | float | None = ...,
        minimum_fraction_digits: int | float | None = ...,
        maximum_fraction_digits: int | float | None = ...,
        minimum_significant_digits: int | float | None = ...,
        maximum_significant_digits: int | float | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...