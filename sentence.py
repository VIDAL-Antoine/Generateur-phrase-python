# -*- coding: utf-8 -*-

import random
import string
import dico

class Sentence:
    def __init__(self):
        self.subject = "Il"
        self.verb = "code"
        self.adverb = "rapidement"
    
    def print_sentence(self):
        print(f'{self.subject} {self.verb} {self.adverb}.')

    def generate_random_sentence(self):
        self.subject = dico.subjects[ random.randint(0, len(dico.subjects)-1) ]
        self.verb = dico.verbs[ random.randint(0, len(dico.verbs)-1) ]
        self.adverb = dico.adverbs[ random.randint(0, len(dico.adverbs)-1) ]

    @staticmethod
    def check_is_in_dico(phrase: string):
        if not(phrase[0].isupper()):
            print(f'La phrase ne commence pas par une majuscule. Veuillez vous assurer que celle-ci commence par une majuscule.')
            return False

        if phrase[-1] != '.':
            print(f'La phrase ne se termine pas par un point. Veuillez en ajouter si vous en avez oublié un.')
            return False

        phraseSplit = phrase.split()
        phraseSplit[-1] = phraseSplit[-1][:-1] #Enlever le point du dernier mot (l'adverbe)

        if phraseSplit[-1] not in dico.adverbs:
            return False

        phraseSplit.pop(-1) #Enlever l'adverbe

        if phraseSplit[-1] not in dico.verbs:
            return False

        phraseSplit.pop(-1) #Enlever le verbe
        sjt = ' '.join(phraseSplit) #Former le sujet complet

        if sjt not in dico.subjects:
            return False

        return True
