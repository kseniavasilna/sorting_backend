import pytest
from main import sort_values

def test_sort_basic():
    values = [
        {"value":"green", "meta":"a"},
        {"value":"red", "meta":"b"},
        {"value":"blue", "meta":"c"}]
    order_rule = {"red": "0", "blue": "1", "green": "2"}

    result = sort_values(values, order_rule)

    assert result == [{"value":"red", "meta":"b"}, {"value":"blue", "meta":"c"}, {"value":"green", "meta":"a"}]


def test_sort_with_duplicates():
    values = [
        {"value":"green", "meta":"a"},
        {"value":"red", "meta":"b"},
        {"value":"red", "meta":"b"},
        {"value":"blue", "meta":"c"}]
    order_rule = {"red": "0", "blue": "1", "green": "2"}

    result = sort_values(values, order_rule)

    assert result == [{"value":"red", "meta":"b"}, {"value":"red", "meta":"b"}, {"value":"blue", "meta":"c"}, {"value":"green", "meta":"a"}]


def test_sort_empty_values():
    values = []
    order_rule = {"red": "0"}

    result = sort_values(values, order_rule)

    assert result == []


def test_sort_single_value():
    values = [{"value":"blue", "meta":"c"}]
    order_rule = {"blue": "1"}

    result = sort_values(values, order_rule)

    assert result == [{"value":"blue", "meta":"c"}]

def test_missing_color_in_order_rule():
    values = [{"value":"red", "meta":"b"}]
    order_rule = {}

    with pytest.raises(KeyError):
        sort_values(values, order_rule)