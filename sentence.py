# -*- coding: utf-8 -*-

import random
import dico

class Sentence:
    def __init__(self):
        self.subject = "Il" 
        self.verb = "code"
        self.adverb = "rapidement"
    
    def print_sentence(self):
        print(f'{self.subject} {self.verb} {self.adverb}')

    def generate_random_sentence(self):
        self.subject = dico.subjects[ random.randint(0, len(dico.subjects)) ]
        self.verb = dico.verbs[ random.randint(0, len(dico.verbs)) ]
        self.adverb = dico.adverbs[ random.randint(0, len(dico.adverbs)) ]
