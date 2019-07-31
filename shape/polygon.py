from abc import ABCMeta, abstractmethod


class Polygon(metaclass=ABCMeta):
    """Polygon Interface"""

    @abstractmethod
    def area(self):
        """Compute the area of specific type of a shape

        Abstract method which should be implemented by shape subclasses.
        """

    @abstractmethod
    def perimeter(self):
        """Compute the perimeter of a specific shape

        Abstract method which should be implemented by shape subclasses.
        """

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self == other

        else:
            raise TypeError("argument must to be Polygon")
