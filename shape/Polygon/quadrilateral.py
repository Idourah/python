from polygon import Polygon


class Quadrilateral(Polygon):
    """Quadrilateral a shape with four edges"""

    def __init__(self, a, b, c, d):
        """Create a new instance  variable of quadrilateral
        :param a: first edge (eg. a = 14)
        :param b: second edge (e.g b = 30)
        :param c : third edge (e.g, c = 36)
        :param d : fourth edge (e.g, d = 90)
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and (c, (int, float)) and isinstance(d, (float,int)):
            self._a = a
            self._b = b
            self._c = c
            self._d = d
        else:
            raise ValueError("please enter number")

    def area(self):
        """Compute de area"""

    def perimeter(self):
        """Compute the perimeter"""

