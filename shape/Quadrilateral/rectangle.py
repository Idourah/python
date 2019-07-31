from Polygon.quadrilateral import Quadrilateral


class Rectangle(Quadrilateral):
    """Rectangle shape with a width and height"""

    def __init__(self, width, height):
        """Create a new instance of Rectangle class"""
        if isinstance(width, (int, float)) and isinstance(height, (int, float)):
            super().__init__(width, height, 0, 0)
            self._width = width
            self._height = height
        else:
            raise TypeError("width and height must be number")

    def area(self):
        """Compute and return rectangle area"""
        return self._width * self._height

    def perimeter(self):
        """Compute and return rectangle perimeter"""
        return (self._height + self._width) * 2
