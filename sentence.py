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

        self.mwSubject = ""
        self.mwVerb = ""
        self.mwAdverb = ""
        self.mbhasAdverb = True
    
    def printSentence(self):
        '''
        printSentence()

        Auteur : VIDAL Antoine
        Projet : Générateur de phrase

        Description :
            Affiche le sujet, le verbe et l'adverbe de l'objet en question pour former une phrase (avec un point à la fin).

        Entrées :
            self : l'objet en question

        Sorties :
            -
        '''

        if(self.mbhasAdverb):
            print(f'{self.mwSubject} {self.mwVerb} {self.mwAdverb}.')
        else:
            print(f'{self.mwSubject} {self.mwVerb}.')

    def generateRandomSentence(self):
        '''
        generateRandomSentence()

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

        self.mwSubject = dico.gvSubjects[ random.randint(0, len(dico.gvSubjects)-1) ]
        self.mwVerb = dico.gvVerbs[ random.randint(0, len(dico.gvVerbs)-1) ]

        #Prendre un adverbe de façon aléatoire
        if(random.choice([True, False])):
            self.mbhasAdverb = True
            self.mwAdverb = dico.gvAdverbs[ random.randint(0, len(dico.gvAdverbs)-1) ]
        else:
            self.mbhasAdverb = False

    @staticmethod
    def checkIsInDictionary(pwPhrase: str):
        '''
        checkIsInDictionary()

        Auteur : VIDAL Antoine
        Projet : Générateur de phrase

        Description :
            Prend une chaîne de caractères et indique si celle-ci est valide.
            Une chaîne de caractères est valide si son sujet, son verbe et son adverbe appartiennent tous au dictionnaire.

        Entrées :
            pwPhrase : la chaîne de caractères à analyser

        Sorties :
            booléen : Vrai si la phrase est valide, Faux si la phrase est invalide
        '''

        lvPhraseSplit = [] #La phrase en paramtère mais séparée en tokens
        lwSubject = "" #Chaîne de caractères représentant la phrase sans le verbe ni l'adverbe

        if not(pwPhrase[0].isupper()):
            print(f'La phrase ne commence pas par une majuscule. Veuillez vous assurer que celle-ci commence par une majuscule.')
            return False
        else:
            print(f'La phrase commence bien par une majuscule.')

        if pwPhrase[-1] != '.':
            print(f'La phrase ne se termine pas par un point. Veuillez en ajouter si vous en avez oublié un.')
            return False
        else:
            print(f'La phrase se termine bien par un point.')

        print(f'Vérification du contenu de la phrase...')

        #Diviser la chaîne entière pour avoir accès plus facilement aux mots
        lvPhraseSplit = pwPhrase.split()

        #Enlever le point du dernier mot (l'adverbe)
        lvPhraseSplit[-1] = lvPhraseSplit[-1][:-1]

        #lvPhraseSplit[-1] est ici l'adverbe
        if lvPhraseSplit[-1] not in dico.gvAdverbs:
            print(f'Le mot "{lvPhraseSplit[-1]}" ne se trouve pas dans la liste des adverbes. Il peut s\'agir d\'un verbe (dans ce cas la phrase sera sans adverbe).')
        else:
            #Le dernier mot est bien un adverbe donc il faut l'enlever
            print(f'Le mot "{lvPhraseSplit[-1]}" se trouve bien dans la liste des adverbes.')
            lvPhraseSplit.pop(-1)

        #lvPhraseSplit[-1] est ici le verbe
        if lvPhraseSplit[-1] not in dico.gvVerbs:
            print(f'Le verbe "{lvPhraseSplit[-1]}" ne se trouve pas dans la liste des verbes.')
            return False
        else:
            print(f'Le verbe "{lvPhraseSplit[-1]}" se trouve bien dans la liste des verbes.')

        lvPhraseSplit.pop(-1) #Enlever le verbe

        #Puisque le sujet peut être fait de plusieurs mots, il faut regrouper les mots restants pour avoir le sujet complet
        lwSubject = ' '.join(lvPhraseSplit)

        if lwSubject not in dico.gvSubjects:
            print(f'Le sujet "{lwSubject}" ne se trouve pas dans la liste des sujets.')
            return False
        else:
            print(f'Le sujet "{lwSubject}" se trouve bien dans la liste des sujets.')

        return True
