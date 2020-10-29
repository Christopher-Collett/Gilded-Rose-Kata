# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        [item.update_quality() for item in self.items]


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if self.quality > 0:
            self.decrement_quality()
        self.decrement_sell_in()
        if self.sell_in < 0 and self.quality > 0:
            self.decrement_quality()

    def decrement_sell_in(self):
        self.sell_in -= 1

    def increment_quality(self):
        self.quality += 1

    def decrement_quality(self):
        self.quality -= 1

    def reset_quality(self):
        self.quality = 0


class Item_Aged_Brie(Item):
    def update_quality(self):
        if self.quality < 50:
            self.increment_quality()
        self.decrement_sell_in()
        if self.sell_in < 0 and self.quality < 50:
            self.increment_quality()


class Item_Backstage_Passes(Item):
    def update_quality(self):
        if self.quality < 50:
            self.increment_quality()
            if self.sell_in < 11 and self.quality < 50:
                self.increment_quality()
            if self.sell_in < 6 and self.quality < 50:
                self.increment_quality()
        self.decrement_sell_in()
        if self.sell_in < 0:
            self.reset_quality()


class Item_Sulfuras(Item):
    def update_quality(self):
        pass


def make_item(name, sell_in, quality):
    if name == "Aged Brie":
        return Item_Aged_Brie(name, sell_in, quality)
    elif name == "Backstage passes to a TAFKAL80ETC concert":
        return Item_Backstage_Passes(name, sell_in, quality)
    elif name == "Sulfuras, Hand of Ragnaros":
        return Item_Sulfuras(name, sell_in, quality)
    else:
        return Item(name, sell_in, quality)
