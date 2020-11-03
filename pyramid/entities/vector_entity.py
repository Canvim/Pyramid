"""Base for vector-based entities"""

from abc import abstractmethod

import numpy as np
import svgpathtools

from .entity import Entity


class VectorEntity(Entity):
    """
    Base Entity Class implemented by all other entities
    including Scene, Rectangle, Arc, Circle and many more.

    Anything that will be rendered should implement this
    class or its derivatives.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.paths = []

    def update(self):
        pass
        # self.generate_paths()

        # for i in range(0, len(self.paths)):
            # self.paths[i] = self.paths[i].translated(0.1+0j).scaled(1 - 0.01)

    @abstractmethod
    def generate_paths(self):
        raise NotImplementedError()
