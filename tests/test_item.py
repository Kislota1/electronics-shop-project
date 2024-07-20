"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import os
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


def test_name_setter():
    item = Item('Test Item', 100.0, 5)

    item.name = "Short"
    assert item.name == "Short"

    # Проверка обрезки длинного имени
    long_name = "This is a very long name"
    item.name = long_name
    assert item.name == long_name[:10]

@pytest.mark.parametrize("s, expected", [
    ("10", 10),
    ("15.5", 15),
    ("20.9", 20),
    ("5.7", 5),
    ("100.0", 100),
])
def test_string_to_number(s, expected):
    assert Item.string_to_number(s) == expected


@pytest.fixture
def setup_test_csv():
    test_csv_content = """
    name,price,quantity
    Тестовый товар 1,50.0,10
    Тестовый товар 2,75.5,5
    """
    with open('test_items.csv', 'w', encoding='utf-8') as f:
        f.write(test_csv_content)

    yield 'test_items.csv'

    os.remove('test_items.csv')


def test_instantiate_from_csv(setup_test_csv):
    file_path = setup_test_csv
    Item.instantiate_from_csv(file_path)

    assert len(Item.all) == 2

    item1 = Item.all[0]
    assert item1.name == "Тестовый товар 1"
    assert item1.price == 50.0
    assert item1.quantity == 10

    item2 = Item.all[1]
    assert item2.name == "Тестовый товар 2"
    assert item2.price == 75.5
    assert item2.quantity == 5

def test_repr_from_item():
    item1 = Item("somthing", 22000, 9)
    item2 = Item("Алибаба", 4, 13)

    assert repr(item1) == "Item('somthing', 22000, 9)"
    assert repr(item2) == "Item('Алибаба', 4, 13)"

def test_str_from_item():
    item1 = Item("somthing", 22000, 9)
    item2 = Item("Алибаба", 4, 13)

    assert str(item1) == 'somthing'
    assert str(item2) == 'Алибаба'
