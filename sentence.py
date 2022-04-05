# -*- coding: utf-8 -*-

import random
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
    def check_is_in_dico(phrase: str):
        if not(phrase[0].isupper()):
            print(f'La phrase ne commence pas par une majuscule. Veuillez vous assurer que celle-ci commence par une majuscule.')
            return False

        if phrase[-1] != '.':
            print(f'La phrase ne se termine pas par un point. Veuillez en ajouter si vous en avez oublié un.')
            return False

        phraseSplit = phrase.split()
        phraseSplit[-1] = phraseSplit[-1][:-1] #Enlever le point du dernier mot (l'adverbe)

        if phraseSplit[-1] not in dico.adverbs:
            print(f'L\'adverbe "{phraseSplit[-1]}" ne se trouve pas dans la liste.')
            return False

        phraseSplit.pop(-1) #Enlever l'adverbe

        if phraseSplit[-1] not in dico.verbs:
            print(f'Le verbe "{phraseSplit[-1]}" ne se trouve pas dans la liste.')
            return False

        phraseSplit.pop(-1) #Enlever le verbe
        sjt = ' '.join(phraseSplit) #Former le sujet complet

        if sjt not in dico.subjects:
            print(f'Le sujet "{sjt}" ne se trouve pas dans la liste.')
            return False

        return True
