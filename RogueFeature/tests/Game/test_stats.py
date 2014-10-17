import unittest

from RogueFeature.Backend.Game import Stats


class StatsTest(unittest.TestCase):
    def test_create_zero(self):
        s = Stats()
        self.assertEqual(s.str, 0)
        self.assertEqual(s.agi, 0)
        self.assertEqual(s.end, 0)
        self.assertEqual(s.spd, 0)
        self.assertEqual(s.hit, 0)

    def test_create_random(self):
        for i in range(10):
            s = Stats(1)
            self.assertLessEqual(s.str, 6)
            self.assertLessEqual(s.agi, 6)
            self.assertLessEqual(s.end, 6)
            self.assertLessEqual(s.spd, 6)

    def test_create_contants(self):
        s = Stats(1, 2, 3, 4)
        self.assertEqual(s.str, 1)
        self.assertEqual(s.agi, 2)
        self.assertEqual(s.end, 3)
        self.assertEqual(s.spd, 4)

    def test_getters_setters(self):
        s = Stats(1, 2, 3, 4)
        self.assertEqual(s.str, 1)
        self.assertEqual(s.agi, 2)
        self.assertEqual(s.end, 3)
        self.assertEqual(s.spd, 4)

        s.strMod = 5
        self.assertEqual(s.strMod, 5)
        s.agiMod = 6
        self.assertEqual(s.agiMod, 6)
        s.endMod = 7
        self.assertEqual(s.endMod, 7)
        s.spdMod = 8
        self.assertEqual(s.spdMod, 8)
        s.atkMod = 9
        self.assertEqual(s.atkMod, 9)
        s.defMod = 10
        self.assertEqual(s.defMod, 10)
        s.dodMod = 11
        self.assertEqual(s.dodMod, 11)
        s.hitMod = 12

        self.assertEqual(s.hitMod, 12)
        self.assertEqual(s.atk, 33)
        self.assertEqual(s.defense, 34)
        self.assertEqual(s.dod, 15)
        self.assertEqual(s.hitMax, 78)

    def test_generate(self):
        s = Stats()
        for i in range(10):
            result = s.Generate(2)
            self.assertLessEqual(result, 12)
            self.assertGreaterEqual(result, 9)

    def test_check_hit(self):
        s = Stats(1, 1, 1, 1)
        self.assertEqual(s.hit, 9)
        s.strMod = -1
        self.assertEqual(s.hit, 6)
