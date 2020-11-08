
import numpy as np
import scipy.interpolate

from .easings import *
from ..entities.entity import Entity

# The amazing anime.js library and it's many supported interpolations https://github.com/juliangarnier/anime/blob/master/src/index.js
# (svg paths included!)

# TODO:
# We must be able to interpolate
#   [X] Integers
#   [X] Floats
#   [X] Booleans (true/false switch when easing(t) >= 0.5)
#   [ ] Strings
#
#   Moreover:
#   [ ] Recursively check lists/tuples of above types
#   [ ] Recursively check dictionaries of above types

def recursively_interpolate_value(start_value, end_value, t, easing):
    if isinstance(start_value, (float, int)):
        return easing(t=t, start=start_value, end=end_value)

    elif isinstance(start_value, (bool)):
        return start_value if easing(t=t, start=0, end=1) < 0.5 else end_value

    elif isinstance(start_value, (complex)):
        real = easing(t=t, start=start_value.real, end=end_value.real)
        imaginary = easing(t=t, start=start_value.imag, end=end_value.imag)
        return complex(real, imaginary)

    # Experiment with scipy interpolating in-between points... Not quite right yet
    # elif isinstance(start_value, (list, tuple, np.ndarray, np.array)):
    #     new_t = easing(t, 0, 1)
    #     start_array = np.array(start_value)
    #     end_array = np.array(end_value)

    #     s_i = scipy.interpolate.interp1d(np.arange(start_array.size), start_array)
    #     scaled_start_array = s_i(np.linspace(0, start_array.size-1, end_array.size))

    #     return (1 - new_t) * scaled_start_array + new_t * end_array

    # Much faster than implementation below. However, it can only handle lists
    # of same datatype.. (maybe even only numbers..?), which is an inherit
    # limitation/advantage of numpy.
    elif isinstance(start_value, (list, tuple, np.ndarray, np.array)):
        new_t = easing(t, 0, 1)
        start_array = np.array(start_value)
        end_array = np.array(end_value)

        if start_array.size < end_array.size:
            start_array = np.resize(start_array, end_array.size)
        else:
            end_array = np.resize(end_array, start_array.size)

        return (1 - new_t) * start_array + new_t * end_array

    # Old, much slower implementation.. Could handle arrays of whatever though!
    # elif isinstance(start_value, (list, tuple, np.ndarray, np.array)):
    #     start_length = len(start_value)
    #     end_length = len(end_value)
    #     new_list = []
    #     if start_length < end_length:
    #         new_list = [recursively_interpolate_value(start_value[i % start_length], end_value[i], t, easing) for i in range(end_length)]
    #     elif start_length > end_length:
    #         new_list = [recursively_interpolate_value(start_value[i], end_value[i % end_length], t, easing) for i in range(start_length)]
    #     else:
    #         new_list = [recursively_interpolate_value(start_value[i], end_value[i], t, easing) for i in range(end_length)]
    #     return new_list

    else:
        raise NotImplementedError(f"Value of type '{start_value.__class__.__name__}' cannot be interpolated yet.")

class Animation:
    def __init__(self, target: Entity = None, duration=1500, start_time=0, easing=smoothSteep, **attributes_to_animate):
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
