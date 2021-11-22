import numpy as np
import math
import rowan

class calc_ang_poly3d_class:
    def __init__(self, global_ref_orientation, orientations, equivalent_orientations):
        self.global_ref_orientation = global_ref_orientation
        self.orientations = orientations
        self.equivalent_orientations = equivalent_orientations

    def calc_ang_poly3d_func(self):
        alpha = []
        for i in range(len(self.orientations)):
            equivQ = []
            for t in range(len(self.equivalent_orientations)): # operation of each invariant quaternion on each particle
               equivQ.append(rowan.normalize(rowan.multiply(self.orientations[i], self.equivalent_orientations[t]))) 

            angles = []
            for q in range(len(equivQ)):
                quat_mul = rowan.multiply(rowan.conjugate(self.global_ref_orientation), equivQ[q])
                quat_mul = rowan.normalize(quat_mul)
                angles.append(2*math.acos(quat_mul[0]))

            theta = np.rad2deg(np.min(angles))
            alpha.append(theta)

        return alpha