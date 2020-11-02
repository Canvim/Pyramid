"""An abstract base class for all Entities to implement and extend"""

from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Base Entity Class implemented by all other entities
    including Scene, Rectangle, Arc, Circle and many more.

    Anything that will be rendered should implement this
    class or its derivatives.
    """

    def __init__(self, x=0, y=0, z=0, rotation=0, scale=1):
        self.x = x
        self.y = y

        # z-index is used for render-order in 2D.
        self.z = z

        self.rotation = rotation
        self.scale = scale
        self.children = []

    @abstractmethod
    def update(self):
        return NotImplemented

    @abstractmethod
    def draw(self):
        return NotImplemented
