"""Type stub for wa-input component."""

from typing import Literal
from pyhtml import Tag
from pyhtml.__types import ChildrenType, AttributeType


class input(Tag):
    def __init__(
        self,
        *children: ChildrenType,
        title: str | None = ...,
        type: Literal["date", "datetime-local", "email", "number", "password", "search", "tel", "text", "time", "url"] | None = ...,
        value: str | bool | None = ...,
        size: Literal["small", "medium", "large"] | None = ...,
        appearance: Literal["filled", "outlined", "filled-outlined"] | None = ...,
        pill: bool | None = ...,
        label: str | None = ...,
        hint: str | None = ...,
        with_clear: bool | None = ...,
        placeholder: str | None = ...,
        readonly: bool | None = ...,
        password_toggle: bool | None = ...,
        password_visible: bool | None = ...,
        without_spin_buttons: bool | None = ...,
        form: str | bool | None = ...,
        required: bool | None = ...,
        pattern: str | None = ...,
        minlength: int | float | None = ...,
        maxlength: int | float | None = ...,
        min: str | bool | None = ...,
        max: str | bool | None = ...,
        step: Literal["any"] | None = ...,
        autocapitalize: Literal["off", "none", "on", "sentences", "words", "characters"] | None = ...,
        autocorrect: Literal["off", "on"] | None = ...,
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