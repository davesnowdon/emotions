'''
Created on 8 Jun 2013

@author: dsnowdon
'''

class Percept(object):
    def __init__(self, satisfaction_vector=None):
        super(Percept, self).__init__()
        if satisfaction_vector is None:
            satisfaction_vector = {}
        self.satisfaction_vector = satisfaction_vector