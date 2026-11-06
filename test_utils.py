import pytest
from utils import format_price, parse_config

def test_format_price():
    assert format_price(1234.56) == "$1,234.56"

def test_parse_config_empty():
    assert parse_config("") == {}

def test_parse_config_value():
    assert parse_config("x") == {"raw": "x"}
