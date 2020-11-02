# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        [item.update_item() for item in self.items]


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Item_With_Additional_Methods(Item):

    def __init__(self, name, sell_in, quality, quality_delta=-1):
        super().__init__(name, sell_in, quality)

        self.min_quality_value = (0,)
        self.max_quality_value = (50,)
        self.original_quality_delta = self.quality_delta = quality_delta

        self.sell_in_delta = -1

    def min_quality(self):
        return self.min_quality_value[0]

    def max_quality(self):
        return self.max_quality_value[0]

    def update_item(self):
        self.update_sell_in()
        self.update_quality()

    def update_quality(self):
        self.quality += self.quality_delta
        self.check_quality()

    def check_quality(self):
        self.quality = self.get_in_range(self.quality,
                                         self.min_quality(),
                                         self.max_quality())

    def update_sell_in(self):
        self.sell_in += self.sell_in_delta
        self.check_sell_in()

    def check_sell_in(self):
        if self.sell_in < 0:
            self.quality_delta = self.original_quality_delta * 2

    def get_in_range(self, value, min_value, max_value):
        if value < min_value:
            return min_value
        elif value > max_value:
            return max_value
        return value


class Item_Backstage_Passes(Item_With_Additional_Methods):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

        self.original_quality_delta = self.quality_delta = 1
        self.quality_after_sell_in_past = 0

    def check_sell_in(self):
        if self.sell_in <= 10:
            self.quality_delta = self.original_quality_delta * 2
        if self.sell_in <= 5:
            self.quality_delta = self.original_quality_delta * 3
        if self.sell_in < 0:
            self.quality_delta = 0
            self.quality = self.quality_after_sell_in_past


class Item_Sulfuras(Item_With_Additional_Methods):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

        self.min_quality_value = (80,)
        self.max_quality_value = (80,)
        self.quality_delta = 0

        self.sell_in = 0
        self.sell_in_delta = 0


def make_item(name, sell_in, quality):
    if name == "Aged Brie":
        return Item_With_Additional_Methods(name, sell_in,
                                            quality, quality_delta=1)
    elif name == "Backstage passes to a TAFKAL80ETC concert":
        return Item_Backstage_Passes(name, sell_in, quality)
    elif name == "Sulfuras, Hand of Ragnaros":
        return Item_Sulfuras(name, sell_in, quality)
    elif name == "Conjured":
        return Item_With_Additional_Methods(name, sell_in,
                                            quality, quality_delta=-2)
    else:
        return Item_With_Additional_Methods(name, sell_in, quality)
