import unittest

from RogueFeature.Backend import Point, Map, Direction


class PointTest(unittest.TestCase):
    def test_properties(self):
        lvl1 = Map(10, 10, 'Level 1')
        p = Point(
            parent=lvl1, imageID='test.png', face=Direction.UP, passable=True)
        self.assertEqual(p.passable, True)
        self.assertEqual(p.Occupied, False)
        self.assertEqual(p.Units, [])
        self.assertEqual(p.ImgID, 'test.png')
        self.assertEqual(p.dir, Direction.UP)
