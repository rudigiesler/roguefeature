import unittest

from RogueFeature.Backend import Direction
from RogueFeature.Backend.Units import BaseObject, Mobile


class BaseObjectTest(unittest.TestCase):
    def test_interact(self):
        o = BaseObject(
            x=1, y=2, imgPath='foo.png', face=Direction.DOWN, name='foo',
            passable=False, interactable=True)
        self.assertEqual(o.Interact(None), None)
