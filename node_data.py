from Point3D import Point3D
import math


class node_data:

    def __init__(self, id: int, p: tuple = None, **kwargs) -> None:
        self.__id = id
        self.__tag = 0
        self.__weight = math.inf
        self.__info = ""
        self.__pos = p
        self.neighbors = {}

    def __str__(self) -> str:
        return f"id:{self.__id},pos:{self.__pos}"

    def __repr__(self) -> str:
        return f"id:{self.__id},pos:{self.__pos}"

    def __eq__(self, o: object) -> bool:
        if not (isinstance(o, node_data)):
            return False
        return self.__id == o.__id

    def __lt__(self, other):
        return self.__weight < other.__weight

    def __hash__(self) -> int:
        return self.__id

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

    def getlocation(self) -> tuple:
        return self.__pos

    def setlocation(self, pos) -> None:
        self.__pos = pos

    def getneighbors(self) -> dict:
        return self.neighbors

    def isneighbor(self, node_id: int) -> bool:
        return self.neighbors.__contains__(node_id)

    def addneighbor(self, node_id: int, w: float) -> None:
        if node_id not in self.neighbors:
            self.neighbors[node_id] = w
