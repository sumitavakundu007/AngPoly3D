import numpy as np
import json
from . import calc_ang_poly3d

def ang_poly3d_func():
    # Input files
    orien_json_file = str(input("Enter the orientations of the particles in a JSON file (2D list): "))
    equiv_orientations_json_file = str(input("Enter the equivalent orientations from a single particle's point group symmetry (2D list): "))
    global_ref_orientation_json_file = str(input("Enter the global reference orientation in JSON format: "))
    # read orientations json file
    with open(orien_json_file) as f:
        posi_data = json.load(f)

    orientations = np.array(posi_data["orientations"])
    # Read equivalent orientations json file
    with open(equiv_orientations_json_file) as g:
        orien_data = json.load(g)

    # Read global reference quaternion
    with open(global_ref_orientation_json_file) as h:
        ref_orien_data = json.load(h)

    global_ref_orientation = np.array(ref_orien_data["ref_orientation"])
    equivalent_orientations = np.array(orien_data["equiv_orientations"])
    calc_ang_poly3d_obj = calc_ang_poly3d.calc_ang_poly3d_class(global_ref_orientation, orientations, equivalent_orientations)
    angles = calc_ang_poly3d_obj.calc_ang_poly3d_func()

    return angles
