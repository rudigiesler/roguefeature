from RogueFeature.Backend.Units import BaseObject, Mobile


class Point:
    def __init__(self, parent, imageID, face, passable):
        self._parent = parent
        self._objects = []
        self._imgID = imageID
        self._dir = face
        self._passable = passable
        self._visible = 0.0
        self._mob = None

    @property
    def passable(self):
        return self._passable

    @property
    def Occupied(self):
        return self._mob is not None

    @property
    def Units(self):
        return self.GenerateUnitList()

    @property
    def ImgID(self):
        return self._imgID

    @property
    def dir(self):
        return self._dir

    def AddUnit(self, u):
        if isinstance(u, BaseObject):
            self._objects.append(u)
        elif isinstance(u, Mobile):
            if self._mob is not None:
                raise Exception(
                    'Cannot add a mobile to an already occupied point.')
            self._mob = u

    def RemoveUnit(self, u):
        if isinstance(u, BaseObject):
            if u in self._objects:
                self._objects.remove(u)
        elif isinstance(u, Mobile):
            if self._mob is u:
                self._mob = None
            else:
                raise Exception(
                    'Cannot remove mobile, it is not occupying this point')

    def Migrate(self, u, x, y):
        self.RemoveUnit(u)
        self._parent.AddUnitToPoint(x, y, u)
        # Core.delta.DeltaEdit(u)

    def GenerateUnitList(self):
        units = list(self._objects)
        if self._mob is not None:
            units.append(self._mob)
        return units
