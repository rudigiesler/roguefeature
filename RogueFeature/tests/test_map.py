import unittest

from RogueFeature.Backend import Map, Point, Direction
from RogueFeature.Backend.Units import BaseObject


class MapTest(unittest.TestCase):
    def setUp(self):
        self.lvl = Map(10, 10, 'Level1')
        self.bo = BaseObject(
            x=1, y=2, imgPath='foo.png', face=Direction.UP, name='foo',
            passable=False, interactable=True)

    def test_properties(self):
        self.assertEqual(self.lvl.rows, 10)
        self.assertEqual(self.lvl.columns, 10)
        self.assertEqual(self.lvl.Name, 'Level1')

    def test_init_point(self):
        self.lvl.InitPoint(
            x=1, y=2, imagePath='foo.png', face=Direction.LEFT, passable=True)
        self.assertIsInstance(self.lvl._points[1][2], Point)

    def test_init_point_out_of_bounds(self):
        with self.assertRaises(IndexError) as err:
            self.lvl.InitPoint(
                x=10, y=10, imagePath='foo.png', face=Direction.LEFT,
                passable=True)
        self.assertEqual(
            err.exception.args[0], 
            'Attempted to initialise a point outside the bounds of map')

    def test_set_spawn(self):
        self.lvl.SetSpawn(2, 3)
        self.assertEqual(self.lvl._spawnX, 2)
        self.assertEqual(self.lvl._spawnY, 3)

    def test_add_player_to_spawn(self):
        # TODO: Create PC in Core to finish this test_properties
        pass

    def test_add_unit_to_point(self):
        self.lvl.InitPoint(1, 2, 'foo.png', Direction.RIGHT, True)
        self.lvl.AddUnitToPoint(1, 2, self.bo)
        self.assertEqual(self.lvl._points[1][2].GetObjects(), [self.bo])

    def test_add_unit_to_point_out_of_bounds(self):
        with self.assertRaises(IndexError) as err:
            self.lvl.AddUnitToPoint(10, 10, self.bo)
        self.assertEqual(
            err.exception.args[0],
            'Attempted to add unit to a point outside the bounds of map')

    def test_add_unit_no_point_initialization(self):
        with self.assertRaises(AttributeError) as err:
            self.lvl.AddUnitToPoint(1, 2, self.bo)
        self.assertEqual(
            err.exception.args[0],
            'Point 1;2 is not initialised')

    def test_bound_check(self):
        self.assertTrue(self.lvl.BoundCheck(1, 2))
        self.assertFalse(self.lvl.BoundCheck(-1, 2))
        self.assertFalse(self.lvl.BoundCheck(1, -2))
        self.assertFalse(self.lvl.BoundCheck(10, 2))
        self.assertFalse(self.lvl.BoundCheck(1, 10))

    def test_passable(self):
        self.lvl.InitPoint(1, 2, 'foo.png', Direction.RIGHT, False)
        self.assertFalse(self.lvl.Passable(1, 2))

        self.lvl.InitPoint(1, 2, 'foo.png', Direction.RIGHT, True)
        self.assertTrue(self.lvl.Passable(1, 2))

        self.lvl.AddUnitToPoint(1, 2, self.bo)
        self.assertFalse(self.lvl.Passable(1, 2))

    def test_get_users(self):
        self.lvl.InitPoint(1, 2, 'foo.png', Direction.RIGHT, False)
        self.lvl.AddUnitToPoint(1, 2, self.bo)
        self.assertEqual(self.lvl.GetUnits(1, 2), [self.bo])

    def test_users_outside_bounds(self):
        with self.assertRaises(IndexError) as err:
            self.lvl.GetUnits(10, 10)
        self.assertEqual(
            err.exception.args[0],
            'Attempted to retrieve a unit list from a point outside bounds ' +
            'of map.')

    def test_occupied(self):
        # TODO: Create Mobile to finish this test
        pass

    def test_get_objects(self):
        self.lvl.InitPoint(1, 2, 'foo.png', Direction.RIGHT, False)
        self.lvl.AddUnitToPoint(1, 2, self.bo)
        self.assertEqual(self.lvl.GetObjects(1, 2), [self.bo])

    def test_get_mobile(self):
        # TODO: Create Mobile to finish this test
        pass