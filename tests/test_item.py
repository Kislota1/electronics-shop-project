"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def test_item_initialization():
    item = Item('Test Item', 100.0, 5)
    assert item.name == "Test Item"
    assert item.price == 100.0
    assert item.quantity == 5

def test_calculate_total_price():
    item = Item("Test Item", 100.0, 5)
    assert item.calculate_total_price() == 500.0

def test_apply_discount():
    item = Item("Test Item", 100.0, 5)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 80.0

def test_apply_discount_with_default_rate():
    item = Item("Test Item", 100.0, 5)
    item.apply_discount()
    assert item.price == 100.0