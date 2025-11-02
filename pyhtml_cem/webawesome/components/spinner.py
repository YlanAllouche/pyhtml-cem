"""
wa-spinner component.
"""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class spinner(Tag):
    """
    wa-spinner web component.
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
        return "wa-spinner"


__all__ = [
    "spinner",
]