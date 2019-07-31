from Polygon.triangle import Triangle
from math import sqrt, pow


class IsosceleTriangle(Triangle):
    """Isoscele triangle"""


    def __init__(self, a, c):
        """Create a new instance of Isoscele triangle, assuming a = b and c < a

           because a given triangle is said isoscele if at least two of its sides are equal

        :param a: triangle side (e.g., a = 24)
        :param c: triangle side (e.g., c = 90)
        """
        if a < c:
            print("base to long")
        else:
            super().__init__(a, a, c)   # call the super constructor method
            self._a = float(a)          # designate a as the equal sides
            self._b = float(c)          # and c as the base

    def area(self):
        """Compute and return the area"""
        try:
            altitude = sqrt(pow(self._a, 2) - pow(self._b, 2)/4)
            area = (1 * altitude * self._b) / 2
            return area

        except AttributeError as e:
            print("cannot compute the area check your arguments values")

    def perimeter(self):
        """return the perimeter of triangle knowing that p = 2a + b"""
        try:
            return (2*self._a) + self._b
        except AttributeError as e:
            print("cannot compute the perimeter check your argument values")
