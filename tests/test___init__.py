"""WWUCS Bot tests."""

import pytest

import wwucs.bot


@pytest.mark.parametrize("attr", ["__author__", "__email__", "__version__"])
def test_attributes(attr):
    """TODO"""
    assert hasattr(wwucs.bot, attr)
