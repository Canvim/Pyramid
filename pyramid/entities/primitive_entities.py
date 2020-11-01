
from .entity import Entity

class Rectangle(Entity):
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
