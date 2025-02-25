class InsertOrderDict(dict):
    def __init__(self):
        super().__init__()
        self._index_map = {}
        self._counter = 0

    def __setitem__(self, key, value):
        if key not in self:
            self._index_map[key] = self._counter
            self._counter += 1
        super().__setitem__(key, value)

    def get_insert_order(self, key):
        return self._index_map.get(key, None)