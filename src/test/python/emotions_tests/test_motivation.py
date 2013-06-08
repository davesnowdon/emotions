'''
Created on 26 May 2013

@author: dsnowdon
'''
import unittest

import emotions.motivation as motivation
import emotions.percept as percept
import emotions.satisfaction_vector as satisfaction_vector


class TestMotivation(unittest.TestCase):

    def test_id(self):
        m1 = motivation.Motivation("foo")
        m2 = motivation.Motivation("bar")
        self.assertNotEqual(m1.id, m2.id, "Identifiers should not be equal")

    def test_decay(self):
        m = motivation.Motivation("foo", initial_score=0.5, decay_rate=0.1)
        s1 = m.score
        s2 = m.decay()
        self.assertGreater(s2, s1, "Score after decay should have increased")
    
    def test_perception(self):
        m1 = motivation.Motivation("foo", initial_score=0.2)
        percepts = self.make_percepts([0.1, 0.5], m1)
        m1.update(percepts)
        self.assertEqual(0.8, m1.score, 
                         "Score should equal initial state plus sum of percept scores")

    def test_score_in_valid_range(self):
        m1 = motivation.Motivation("foo", initial_score=0.5)
        percepts = self.make_percepts([0.1, 0.5], m1)
        m1.update(percepts)
        print "score = {}, min = {}, max = {}".format(m1.score, m1.min_score, m1.max_score)
        self.assertLessEqual(m1.score, m1.max_score,  
                         "Score should be less than max score")
        self.assertGreaterEqual(m1.score, m1.min_score,  
                         "Score should be greater than min score")
    
    def test_max_change_per_update(self):
        m1 = motivation.Motivation("foo", initial_score=0.0, max_change=0.3)
        percepts = self.make_percepts([0.1, 0.5], m1)
        m1.update(percepts)
        self.assertLessEqual(m1.score, 0.3, "Change should be less than 0.3")
        
    def test_output_sv(self):
        m1 = motivation.Motivation("foo", initial_score=0.0)
        m2 = motivation.Motivation("bar", initial_score=0.0)        
        percepts = self.make_percepts([0.1, 0.5], m1)
        self.add_percepts(percepts, [0.2, 0.4], m2)
        sv = motivation.update_motivations([m1, m2], percepts)
        print str(sv)
        self.assertTrue(satisfaction_vector.is_equal(sv, {m1.id: 0.6, m2.id: 0.6}), 
                             "test motivations output sv")
        
        
    def add_percepts(self, percepts, values, motivation):
        for (percept, value) in zip(percepts, values):
            percept.satisfaction_vector[motivation.id] = value
        return percepts
    
    def make_percepts(self, values, motivation):
        percepts = []
        for score in values:
            sv = { motivation.id : score}
            percepts.append(percept.Percept(sv))
        return percepts



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
