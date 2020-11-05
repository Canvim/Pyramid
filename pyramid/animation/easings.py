
import math

import numpy as np

from ..utils.utils import sigmoid


def linear(t=0, start=0, end=1):
    return start + (end - start) * t

def exponential(t, start, end, exponent=2):
    return linear(t**exponent, start, end)

# Implementation by the manim project
def manim_smooth(t, inflection=10.0):
    error = sigmoid(-inflection / 2)
    return np.clip(
        (sigmoid(inflection * (t - 0.5)) - error) / (1 - 2 * error),
        0,
        1,
    )

# Visualizations at https://www.desmos.com/calculator/olniyqli1y

def smooth(t, start=0, end=1):
    return linear(manim_smooth(t), start, end)

def smoothSteep(t, start=0, end=1):
    return linear(manim_smooth(t, 15), start, end)

def smoothSteeper(t, start=0, end=1):
    return linear(manim_smooth(t, 25), start, end)

def fastSmoothInSlowSmoothOut(t, start=0, end=1):
    return linear(manim_smooth(t**0.3, 15)**4, start, end)

def slowSmoothInFastSmoothOut(t, start=0, end=1):
    return linear(manim_smooth(t**5, 15)**0.3, start, end)