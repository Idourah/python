from Polygon.triangle import Triangle
from math import sqrt


class RectangleTriangle(Triangle):
    """"""
    def __init__(self, a, b):
        """Create a new instance of triangle rectangle
        :param a : triangle side
        :param b : triangle side
        """
        super().__init__(a, b, c=0)
        self._a = float(a)
        self._b = float(b)

    def area(self):
        """Compute and return the area"""
        area = (self._a * self._b)/2
        return area

    def perimeter(self):
        """Compute a return the perimeter

        R :radius of the circumcircle
        r :radius of the incircle
        s : semi perimeter
        """
        R = (self._a + self._b)/2
        c = sqrt(pow(self._a, 2)+pow(self._b, 2))
        r = (self._a * self._b)/(self._a + self._b + c)
        s = self._a + self._b + c

        return s


