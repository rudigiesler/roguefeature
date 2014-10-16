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
