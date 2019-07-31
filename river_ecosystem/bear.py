from animal import Animal
from Fish import Fish


class Bear(Animal):
    """Abstract representation of a real bear"""

    def __init__(self, color, identifier, strength=100, gender=True):
        """Create a new instance of bear"""
        super().__init__(color, strength, gender)
        self._id = identifier

    @staticmethod
    def kill(fish):
        """the bear can kill the fish"""
        if isinstance(fish, Fish):
            fish.die()
            return True
        else:
            print("cannot kill this animal")

    def get_id(self):
        return self._id

    def about(self):
        dictionary = {'animal ':'Bear', 'color ': super().get_color(), 'id': self.get_id()}
        return dictionary
