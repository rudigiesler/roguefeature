import random

from RogueFeature.Backend.Game import Stats
from .unit import Unit


class Mobile(Unit):
    def __init__(self, x, y, imgPath, face, name, *args):
        super(Mobile, self).__init__(x, y, imgPath, face, name, False)
        self._stats = Stats(args)
        self.hit = self._stats.hitMax

    @property
    def hitMax(self):
        return self._stats.hitMax + self._stats.hitMod

    @property
    def atk(self):
        return self._stats.atkMax + self._stats.atkMod

    @property
    def defense(self):
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
            if m.atk <= self.defense:
                return None
            self.hit -= (m.atk - self.defense)
            if self.hit <= 0:
                self.Die()

    def Die(self):
        self._point.RemoveUnit(self)
