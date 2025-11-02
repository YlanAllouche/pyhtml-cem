"""
wa-carousel-item component.
"""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class carousel_item(Tag):
    """
    wa-carousel-item web component.

    Slots:
        : The carousel item's content..
    """
    def __init__(
        self,
        *children: ChildrenType,
        **attributes: AttributeType,
    ) -> None:
        # Build attributes dict, filtering out None values
        attributes = attributes.copy()
        attributes.update({
        })
        # Filter out None values and convert numbers to strings
        attributes = {
            k: str(v) if isinstance(v, (int, float)) else v
            for k, v in attributes.items()
            if v is not None
        }
        super().__init__(*children, **attributes)

    def _get_tag_name(self) -> str:
        return "wa-carousel-item"


__all__ = [
    "carousel_item",
]