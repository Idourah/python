import math
from abc import abstractmethod

"""
   Author: Yoane Karstusba
   
   Description:
   
   date : 26.08.2019
   
   code version: 1.0
"""


class Animal:
    """Abstract representation of a real animal"""

    ANIMAL_ID = 0  # data-level member

    def __init__(self, color, strength, gender=1):
        """Create a new instance of animal class.

        :param color : the skin color of the animal (e.g., "red")
        :param gender
        :param strength
        """

        self._color = color
        self._gender = gender
        self._strength = strength

    def get_color(self):
        """Return animal color"""
        return self._color

    def get_gender(self):
        return self._gender

    def get_strength(self):
        return self._strength

    """ setters """

    def set_color(self, color):
        """Assign a given color to animal, assuming color to be string"""

        if isinstance(color, str):              # check if color is a string
            self._color = color                 # assign it to instance variable sef._color

        else:                                   # otherwise
            print("set_color given argument must be a string") # recall that color should be a string type value

    @abstractmethod
    def about(self):
        """describe the object"""
