class EdgeData:
    def __init__(self, src: int, dest: int, weight: float) -> None:
        self._src = src
        self._dest = dest
        self._weight = weight

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

    def getsrc(self) -> int:
        return self._src

    def getdest(self) -> int:
        return self._dest

    def getweught(self) -> float:
        return self._weight
