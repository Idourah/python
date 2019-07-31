from Polygon.quadrilateral import Quadrilateral


class Square(Quadrilateral):
    """Square shape with four equal sides"""

    def __init__(self, side):
        """Create a new instance of square
        :param side : the square side
        """
        if isinstance(side, (int, float)):
            super().__init__(side, side, side, side)
            self._side = side
        else:
            raise TypeError("side must be a number")

    def area(self):
        """compute and return the square area A = side x side"""

        return self._side ** 2

    def perimeter(self):
        """Compute and return  the square perimeter p = 4 x side"""

        return self._side * 4

