from Polygon.triangle import Triangle
from math import sqrt, pow


class EquilateralTriangle(Triangle):
    """Equilateral Triangle a triangle whose all side are equal """

    def __init__(self, a):
        """Create a instance of equilateral triangle assuming all sides are equal a=b=c.

        :param a : triangle side (eg., a = 25)
        """
        if isinstance(a, (int, float)):
            super().__init__(a, a, a)
            self._a = float(a)

        else:
            print("a, must be a number")

    def height(self):
        """compute and return the altitude of triangle"""
        return (sqrt(3)/2) * self._a

    def area(self):
        """compute and return the area of a triangle."""
        return (sqrt(3)/4)*(pow(self._a,2))

    def perimeter(self):
        """Compute and return """
        return 3*self._a

