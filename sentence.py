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

    def checkIsInDictionary(self, pwPhrase: str):
        '''
        checkIsInDictionary()

        Auteur : VIDAL Antoine
        Projet : Générateur de phrase

        Description :
            Prend une chaîne de caractères et indique si celle-ci est valide.
            Une chaîne de caractères est valide si son sujet, son verbe et facultativement son adverbe appartiennent tous au dictionnaire.

        Entrées :
            self : l'objet en question
            pwPhrase : la chaîne de caractères à analyser

        Sorties :
            booléen : Vrai si la phrase est valide, Faux si la phrase est invalide
        '''

        lvPhraseSplit = [] #La phrase en paramtère mais séparée en tokens

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

        #Enlever le point du dernier mot
        lvPhraseSplit[-1] = lvPhraseSplit[-1][:-1]

        #Vérifier le sujet
        self.mwSubject = checkGroupOfWordsInList(lvPhraseSplit, dico.gvSubjects)
        if self.mwSubject == "":
            return False
        else:
            #Un sujet a bien été trouvé dans le dictionnaire donc nous continuons
            pass

        self.mwVerb = checkGroupOfWordsInList(lvPhraseSplit, dico.gvVerbs)
        if self.mwVerb == "":
            return False
        else:
            #Un verbe a bien été trouvé dans le dictionnaire donc nous continuons
            pass

        self.mwAdverb = checkGroupOfWordsInList(lvPhraseSplit, dico.gvAdverbs)
        if self.mwAdverb == "Adverbe absent de la liste":
            self.mwAdverb == ""
            return False
        else:
            #Un adverbe a bien été trouvé dans le dictionnaire ou la phrase n'a pas d'adverbe donc nous nous arrêtons
            pass

        return True

def checkGroupOfWordsInList(pvPhraseSplit : str, pvWordList : list):
    '''
    checkIsInDictionary()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Prend une chaîne de caractères et indique si celle-ci est valide.
        Une chaîne de caractères est valide si son sujet, son verbe et facultativement son adverbe appartiennent tous au dictionnaire.

    Entrées :
        self : l'objet en question
        pwPhrase : la chaîne de caractères à analyser

    Sorties :
        chaîne : la chaîne de caractères appartenant au dictionnaire, "" si la chaîne n'appartient pas au dictionnaire ou si la phrase n'a pas d'adverbe, "Adverbe absent de la liste" si la fin de la phrase contient un adverbe non présent dans la liste. 
    '''

    try:
        lwString = pvPhraseSplit[0] #Chaîne de caractères représentant la phrase sans le verbe ni l'adverbe
        i = 0 #Compteur permettant de parcourir les mots de la liste

        while i < len(pvPhraseSplit):
            if lwString in pvWordList:
                print(f'"{lwString}" se trouve bien dans la liste.')
                del pvPhraseSplit[:i+1]
                return lwString

            #Puisque l'adverbe est facultatif, il faut différencier le cas d'un adverbe absent d'un adverbe mal écrit
            #On regarde donc si le dernier groupe de mots est bien dans la liste des adverbes (si non cela veut dire qu'il a mal été écrit)
            elif i == len(pvPhraseSplit)-1 and lwString not in dico.gvAdverbs:
                    return "Adverbe absent de la liste"
            else:
                #
                pass
            i += 1
            lwString = lwString + ' ' + pvPhraseSplit[i]

    except IndexError:
        print(f'Chaîne non trouvée. Il se peut que la phrase soit sans adverbe ou que le mot tapé n\'existe pas.')
        return ""
