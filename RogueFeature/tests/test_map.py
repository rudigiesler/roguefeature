import unittest

from RogueFeature.Backend import Map


class MapTest(unittest.TestCase):
    def test_properties(self):
        lvl = Map(10, 10, 'Level 1')
        print(Map.rows)
        self.assertEqual(lvl.rows, 10)
        self.assertEqual(lvl.columns, 10)
        self.assertEqual(lvl.Name, 'Level 1')
