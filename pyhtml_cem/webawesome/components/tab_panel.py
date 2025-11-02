"""
wa-tab-panel component.
"""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class tab_panel(Tag):
    """
    wa-tab-panel web component.

    Args:
        *children: Child elements and text content
        name: The tab panel's name.
        active: When true, the tab panel will be shown.
        **attributes: Additional HTML attributes

    Slots:
        : The tab panel's content.
    """
    def __init__(
        self,
        *children: ChildrenType,
        name: str | None = None,
        active: bool | None = None,
        **attributes: AttributeType,
    ) -> None:
        # Build attributes dict, filtering out None values
        attributes = attributes.copy()
        attributes.update({
            'name': name,
            'active': active,
        })
        # Filter out None values and convert numbers to strings
        attributes = {
            k: str(v) if isinstance(v, (int, float)) else v
            for k, v in attributes.items()
            if v is not None
        }
        super().__init__(*children, **attributes)

    def _get_tag_name(self) -> str:
        return "wa-tab-panel"


__all__ = [
    "tab_panel",
]