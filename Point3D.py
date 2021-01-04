class Point3D:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.__x = x
        self.__y = y
        self.__z = z

    def x(self) -> float:
        return self.__x

    def y(self) -> float:
        return self.__y

    def z(self) -> float:
        return self.__z

    def distance(self, p2) -> float:
        dx = self.x() - p2.x
        dy = self.y() - p2.y
        dz = self.z() - p2.z
        t = (dx * dx + dy * dy + dz * dz)
        return t ** 0.5
