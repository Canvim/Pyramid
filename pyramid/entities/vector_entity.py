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

    def __init__(self, points=np.array([]), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points = points

    @abstractmethod
    def generate_points(self):
        raise NotImplementedError()

    @abstractmethod
    def update(self):
        raise NotImplementedError()

    def draw(self):

        # TODO: Implement General-purpose vector drawing of points using
        # move_to, line_to, curve_to and so on for all the points with
        # their correseponding points

        raise NotImplementedError()

        for point in self.points:
            pass
