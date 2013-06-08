'''
Created on 8 Jun 2013

@author: dsnowdon
'''

import math

FLOAT_CMP_ACCURACY=0.00000001

def expression_vector_difference(ev, sv):
    difference = {}
    for mid in ev.keys():
        if not feq(ev[mid], 0):
            score = sv.get(mid, 0)
            difference[mid] = ev[mid] - score
        else:
            difference[mid] = 0
    return difference

def expression_vector_average(ev):
    return sum(ev.values()) / len(ev)

def control_point_averages(control_points, sv):
    cp_averages = []
    for cp in control_points:
        difference = expression_vector_difference(cp[2], sv)
        average = expression_vector_average(difference)
        cp_averages.append((cp[0], cp[1], average))
    return cp_averages

def express():
    pass

def is_equal(sv1, sv2):
    for mid in list(set(sv1.keys()) | set(sv2.keys())):
        if not feq(sv1[mid], sv2[mid]):
            return False
    return True

def feq(a,b):
    return abs(a-b) < FLOAT_CMP_ACCURACY