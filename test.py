import numpy as np
import scipy.interpolate as interp

points1 = np.array([i for i in range(10+1)])
points2 = np.array([i for i in range(5+1)])

print(points2)

p2_i = interp.interp1d(np.arange(points2.size), points2)
scaled_p2 = p2_i(np.linspace(0, points2.size-1, points1.size))

def interpolate(a, b, t):
    return (1-t)*a + t*b

print(interpolate(points1, scaled_p2, 1.0))