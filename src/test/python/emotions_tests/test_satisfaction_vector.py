'''
Created on 8 Jun 2013

@author: davesnowdon
'''
import unittest

import emotions.satisfaction_vector as satisfaction_vector
from emotions.satisfaction_vector import feq, ControlPoint, ControlPointAverage


class TestSatisfactionVector(unittest.TestCase):

    def test_make_ev_from_sv_and_threshold(self):
        sv = {1: 0.5, 2: 0.7}
        threshold = {1: 1.0, 2: 1.0}
        ev = satisfaction_vector.expression_vector_difference(threshold, sv)
        expected = {1: 0.5, 2: 0.3}
        self.assertTrue(satisfaction_vector.is_equal(expected, ev),
                         "expression vector should equal {}".format(expected))

    def test_expression_vector_average(self):
        ev = {1: 0.5, 2: 0.7}
        average = satisfaction_vector.expression_vector_average(ev)
        self.assertEqual(average, 0.6, "average should be 0.6")

    def test_get_averages_for_all_control_points(self):
        sv = {1: 0.5, 2: 0.7}
        control_points = [ControlPoint(-1, 1, {1: 1.0, 2: 1.0}),
                          ControlPoint(0, 1, {1: 0.5, 2: 0.5}),
                          ControlPoint(1, 1, {1: 1, 2: 1}),
                          ControlPoint(-1, 0, {1: 1, 2: 1}),
                          ControlPoint(0, 0, {1: 0, 2: 0}),
                          ControlPoint(1, 0, {1: 0, 2: 0.5}),
                          ControlPoint(-1, -1, {1: 0.5, 2: 0}),
                          ControlPoint(0, -1, {1: 0.5, 2: 0.5}),
                          ControlPoint(1, -1, {1: 0.5, 2: 0.5})]
        expected = [ControlPointAverage(-1, 1, 0.4),
                    ControlPointAverage(0, 1, -0.1),
                    ControlPointAverage(1, 1, 0.4),
                    ControlPointAverage(-1, 0, 0.4),
                    ControlPointAverage(0, 0, 0),
                    ControlPointAverage(1, 0, -0.2),
                    ControlPointAverage(-1, 1, 0),
                    ControlPointAverage(0, 1, -0.1),
                    ControlPointAverage(1, 1, -0.1)]

        result = satisfaction_vector.control_point_averages(control_points, sv)
        print "cp average result = {}".format(result)
        self.assertEqual(len(control_points), len(result),
                         "Should get one result for each control point")
        self.assertTrue(self.cp_equal(expected, result),
                        "expected control point averages {}".format(expected))

    def test_count_non_zero(self):
        self.assertEqual(1, satisfaction_vector.count_non_zero_values({1: 1}),
                         "count dict of length 1 is 1")
        self.assertEqual(0, satisfaction_vector.count_non_zero_values({1: 0, 2: 0, 3: 0}),
                         "count dict of zero values is 0")
        self.assertEqual(2, satisfaction_vector.count_non_zero_values({1: 1, 2: 2}),
                         "count dict of 2 values is 2")

    def test_valence_arousal_from_satisfaction_vector(self):
        sv = {1: 0.5, 2: 0.7}
        control_points = [ControlPoint(-1, 1, {1: 1.0, 2: 1.0}),
                          ControlPoint(0, 1, {1: 0.5, 2: 0.5}),
                          ControlPoint(1, 1, {1: 1, 2: 1}),
                          ControlPoint(-1, 0, {1: 1, 2: 1}),
                          ControlPoint(0, 0, {1: 0, 2: 0}),
                          ControlPoint(1, 0, {1: 0, 2: 0.5}),
                          ControlPoint(-1, -1, {1: 0.5, 2: 0}),
                          ControlPoint(0, -1, {1: 0.5, 2: 0.5}),
                          ControlPoint(1, -1, {1: 0.5, 2: 0.5})]

        self.fail("not implemented")

    def cp_equal(self, cps1, cps2):
        if not len(cps1) == len(cps2):
            return False

        for (v1, v2) in zip(cps1, cps2):
            if not feq(v1[2], v2[2]):
                return False
        return True


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
