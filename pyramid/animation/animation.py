
from .easings import *
from ..entities.entity import Entity

# The amazing anime.js library and it's many supported interpolations https://github.com/juliangarnier/anime/blob/master/src/index.js
# (svg paths included!)

# TODO:
# We must be able to interpolate
#   [X] Integers
#   [X] Floats
#   [ ] Strings
#   [ ] Paths
#
#   Moreover:
#   [ ] Recursively check arrays/tuples of above types
#   [ ] Recursively check dictionaries of above types


class Animation:
    def __init__(self, target: Entity = None, duration=1000, start_time=0, easing=smoothSteep, **properties_to_animate):
        self.target = target
        self.duration = duration
        self.easing = easing
        self.properties_to_animate = properties_to_animate
        self.original_property_values = {}

        self.start_time = 0

        self.progress = 0

    def interpolate(self, time):
        t = np.clip((time - self.start_time) / self.duration, -1, 1)

        if t <= 0:
            return

        # If the original_values are not present, get them!
        if not self.original_property_values:
            for key, end_value in self.properties_to_animate.items():
                if self.target.__getattribute__(key):
                    self.original_property_values[key] = self.target.__getattribute__(key)
                else:
                    raise AttributeError(f"'{key}' does not exist as an attribute of entity '{self.target.__name__}'")

        for key, end_value in self.properties_to_animate.items():
            start_value = self.original_property_values[key]
            self.target.__setattr__(key, self.easing(t=t, start=start_value, end=end_value))
