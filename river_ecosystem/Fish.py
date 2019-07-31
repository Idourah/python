from animal import Animal


class Fish(Animal):
    """Abstract representation of a real fish. in our ecosystem fish can die"""

    def __init__(self, color, identifier, strength=50, gender=False, life=25):
        """Create new instance of fish

        :param life : present the life of fish if zero it dies default(25)
        :param gender : fish gender default (False) when False : Female and True = male
        :param strength : fish strength default 50 determine whether it could survive in a collide with another fish
        """
        super().__init__(color, strength, gender)
        self._life = life
        self._id = identifier

    def die(self):
        """Kill the fish by setting its life to 0"""
        self._life = 0

    def get_id(self):
        return self._id

    def about(self):
        dictionary = {'animal ': 'Fish', 'color ': super().get_color(), 'id ': self.get_id()}
        return dictionary
