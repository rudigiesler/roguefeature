import unittest

from RogueFeature.Backend import Point, Map, Direction
from RogueFeature.Backend.Units import BaseObject


class PointTest(unittest.TestCase):
    def setUp(self):
        self.lvl1 = Map(10, 10, 'Level 1')
        self.p = Point(
            parent=self.lvl1, imageID='test.png', face=Direction.UP,
            passable=True)
        self.bo = BaseObject(
            x=1, y=2, imgPath='foo.png', face=Direction.UP, name='foo',
            passable=False, interactable=True)

    def test_properties(self):
        self.assertTrue(self.p.passable)
        self.assertFalse(self.p.Occupied)
        self.assertEqual(self.p.Units, [])
        self.assertEqual(self.p.ImgID, 'test.png')
        self.assertEqual(self.p.dir, Direction.UP)

    def test_add_unit(self):
        self.assertEqual(self.p.Units, [])

        self.p.AddUnit(self.bo)
        self.assertEqual(self.p.Units, [self.bo])

    def test_remove_unit(self):
        self.p.AddUnit(self.bo)
        self.assertEqual(self.p.Units, [self.bo])

        self.p.RemoveUnit(self.bo)
        self.assertEqual(self.p.Units, [])

    def test_migrate(self):
        # TODO: Implement Map.AddUnitToPoint for Point.Migrate
        pass

    def test_generate_unit_list(self):
        self.p.AddUnit(self.bo)
        self.assertEqual(self.p.GenerateUnitList(), [self.bo])

    def test_get_objects(self):
        self.p.AddUnit(self.bo)
        self.assertEqual(self.p.GetObjects(), [self.bo])
