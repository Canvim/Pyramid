"""Base for vector-based entities"""

from abc import abstractmethod

import numpy as np

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

    @abstractmethod
    def generate_paths(self):
        raise NotImplementedError()

    @abstractmethod
    def update(self):
        raise NotImplementedError()
