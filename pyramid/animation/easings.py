
import math

from ..utils.utils import minmax

# The amazing anime.js library and it's many supported interpolations https://github.com/juliangarnier/anime/blob/master/src/index.js
# (svg paths included!)

# We must be able to interpolate
#   [X] Integers
#   [X] Floats
#   [ ] Strings
#   [ ] Points
#   [ ] Paths
#   [ ] Recursive arrays/tuples of said types
#   [ ] Recursive dictionaries of said types


class Easing:
    def interpolate(self, t=0, start=0, end=1):
        raise NotImplementedError()


def linear(t=0, start=0, end=1):
    value = start + (end - start) * t
    return minmax(value, start, end)

class Linear(Easing):
    def interpolate(self, t=0, start=0, end=1):
        return linear(t, start, end)


def exponential(t, start, end, exponent=2):
    exponential_t = t**exponent
    return linear(exponential_t, start, end)


class Exponential(Easing):
    exponent = 1
    def interpolate(self, t=0, start=0, end=1):
        return exponential(t, start, end, self.exponent)

class Quadratic(Exponential):
    exponent = 2

class Cubic(Exponential):
    exponent = 3

class Quartic(Exponential):
    exponent = 4

class Quintic(Exponential):
    exponent = 5

class Heptic(Exponential):
    exponent = 6