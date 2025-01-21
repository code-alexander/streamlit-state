"""Tests for getting and setting state variables."""

from src.streamlit_state import callback, state


def test_dict_initial_state() -> None:
    """Test that the initial state is set correctly."""
    x = state('x', 0, {})
    assert x() == 0


def test_dict_initial_state_none_explicit() -> None:
    """Test that the initial state can be explicitly set to None."""
    x = state('x', None, {})
    assert x() is None


def test_dict_initial_state_none_implicit() -> None:
    """Test that the initial state can be implicitly set to None."""
    x = state('x', mapping={})
    assert x() is None


def test_dict_set_state_value() -> None:
    """Test that the state can be updated with a value."""
    x = state('x', 0, {})
    x = x(1)
    assert x() == 1


def test_dict_set_state_function() -> None:
    """Test that the state can be updated with a function."""
    x = state('x', 0, {})
    x = x(lambda x: x + 1)
    assert x() == 1


def test_dict_set_state_cast() -> None:
    """Test that the state can be cast to a new type."""
    x = state('x', 0, {})
    x = x(str)
    assert x() == '0'


def test_dict_callback_set_state_value() -> None:
    """Test that the state can be updated with a value in a callback."""
    x = state('x', 0, {})
    r = callback(x, 1)
    assert r is None
    assert x() == 1


def test_dict_callback_set_state_function() -> None:
    """Test that the state can be updated with a function in a callback."""
    x = state('x', 0, {})
    r = callback(x, lambda x: x + 1)
    assert r is None
    assert x() == 1


def test_dict_callback_set_state_cast() -> None:
    """Test that the state can be cast to a new type in a callback."""
    x = state('x', 0, {})
    r = callback(x, str)
    assert r is None
    assert x() == '0'
