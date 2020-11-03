
import math

import numpy as np
import operator as op

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

class Smooth(Easing):
    def interpolate(self, t, start, end):
        return linear(smooth(t), start, end)

def linear(t=0, start=0, end=1):
    return start + (end - start) * t

def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def smooth(t, inflection=10.0):
    error = sigmoid(-inflection / 2)
    return np.clip(
        (sigmoid(inflection * (t - 0.5)) - error) / (1 - 2 * error),
        0,
        1,
    )
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