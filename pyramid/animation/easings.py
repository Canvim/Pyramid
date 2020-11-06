
import math

import numpy as np

from ..utils.utils import sigmoid


# Many simple easing implementations by Google in Flutter:
# https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/animation/curves.dart

def linear(t=0, start=0, end=1):
    return start + (end - start) * t


def exponential(t, start, end, exponent=2):
    return linear(t**exponent, start, end)

# Implementation by the manim project at https://github.com/3b1b/manim/blob/99952067c1a399e15a197310d35a39bb2864b1af/manimlib/utils/rate_functions.py#L11
# Released under the MIT License. Copyright (c) 2018 3Blue1Brown LLC.
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
