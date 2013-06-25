'''
Created on 8 Jun 2013

@author: davesnowdon
'''

import math
import collections

ControlPoint = collections.namedtuple('ControlPoint', ['valence', 'arousal', 'thresholds'])

ControlPointAverage = collections.namedtuple('ControlPointAverage', ['valence', 'arousal', 'average'])


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

def count_non_zero(thresholds):
    count = 0
    for mid in thresholds.keys():
        if not feq(thresholds[mid], 0):
            count = count + 1
    return count

def expression_vector_average(ev, num_significant_values=None):
    count = num_significant_values if num_significant_values else len(ev)
    if count:    
        return sum(ev.values()) / count
    else:
        return 0

def control_point_averages(control_points, sv):
    cp_averages = []
    for cp in control_points:
        difference = expression_vector_difference(cp.thresholds, sv)
        average = expression_vector_average(difference,
                                            count_non_zero(cp.thresholds))
        cp_averages.append(ControlPointAverage(valence=cp.valence,
                                               arousal=cp.arousal,
                                               average=average))
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