'''
Created on 26 May 2013

@author: dsnowdon
'''
import math 

LAYER_PHYSICAL = 1
LAYER_SAFETY = 2
LAYER_SOCIAL = 3
LAYER_SKILLS_VALUES = 4
LAYER_CONTRIBUTION = 5

INHIBIT_DOWN = 1
INHIBIT_UP = 2

DEFAULT_DECAY_RATE = 0.01

next_motivation_id = 0


def get_id():
    global next_motivation_id
    next_motivation_id = next_motivation_id + 1
    return next_motivation_id


class Motivation(object):
    def __init__(self, name,
                 initial_score=0.0,
                 min_score=0.0,
                 max_score=1.0,
                 decay_rate=DEFAULT_DECAY_RATE,
                 max_change=1.0,
                 layer=LAYER_PHYSICAL,
                 inhibition_direction=INHIBIT_DOWN,
                 inhibition_multiplier=0):
        super(Motivation, self).__init__()
        self.id = get_id()
        self.name = name
        self.score = initial_score
        self.min_score = min_score
        self.max_score = max_score
        self.max_change = max_change
        self.score_decay = decay_rate
        self.layer = layer
        self.inhibition_direction = inhibition_direction
        self.inhibition_multiplier = inhibition_multiplier

    def decay(self):
        self.score = self.score + self.score_decay
        self.constrain()
        return self.score

    def constrain(self):
        """ Constrain the score to be within min_score and max_score"""
        self.score = max(self.score, self.min_score)
        self.score = min(self.score, self.max_score)
    
    def update(self, percepts):
        percept_svs = [percept.satisfaction_vector[self.id ] for percept in percepts]
        change = sum(percept_svs)
        if abs(change) > self.max_change:
            self.score += math.copysign(self.max_change, change)
        else:
            self.score += change
            
        self.constrain()
        return self.score
        
def update_motivations(motivations, percepts):
    output_sv = {}
    for motivation in motivations:
        output_sv[motivation.id] = motivation.update(percepts)
    return output_sv