'''
Created on 26 May 2013

@author: dsnowdon
'''

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
                 layer=LAYER_PHYSICAL,
                 inhibition_direction=INHIBIT_DOWN,
                 inhibition_multiplier=0):
        super(Motivation, self).__init__()
        self.id = get_id()
        self.name = name
        self.score = initial_score
        self.min_score = min_score,
        self.max_score = max_score
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
