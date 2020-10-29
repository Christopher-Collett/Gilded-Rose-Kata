# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if self.quality_over_0(item):
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        self.decrement_quality(item)
            else:
                if self.quality_under_50(item):
                    self.increment_quality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if self.sell_in_under_11(item):
                            if self.quality_under_50(item):
                                self.increment_quality(item)
                        if self.sell_in_under_6(item):
                            if self.quality_under_50(item):
                                self.increment_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                self.decrement_sell_in(item)
            if self.sell_in_under_0(item):
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if self.quality_over_0(item):
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                self.decrement_quality(item)
                    else:
                        self.reset_quality(item)
                else:
                    if self.quality_under_50(item):
                        self.increment_quality(item)

    def sell_in_under_0(self, item):
        return item.sell_in < 0

    def sell_in_under_6(self, item):
        return item.sell_in < 6

    def sell_in_under_11(self, item):
        return item.sell_in < 11

    def decrement_sell_in(self, item):
        item.sell_in -= 1

    def quality_over_0(self, item):
        return item.quality > 0

    def quality_under_50(self, item):
        return item.quality < 50

    def increment_quality(self, item):
        item.quality += 1

    def decrement_quality(self, item):
        item.quality -= 1

    def reset_quality(self, item):
        item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
