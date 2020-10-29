# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                item.update_aged_brie_quality()
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.udpate_backstage_passes_quality()
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.update_sulfuras_quality()
            else:
                item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_aged_brie_quality(self):
        if self.quality_under_50():
            self.increment_quality()
        self.decrement_sell_in()
        if self.sell_in_under_0() and self.quality_under_50():
            self.increment_quality()

    def udpate_backstage_passes_quality(self):
        if self.quality_under_50():
            self.increment_quality()
            if self.sell_in_under_11() and self.quality_under_50():
                self.increment_quality()
            if self.sell_in_under_6() and self.quality_under_50():
                self.increment_quality()
        self.decrement_sell_in()
        if self.sell_in_under_0():
            self.reset_quality()

    def update_sulfuras_quality(self):
        pass

    def update_quality(self):
        if self.quality_over_0():
            self.decrement_quality()
        self.decrement_sell_in()
        if self.sell_in_under_0() and self.quality_over_0():
            self.decrement_quality()

    def sell_in_under_0(self):
        return self.sell_in < 0

    def sell_in_under_6(self):
        return self.sell_in < 6

    def sell_in_under_11(self):
        return self.sell_in < 11

    def decrement_sell_in(self):
        self.sell_in -= 1

    def quality_over_0(self):
        return self.quality > 0

    def quality_under_50(self):
        return self.quality < 50

    def increment_quality(self):
        self.quality += 1

    def decrement_quality(self):
        self.quality -= 1

    def reset_quality(self):
        self.quality = 0
