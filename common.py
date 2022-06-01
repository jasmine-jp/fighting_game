import numpy as np

class Common:
    window_x, window_y = 160, 120

    def jump(self):
        return np.array([0, 1])
    
    def rightmove(self, keepflag):
        return np.array([1, 0]) if keepflag else np.array([0, 0])
    
    def leftmove(self, keepflag):
        return np.array([-1, 0]) if keepflag else np.array([0, 0])