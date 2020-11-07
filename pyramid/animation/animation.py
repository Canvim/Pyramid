
from numpy.lib.arraysetops import isin
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

def recursively_interpolate_value(start_value, end_value, t, easing):
    if isinstance(start_value, (float, int)):
        return easing(t=t, start=start_value, end=end_value)
    else:
        raise NotImplementedError(f"Value of type '{start_value.__class__.__name__}' cannot be interpolated yet.")

class Animation:
    def __init__(self, target: Entity = None, duration=1000, start_time=0, easing=smoothSteep, **attributes_to_animate):
        self.target = target
        self.duration = duration
        self.easing = easing
        self.attributes_to_animate = attributes_to_animate
        self.original_property_values = {}

        self.start_time = 0

        self.progress = 0

    def interpolate(self, time):
        t = np.clip((time - self.start_time) / self.duration, -1, 1)

        if t <= 0:
            return

        # If the original_values are not present, get them!
        if not self.original_property_values:
            for key, end_value in self.attributes_to_animate.items():
                self.original_property_values[key] = getattr(self.target, key)

        self.interpolate_attributes_on_target(t)

    def interpolate_attributes_on_target(self, t):
        for key, end_value in self.attributes_to_animate.items():
            start_value = self.original_property_values[key]

            new_value = recursively_interpolate_value(start_value, end_value, t, self.easing)

            self.target.__setattr__(key, new_value)
