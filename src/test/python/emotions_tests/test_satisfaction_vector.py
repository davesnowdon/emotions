'''
Created on 8 Jun 2013

@author: dns
'''
import unittest

import emotions.satisfaction_vector as satisfaction_vector
from emotions.satisfaction_vector import feq

class TestSatisfactionVector(unittest.TestCase):

    def test_make_ev_from_sv_and_threshold(self):
        sv = { 1: 0.5, 2: 0.7 }
        threshold = { 1: 1.0, 2: 1.0 }
        ev = satisfaction_vector.expression_vector_difference(threshold, sv)
        expected = { 1: 0.5, 2: 0.3}
        self.assertTrue(satisfaction_vector.is_equal(expected, ev), 
                         "expression vector should equal {}".format(expected))

    def test_expression_vector_average(self):
        ev = { 1: 0.5, 2: 0.7 }
        average = satisfaction_vector.expression_vector_average(ev)
        self.assertEqual(average, 0.6, "average should be 0.6")

    def test_get_averages_for_all_control_points(self):
        sv = { 1: 0.5, 2: 0.7 }
        control_points = [(1, 1, { 1: 1.0, 2: 1.0 }),
                          (-1, 0, { 1: 0.5, 2: 0.5 })]
        expected = [(1, 1, 0.4), (-1, 0, -0.1)]
        result = satisfaction_vector.control_point_averages(control_points, sv)
        print "cp average result = {}".format(result)
        self.assertTrue(self.cp_equal(expected, result), 
                        "expected control point averages {}".format(expected))
        
#    def test_valence_arousal_from_satisfaction_vector(self):
#        motivation_id1 = 1
#        motivation_id2 = 2
#        sv = { motivation_id1 : 0.1,
#             motivation_id2 : 0.5 }
#        control_points = self.make_control_points_with_zeros()
#        (v, a) = satisfaction_vector.express(sv, control_points)
#        
    
    def cp_equal(self, cps1, cps2):        
        for (v1, v2) in zip(cps1, cps2):
            if not feq(v1[2], v2[2]):
                return False;
        return True
        
    def make_control_points_with_zeros(self):
        return [ (-1,  1, {}),
                 (0,   1, {}),
                 (1,   1, {}),
                 (-1,  0, {}),
                 (0,   0, {}),
                 (1,   0, {}),
                 (-1, -1, {}),
                 (0,  -1, {}),
                 (1,  -1, {})]

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()