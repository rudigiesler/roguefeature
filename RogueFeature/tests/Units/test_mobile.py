import unittest

from RogueFeature.Backend import Direction, Point, Map
from RogueFeature.Backend.Units import Mobile


class MobileTest(unittest.TestCase):
    def setUp(self):
        self.mob = Mobile(1, 2, 'foo.png', Direction.DOWN, 'Foo', 1, 2, 3, 4)
        self.map = Map(10, 10, 'Level1')
        self.map.InitPoint(1, 2, 'bar.png', Direction.LEFT, True)
        self.map.AddUnitToPoint(1, 2, self.mob)

    def test_attributes(self):
        self.assertEqual(self.mob.hit, 21)
        self.mob.hit = 5
        self.assertEqual(self.mob.hit, 5)
        self.assertEqual(self.mob.hitMax, 21)
        self.assertEqual(self.mob.atk, 7)
        self.assertEqual(self.mob.defense, 9)
        self.assertEqual(self.mob.dod, 4)
        self.assertEqual(self.mob.str, 1)
        self.assertEqual(self.mob.agi, 2)
        self.assertEqual(self.mob.end, 3)
        self.assertEqual(self.mob.spd, 4)

    def test_die(self):
        self.assertTrue(self.map.Occupied(1, 2))
        self.mob.Die()
        self.assertFalse(self.map.Occupied(1, 2))

    def test_take_hit(self):
        mob2 = Mobile(1, 2, 'foo.png', Direction.DOWN, 'Foo', 5, 5, 5, 5)
        self.mob._stats._dod = 0
        self.assertEqual(self.mob.hit, 21)
        self.mob.TakeHit(mob2)
        self.assertEqual(self.mob.hit, 8)
