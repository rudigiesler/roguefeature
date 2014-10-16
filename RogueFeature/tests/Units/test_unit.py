import unittest

from RogueFeature.Backend import Direction, Point, Map
from RogueFeature.Backend.Units import Unit


class UnitTest(unittest.TestCase):
    def test_creation(self):
        u = Unit(
            x=1, y=0, imagePath='test.png', face=Direction.LEFT, name="foo",
            passable=False)
        self.assertEqual(isinstance(u, Unit), True)

    def test_set_point(self):
        lvl1 = Map(10, 10, 'Level 1')
        p = Point(
            parent=lvl1, imageID='test.png', face=Direction.UP, passable=True)
        u = Unit(
            x=1, y=0, imagePath='test.png', face=Direction.LEFT, name="foo",
            passable=False)
        u.SetPoint(p)
        self.assertEqual(u._point, p)