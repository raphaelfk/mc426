class LocationRepository:
    def __init__(self):
        self._store = []

    def add(self, local):
        self._store.append(local)

    def all(self):
        return list(self._store)
