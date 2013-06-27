'''
Created on 27 Jun 2013

@author: davesnowdon
'''


FLOAT_CMP_ACCURACY = 0.00000001


def feq(a, b):
    return abs(a - b) < FLOAT_CMP_ACCURACY
