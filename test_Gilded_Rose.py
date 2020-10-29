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


def test_quality_and_sell_in_decrease_normally():
    test_before_and_after('+5 Dexterity Vest', 5, 5, 4, 4)


def test_quality_decreases_by_2_after_sell_in_date():
    test_before_and_after('+5 Dexterity Vest', 0, 5, -1, 3)


def test_quality_isnt_negative():
    test_before_and_after('+5 Dexterity Vest', 5, 0, 4, 0)


def test_aged_brie_increases_in_quality():
    test_before_and_after('Aged Brie', 5, 10, 4, 11)


def test_aged_brie_doesnt_go_over_50():
    test_before_and_after('Aged Brie', 5, 50, 4, 50)


def test_sulfuras_doesnt_change():
    test_before_and_after('Sulfuras, Hand of Ragnaros',
                          0, 80, 0, 80)


def test_backstage_increases_in_quality():
    test_before_and_after('Backstage passes to a TAFKAL80ETC concert',
                          20, 10, 19, 11)


def test_backstage_doesnt_go_over_50():
    test_before_and_after('Backstage passes to a TAFKAL80ETC concert',
                          5, 50, 4, 50)


def test_backstage_increase_by_2_on_day_10():
    test_before_and_after('Backstage passes to a TAFKAL80ETC concert',
                          11, 10, 10, 12)


def test_backstage_increase_by_2_after_day_10():
    test_before_and_after('Backstage passes to a TAFKAL80ETC concert',
                          10, 10, 9, 12)


def test_backstage_increase_by_3_on_day_5():
    test_before_and_after('Backstage passes to a TAFKAL80ETC concert',
                          6, 10, 5, 13)


def test_backstage_increase_by_3_after_day_5():
    test_before_and_after('Backstage passes to a TAFKAL80ETC concert',
                          5, 10, 4, 13)


def test_backstage_quality_is_0_after_day_0():
    test_before_and_after('Backstage passes to a TAFKAL80ETC concert',
                          0, 10, -1, 0)


def test_conjured_degrade_by_2_normally():
    test_before_and_after('Conjured', 5, 10, 4, 8)


def test_conjured_degrade_by_4_after_day_0():
    test_before_and_after('Conjured', 0, 10, -1, 6)


@pytest.mark.parametrize('name, sell_in, quality,' +
                         'expected_sell_in, expected_quality',
                         get_test_cases('Gilded_Rose_Example.csv'))
def test_before_and_after(name, sell_in, quality,
                          expected_sell_in, expected_quality):
    item = make_item(name, sell_in, quality)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


def test_Item_repr():
    item = Item('+5 Dexterity Vest', -1, 5)
    assert str(item) == '+5 Dexterity Vest, -1, 5'
