import numpy as np

window_x, window_y = 256, 128
bodysize = 16

def jump():
    return np.array([0, -4])

def rightmove():
    return np.array([2, 0])

def leftmove():
    return np.array([-2, 0])

def fall():
    return np.array([0, 2])