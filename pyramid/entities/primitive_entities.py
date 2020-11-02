
from .entity import Entity

class Rectangle(Entity):
    def __init__(self, width=200, height=100, **kwargs):
        super().__init__(**kwargs)

    def update(self):
        pass

    def draw(self):
        pass
