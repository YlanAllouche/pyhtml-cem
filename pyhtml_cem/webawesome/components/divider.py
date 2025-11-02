"""
wa-divider component.
"""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class divider(Tag):
    """
    wa-divider web component.

    Args:
        *children: Child elements and text content
        orientation: Sets the divider's orientation.
        **attributes: Additional HTML attributes
    """
    def __init__(
        self,
        *children: ChildrenType,
        orientation: Literal["horizontal", "vertical"] | None = None,
        **attributes: AttributeType,
    ) -> None:
        # Build attributes dict, filtering out None values
        attributes = attributes.copy()
        attributes.update({
            'orientation': orientation,
        })
        # Filter out None values and convert numbers to strings
        attributes = {
            k: str(v) if isinstance(v, (int, float)) else v
            for k, v in attributes.items()
            if v is not None
        }
        super().__init__(*children, **attributes)

    def _get_tag_name(self) -> str:
        return "wa-divider"


__all__ = [
    "divider",
]