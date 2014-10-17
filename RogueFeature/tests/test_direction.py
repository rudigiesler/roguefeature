import unittest

from RogueFeature.Backend import Direction


class DirectionTest(unittest.TestCase):
    def test_direction_values(self):
        self.assertEqual(Direction.UP, 0)
        self.assertEqual(Direction.DOWN, 1)
        self.assertEqual(Direction.LEFT, 2)
        self.assertEqual(Direction.RIGHT, 3)
