# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49
            ),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(19, gilded_rose.items[0].quality)


if __name__ == "__main__":
    unittest.main()
