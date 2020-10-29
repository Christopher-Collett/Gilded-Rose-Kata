from numpy import loadtxt
import pytest

from Gilded_Rose import GildedRose, Item, make_item


def get_test_cases(filename):
    test_cases_raw = loadtxt(filename, dtype=str, delimiter='\t', skiprows=1)
    test_cases = []
    for test_case in test_cases_raw:
        name, sell_in, quality, expected_sell_in, expected_quality = test_case
        test_case = (name, int(sell_in), int(quality),
                     int(expected_sell_in), int(expected_quality))
        test_cases.append(test_case)
    return test_cases


@pytest.mark.parametrize('name, sell_in, quality,' +
                         'expected_sell_in, expected_quality',
                         get_test_cases('Gilded_Rose_Example.csv'))
def test_predefined_quality_standard(name, sell_in, quality,
                                     expected_sell_in, expected_quality):
    item = make_item(name, sell_in, quality)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


def test_Item_repr():
    item = Item('+5 Dexterity Vest', -1, 5)
    assert str(item) == '+5 Dexterity Vest, -1, 5'
