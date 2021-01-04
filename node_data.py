class node_data:

    def __init__(self, id: int, **kwargs) -> None:
        self.__id = id
        self.__tag = 0
        self.__weight = 0
        self.__info = ""

    def __str__(self) -> str:
        return str(self.__id)

    def __repr__(self) -> str:
        return str(self.__id)

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def getkey(self) -> int:
        return self.__id

    def gettag(self) -> int:
        return self.__tag

    def getweight(self) -> float:
        return self.__weight

    def getinfo(self) -> str:
        return self.__info

    def settag(self, tag: int) -> None:
        self.__tag = tag

    def setweight(self, w: float) -> None:
        self.__weight = w

    def setinfo(self, info: str) -> None:
        self.__info = info
