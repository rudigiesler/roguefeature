import random

from RogueFeature.Backend.Game import Stats
from .unit import Unit


class Mobile(Unit):
    @property
    def hit(self):
        return self._stats.hit

    @hit.setter
    def hit(self, value):
        self._stats.hit = value

    @property
    def hitMax(self):
        return self._stats.hitMax + self._stats.hitMod

    @property
    def atk(self):
        return self._stats.atk + self._stats.atkMod

    @property
    def defense(self):
        return self._stats.defense + self._stats.defMod

    @property
    def dod(self):
        return self._stats.dod + self._stats.dodMod

    @property
    def str(self):
        return self._stats.str + self._stats.strMod

    @property
    def agi(self):
        return self._stats.agi + self._stats.agiMod

    @property
    def end(self):
        return self._stats.end + self._stats.endMod

    @property
    def spd(self):
        return self._stats.spd + self._stats.spdMod

    def Die(self):
        self._point.RemoveUnit(self)

    def __init__(self, x, y, imgPath, face, name, *args):
        super(Mobile, self).__init__(x, y, imgPath, face, name, False)
        self._stats = Stats(*args)
        self.hit = self._stats.hitMax

    def TakeHit(self, m):
        if not self.dod * 0.01 > random.random() and m.atk > self.defense:
            self.hit -= (m.atk - self.defense)
            if self.hit <= 0:
                self.Die()
