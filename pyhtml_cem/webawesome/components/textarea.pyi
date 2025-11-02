"""Type stub for wa-textarea component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class textarea(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        title: str | None = ...,
        name: str | bool | None = ...,
        value: str | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        appearance: Literal["filled", "outlined", "filled-outlined"] | None = ...,
        label: str | None = ...,
        hint: str | None = ...,
        placeholder: str | None = ...,
        rows: int | float | None = ...,
        resize: Literal["none", "vertical", "horizontal", "both", "auto"] | None = ...,
        disabled: bool | None = ...,
        readonly: bool | None = ...,
        form: str | bool | None = ...,
        required: bool | None = ...,
        minlength: int | float | None = ...,
        maxlength: int | float | None = ...,
        autocapitalize: Literal["off", "none", "on", "sentences", "words", "characters"] | None = ...,
        autocorrect: str | None = ...,
        autocomplete: str | None = ...,
        autofocus: bool | None = ...,
        enterkeyhint: Literal["enter", "done", "go", "next", "previous", "search", "send"] | None = ...,
        spellcheck: bool | None = ...,
        inputmode: Literal["none", "text", "decimal", "numeric", "tel", "search", "email", "url"] | None = ...,
        with_label: bool | None = ...,
        with_hint: bool | None = ...,
        **attributes: AttributeType,
    ) -> None: ...

    def _get_tag_name(self) -> str: ...