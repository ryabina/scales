
class ScalesModel(object):

    def __init__(self):
        self._weight = None
        self._address = None

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def address(self):
        return self._address

    @weight.setter
    def address(self, value):
        self._address = value
