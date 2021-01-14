import math


class node_data:
    """
    This class  represents the set of operations applicable on a
    node (vertex) in a (directional) weighted graph.
    """

    def __init__(self, id: int, p: tuple = None, **kwargs) -> None:
        self.id = id
        self.tag = 0
        self.weight = math.inf
        self.info = "f"
        self.pos = p
        self.edge_out = 0
        self.edge_in = 0

    def __str__(self) -> str:
        return f"{self.id}:|edges out| {self.edge_out} |edges in| {self.edge_in}"

    def __repr__(self) -> str:
        return f"{self.id}:|edges out| {self.edge_out} |edges in| {self.edge_in}""

    def __eq__(self, o: object) -> bool:
        if not (isinstance(o, node_data)):
            return False
        return self.id == o.id

    def __lt__(self, other):
        return self.weight < other.weight

    def __hash__(self) -> int:
        return self.id

    def getkey(self) -> int:
        """
        Returns the key (id) associated with this node.
        :return:key
        """
        return self.id

    def gettag(self) -> int:
        """
        Temporal data (aka color: e,g, white, gray, black) which can be used be algorithms
        :return:tag
        """
        return self.tag

    def getweight(self) -> float:
        """
        Returns the weight associated with this node.
        :return:weight
        """
        return self.weight

    def getinfo(self) -> str:
        """
         Returns the remark (meta data) associated with this node.
        :return:info
        """
        return self.info

    def settag(self, tag: int) -> None:
        """
        Allows setting the "tag" value for temporal marking an node - common practice for marking by algorithms.
        :param tag:the new value of the tag
        :return:None
        """
        self.tag = tag

    def setweight(self, w: float) -> None:
        """
        Allows changing this node's weight.
        :param w:- the new weight
        :return:None
        """
        self.weight = w

    def setinfo(self, info: str) -> None:
        """
        Allows changing the remark (meta data) associated with this node.
        :param info:
        :return: None
        """
        self.info = info

    def getlocation(self) -> tuple:
        """
        Returns the location of this node
        :return: location
        """
        return self.pos

    def setlocation(self, pos) -> None:
        """
         Allows changing this node's location.
        :param pos: new new location  (position) of this node.
        :return: None
        """
        self.pos = pos
