# -*- coding: utf-8 -*-

import random
import dico

class Sentence:
    def __init__(self):
        '''
        __init__()

        Auteur : VIDAL Antoine
        Projet : Générateur de phrase

        Description :
            Initialise une phrase avec trois mots aléatoires (mais qui seront remplacés par d'autres fonctions).

        Entrées :
            self : l'objet en question

        Sorties :
            -
        '''

        self.subject = ""
        self.verb = ""
        self.adverb = ""
    
    def print_sentence(self):
        '''
        print_sentence()

        Auteur : VIDAL Antoine
        Projet : Générateur de phrase

        Description :
            Affiche le sujet, le verbe et l'adverbe de l'objet en question pour former une phrase (avec un point à la fin).

        Entrées :
            self : l'objet en question

        Sorties :
            -
        '''
        print(f'{self.subject} {self.verb} {self.adverb}.')

    def generate_random_sentence(self):
        '''
        generate_random_sentence()

        Auteur : VIDAL Antoine
        Projet : Générateur de phrase

        Description :
            Créé une phrase aléatoire parmi les mots du dictionnaire en choississant un élément quelconque pour chaque liste.
            Un élément aléatoire de chaque liste est choisi. Il suffit ensuite de mettre les éléments à la suite pour obtenir une phrase.

        Entrées :
            self : l'objet en question

        Sorties :
            -
        '''

        self.subject = dico.subjects[ random.randint(0, len(dico.subjects)-1) ]
        self.verb = dico.verbs[ random.randint(0, len(dico.verbs)-1) ]
        self.adverb = dico.adverbs[ random.randint(0, len(dico.adverbs)-1) ]

    @staticmethod
    def check_is_in_dictionary(phrase: str):
        '''
        check_is_in_dictionary()

        Auteur : VIDAL Antoine
        Projet : Générateur de phrase

        Description :
            Prend une chaîne de caractères et indique si celle-ci est valide.
            Une chaîne de caractères est valide si son sujet, son verbe et son adverbe appartiennent tous au dictionnaire.

        Entrées :
            phrase : la chaîne de caractères à analyser

        Sorties :
            booléen : Vrai si la phrase est valide, Faux si la phrase est invalide
        '''

        #Retourner False dès qu'une erreur apparaît
        if not(phrase[0].isupper()):
            print(f'La phrase ne commence pas par une majuscule. Veuillez vous assurer que celle-ci commence par une majuscule.')
            return False

        if phrase[-1] != '.':
            print(f'La phrase ne se termine pas par un point. Veuillez en ajouter si vous en avez oublié un.')
            return False

        #Diviser la chaîne entière pour avoir accès plus facilement aux mots
        phraseSplit = phrase.split()

        #Enlever le point du dernier mot (l'adverbe)
        phraseSplit[-1] = phraseSplit[-1][:-1]

        #phraseSplit[-1] est ici l'adverbe
        if phraseSplit[-1] not in dico.adverbs:
            print(f'L\'adverbe "{phraseSplit[-1]}" ne se trouve pas dans la liste.')
            return False

        phraseSplit.pop(-1) #Enlever l'adverbe

        #phraseSplit[-1] est ici le verbe
        if phraseSplit[-1] not in dico.verbs:
            print(f'Le verbe "{phraseSplit[-1]}" ne se trouve pas dans la liste.')
            return False

        phraseSplit.pop(-1) #Enlever le verbe

        #Puisque le sujet peut être fait de plusieurs mots, il faut regrouper les mots restants pour avoir le sujet complet
        sjt = ' '.join(phraseSplit)

        if sjt not in dico.subjects:
            print(f'Le sujet "{sjt}" ne se trouve pas dans la liste.')
            return False

        return True
