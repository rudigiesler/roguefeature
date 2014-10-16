from .unit import Unit


class BaseObject(Unit):
    def __init__(self, x, y, imgPath, face, name, passable, interactable):
        super(BaseObject, self).__init__(x, y, imgPath, face, name, passable)
        self.interactable = interactable

    def Interact(self, m):
        if not self.interactable:
            return None
