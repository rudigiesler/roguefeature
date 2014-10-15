import random

from RogueFeature.Backend.Units import Unit

class Mobile(Unit):
    def __init__(self, x, y, imgPath, face, name, *args):
        super(BaseObject, self).__init__(x, y, imgPath, face, name, False)
        self._states = Stats(args)
        self.hit = _stats.hitMax

    @property
    def hitMax(self):
        return self._stats.hitMax + self._stats.hitMod

    @property
    def atk(self):
        return self._stats.atkMax + self._stats.atkMod

    @property
    def def(self):
        return self._stats.defMax + self._stats.defMod

    @property
    def dod(self):
        return self._stats.dodMax + self._stats.dodMod

    @property
    def str(self):
        return self._stats.strMax + self._stats.strMod

    @property
    def agi(self):
        return self._stats.agiMax + self._stats.agiMod

    @property
    def end(self):
        return self._stats.endMax + self._stats.endMod

    @property
    def spd(self):
        return self._stats.spdMax + self._stats.spdMod

    def TakeHit(self, m):
        if not self.dod * 0.01 > random.random():
            if m.atk <= self.def:
                return None
            self.hit = hit - (m.atk - def)
            if hit <= 0:
                self.Die()

    def Die(self):
        self._point.RemoveUnit(self)