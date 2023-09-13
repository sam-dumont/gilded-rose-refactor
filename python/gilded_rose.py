# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for i, item in enumerate(self.items):
            if item.name == "Aged Brie":
                self.items[i] = AgedBrieRule(item).process()
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.items[i] = SulfurasRule(item).process()
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.items[i] = BackstagePassRule(item).process()
            elif item.name == "Conjured Mana Cake":
                self.items[i] = ConjuredRule(item).process()
            else:
                self.items[i] = RegularRule(item).process()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class RegularRule(object):
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality
        self.degrade_factor = 1
        self.MAX_QUALITY = 50
        self.MIN_QUALITY = 0

    def preprocess(self):
        if self.quality > self.MAX_QUALITY:
            raise ValueError(
                f"Item quality should never be higher than {self.MAX_QUALITY}"
            )
        if self.quality < self.MIN_QUALITY:
            raise ValueError(
                f"Item quality should never be lower than {self.MIN_QUALITY}"
            )

    def postprocess(self):
        self.sell_in = self.sell_in - 1
        return Item(self.name, self.sell_in, self.quality)

    def process(self):
        self.preprocess()
        if self.quality > self.MIN_QUALITY:
            if self.sell_in > 0:
                self.quality = max(self.quality - self.degrade_factor, self.MIN_QUALITY)
            else:
                self.quality = max(
                    self.quality - (2 * self.degrade_factor), self.MIN_QUALITY
                )
        return self.postprocess()


class AgedBrieRule(RegularRule):
    def process(self):
        self.preprocess()
        if self.quality < self.MAX_QUALITY:
            if self.sell_in > 0:
                self.quality = min(self.quality + 1, self.MAX_QUALITY)
            else:
                self.quality = min(self.quality + 2, self.MAX_QUALITY)
        return self.postprocess()


class SulfurasRule(RegularRule):
    def preprocess(self):
        pass

    def process(self):
        return Item(self.name, self.sell_in, self.quality)


class BackstagePassRule(RegularRule):
    def process(self):
        self.preprocess()
        if self.sell_in <= 0:
            self.quality = self.MIN_QUALITY
        elif self.quality <= self.MAX_QUALITY:
            if self.sell_in <= 5:
                self.quality = min(self.MAX_QUALITY, self.quality + 3)
            elif self.sell_in <= 10:
                self.quality = min(self.MAX_QUALITY, self.quality + 2)
            else:
                self.quality = min(self.MAX_QUALITY, self.quality + 1)
        return self.postprocess()


class ConjuredRule(RegularRule):
    def __init__(self, item):
        super().__init__(item)
        self.degrade_factor = 2
