
from ..utils.utils import minmax
from .easings import Easing, Linear
from ..entities.entity import Entity

class Animation:
    def __init__(self, target : Entity = None, duration=1000, easing : Easing = Linear, **properties_to_animate):
        self.target = target
        self.duration = duration
        self.easing = easing
        self.properties_to_animate = properties_to_animate
        self.original_property_values = {}

        for key, end_value in self.properties_to_animate.items():
            if self.target.__getattribute__(key):
                self.original_property_values[key] = self.target.__getattribute__(key)
            else:
                raise NotImplementedError(f"'{key}' does not exist as an attribute of entity '{target.__name__}'")

        self.progress = 0

    def interpolate(self, t):
        t = minmax(t, 0, 1)

        for key, end_value in self.properties_to_animate.items():
            start_value = self.original_property_values[key]
            self.target.__setattr__(key, self.easing.interpolate(t, start_value, end_value))
