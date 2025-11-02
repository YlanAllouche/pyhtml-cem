"""Type stub for wa-button component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class button(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        title: str | None = ...,
        variant: Literal["neutral", "brand", "success", "warning", "danger"] | None = ...,
        appearance: Literal["accent", "filled", "outlined", "filled-outlined", "plain"] | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        with_caret: bool | None = ...,
        disabled: bool | None = ...,
        loading: bool | None = ...,
        pill: bool | None = ...,
        type: Literal["button", "submit", "reset"] | None = ...,
        name: str | None = ...,
        value: str | None = ...,
        href: str | None = ...,
        target: Literal["_blank", "_parent", "_self", "_top"] | None = ...,
        rel: str | bool | None = ...,
        download: str | bool | None = ...,
        form: str | bool | None = ...,
        formaction: str | None = ...,
        formenctype: Literal["application/x-www-form-urlencoded", "multipart/form-data", "text/plain"] | None = ...,
        formmethod: Literal["post", "get"] | None = ...,
        formnovalidate: bool | None = ...,
        formtarget: Literal["_self", "_blank", "_parent", "_top"] | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...