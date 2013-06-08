'''
Created on 26 May 2013

@author: dns
'''
import unittest

import emotions.motivation as motivation


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


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
