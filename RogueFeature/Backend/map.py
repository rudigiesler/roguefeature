from .point import Point


class Map:

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def Name(self):
        return self._name

    def __init__(self, rows, columns, name):
        self._rows = rows
        self._columns = columns
        self._name = name
        self._points = [[None for i in range(rows)] for j in range(columns)]

    def InitPoint(self, x, y, imagePath, face, passable):
        try:
            self._points[x][y] = Point(self, imagePath, face, passable)
        except IndexError:
            raise IndexError(
                'Attempted to initialise a point outside the bounds of map')

    def SetSpawn(self, x, y):
        self._spawnX = x
        self._spawnY = y

    def AddPlayerToSpawn(self):
        try:
            # TODO: Create PC in Core
            self._points[self._spawnX][self._spawnY].AddUnit(None)
            # Core.pc.SetPoint(self._points[_spawnX][_spawnY])
            # Core.pc.NewMap(self._spawnX, self._spawnY)
        except AttributeError:
            raise AttributeError('Spawn point for player not set')

    def AddUnitToPoint(self, x, y, u):
        try:
            self._points[x][y].AddUnit(u)
            u.SetPoint(self._points[x][y])
        except (AttributeError, IndexError) as e:
            if isinstance(e, AttributeError):
                raise AttributeError(
                    'Point %d;%d is not initialised' % (x, y))
            else:
                raise IndexError(
                    'Attempted to add unit to a point outside the bounds of ' +
                    'map')

    def BoundCheck(self, x, y):
        return not (x >= self._columns or x < 0 or y >= self._rows or y < 0)

    def Passable(self, x, y):
        if not self.BoundCheck(x, y):
            return False
        p = self._points[x][y]
        if p.passable:
            for u in p.GenerateUnitList():
                if not u.passable:
                    return False
        else:
            return False
        return True

    def GetUnits(self, x, y):
        try:
            return self._points[x][y].GenerateUnitList()
        except IndexError:
            raise IndexError(
                'Attempted to retrieve a unit list from a point outside ' +
                'bounds of map.')

    def Occupied(self, x, y):
        return self._points[x][y].Occupied

    def GetObjects(self, x, y):
        return self._points[x][y].GetObjects()

    def GetMobile(self, x, y):
        return self._points[x][y].GetMobile()
