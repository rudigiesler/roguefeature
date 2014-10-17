import random


class Stats:
    SCALE = 5
    DEF_SCALE = 0.8

    @property
    def strMod(self):
        return self._strMod

    @strMod.setter
    def strMod(self, value):
        self._strMod = value
        self.CheckHit()

    @property
    def agiMod(self):
        return self._agiMod

    @agiMod.setter
    def agiMod(self, value):
        self._agiMod = value

    @property
    def endMod(self):
        return self._endMod

    @endMod.setter
    def endMod(self, value):
        self._endMod = value
        self.CheckHit()

    @property
    def spdMod(self):
        return self._spdMod

    @spdMod.setter
    def spdMod(self, value):
        self._spdMod = value

    @property
    def atkMod(self):
        return self._atkMod

    @atkMod.setter
    def atkMod(self, value):
        self._atkMod = value

    @property
    def defMod(self):
        return self._defMod

    @defMod.setter
    def defMod(self, value):
        self._defMod = value

    @property
    def dodMod(self):
        return self._dodMod

    @dodMod.setter
    def dodMod(self, value):
        self._dodMod = value

    @property
    def hitMod(self):
        return self._hitMod

    @hitMod.setter
    def hitMod(self, value):
        self._hitMod = value
        self.CheckHit()

    @property
    def str(self):
        return self._str

    @str.setter
    def str(self, value):
        self._str = value
        self.CheckHit()

    @property
    def agi(self):
        return self._agi

    @agi.setter
    def agi(self, value):
        self._agi = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
        self.CheckHit

    @property
    def spd(self):
        return self._spd

    @spd.setter
    def spd(self, value):
        self._spd = value

    @property
    def atk(self):
        return int(
            (self._str + self._strMod) * 3 + (self._end + self._endMod) * 1.5)

    @property
    def defense(self):
        return int(
            self.DEF_SCALE * (self._agi + self._agiMod) * 3 +
            (self._end + self._endMod) * 1.5)

    @property
    def dod(self):
        return int(
            (self._spd + self._spdMod) * 1 + (self._agi + self._agiMod) * 0.4)

    @property
    def hitMax(self):
        return int(
            (self._end + self._endMod) * 6 + (self._str + self.strMod) * 3)

    def __init__(self, *args):
        if len(args) == 0:
            str, agi, end, spd = 0, 0, 0, 0
        elif len(args) == 1:
            seed, = args
            str = self.Generate(seed)
            agi = self.Generate(seed)
            end = self.Generate(seed)
            spd = self.Generate(seed)
        else:
            str, agi, end, spd = args
        self.InitZero()
        self._str = str
        self._agi = agi
        self._end = end
        self._spd = spd
        self.hit = self.hitMax

    def Generate(self, seed):
        mod = 0.85 + (0.3 * random.random())
        return int(round(seed * self.SCALE * mod))

    def InitZero(self):
        self._str = 0
        self._strMod = 0
        self._agi = 0
        self._agiMod = 0
        self._end = 0
        self._endMod = 0
        self._spd = 0
        self._spdMod = 0
        self._atkMod = 0
        self._dodMod = 0
        self._defMod = 0
        self._hitMod = 0

    def CheckHit(self):
        if (self.hit > (self.hitMax + self.hitMod)):
            self.hit = self.hitMax + self.hitMod
