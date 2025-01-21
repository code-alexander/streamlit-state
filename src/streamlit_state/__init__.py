"""`streamlit-state` package.

A thin wrapper for session state in Streamlit.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, overload

if TYPE_CHECKING:
    from collections.abc import Callable, MutableMapping
    from types import EllipsisType
    from typing import Any

    from streamlit.elements.lib.utils import Key


import streamlit as st

__all__ = ['state']


class State[A](Protocol):
    @overload
    def __call__(self) -> A: ...

    @overload
    def __call__[B](self, updater: Callable[[A], B]) -> State[B]: ...

    @overload
    def __call__[B](self, updater: B) -> State[B]: ...

    def __call__[B](self, updater: Callable[[A], B] | B | EllipsisType = ...) -> A | State[B]: ...


@overload
def state(key: Key, initial: None = None, mapping: MutableMapping[Key, Any] = st.session_state) -> State[None]: ...


@overload
def state[A](key: Key, initial: A, mapping: MutableMapping[Key, Any] = st.session_state) -> State[A]: ...


def state[A](
    key: Key, initial: A | None = None, mapping: MutableMapping[Key, Any] = st.session_state
) -> State[A] | State[None]:
    """Returns a function that can get or set a session state variable.

    Args:
        key (Key): The session state key.
        initial (A | None, optional):
            The initial value of the session state variable. Defaults to `None`.
        mapping (MutableMapping[Key, Any], optional):
            The session state object. Defaults to `st.session_state`.

    Returns:
        State[A] | State[None]: A function that can get or set a session state variable.
    """
    if key not in mapping:
        mapping[key] = initial

    @overload
    def apply() -> A: ...

    @overload
    def apply[B](updater: Callable[[A], B]) -> State[B]: ...

    @overload
    def apply[B](updater: B) -> State[B]: ...

    def apply[B](
        updater: Callable[[A], B] | B | EllipsisType = ...,
    ) -> A | State[A] | State[B]:
        """Gets or sets a session state variable.

        Args:
            updater (Callable[[A], B] | B | EllipsisType, optional):
                A value or function to update the state with.
                If not provided, the current state is returned.
                Defaults to `...`.

        Returns:
            A | State[A] | State[B]:
                The current state value if `updater` is not provided,
                else a function that can get or set the state variable.
        """
        if updater is ...:
            return mapping[key]
        mapping[key] = updater(mapping[key]) if callable(updater) else updater
        return apply

    return apply


def callback[A, B](fn: State[A], updater: B | Callable[[A], B]) -> None:
    """Applies a state change without returning a function.

    This is useful for Streamlit callbacks, which expect `Callable[..., None]`.

    Args:
        fn (State[A]): A function that can get or set a session state variable.
        updater (B | Callable[[A], B]): A value or function to update the state with.
    """
    fn(updater)
