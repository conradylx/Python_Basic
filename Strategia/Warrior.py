class Warrior:
    def __init__(self):
        self._exp = 0

    def __repr__(self):
        return f"{self.__class__.__name__}: hp={self._life}, exp={self._exp}"

    def march(self, distance):
        print(f"{self.__class__.__name__}: I've marched {distance}m.")
        self._exp += distance * 0.2
