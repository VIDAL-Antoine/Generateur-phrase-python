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
        self.mbHasAdverb = True
    
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

        if(self.mbHasAdverb):
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
            self.mbHasAdverb = True
            self.mwAdverb = dico.gvAdverbs[ random.randint(0, len(dico.gvAdverbs)-1) ]
        else:
            self.mbHasAdverb = False

    def checkIsValidSentence(self, pwPhrase: str):
        '''
        checkIsValidSentence()

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

        lvPhraseSplit = [] #La phrase en paramètre mais séparée en tokens

        #Vérification si la phrase commence par une majuscule
        if not(pwPhrase[0].isupper()):
            print(f'La phrase ne commence pas par une majuscule. Veuillez vous assurer que celle-ci commence par une majuscule.')
            return False
        else:
            print(f'La phrase commence bien par une majuscule.')

        #Vérification si la phrase se termine par un point
        if pwPhrase[-1] == '.':
            print(f'La phrase se termine bien par un point.')
            pwPhrase = pwPhrase[:-1] ##Enlever le point de la phraseOn enlève le point de la phrase
        else:
            print(f'La phrase ne se termine pas par un point. Veuillez en ajouter si vous en avez oublié un.')
            return False

        print(f'Vérification du contenu de la phrase...')

        #Diviser la chaîne entière pour avoir accès plus facilement aux mots
        lvPhraseSplit = pwPhrase.split()

        #Vérifier le sujet
        print("Recherche du sujet...")
        self.mwSubject = checkGroupOfWordsInList(lvPhraseSplit, dico.gvSubjects)

        #Le sujet n'a pas été trouvé dans le dictionnaire
        if self.mwSubject == "":
            return False
        #Le sujet a pas été trouvé dans le dictionnaire
        else:
            pass

        #Vérifier le verbe
        print("Recherche du verbe...")
        self.mwVerb = checkGroupOfWordsInList(lvPhraseSplit, dico.gvVerbs)

        #Le verbe n'a pas été trouvé dans le dictionnaire
        if self.mwVerb == "":
            return False
        #Le verbe a été trouvé dans le dictionnaire
        else:
            pass

        #S'il ne reste plus de mots alors cela signifie que la phrase est sans adverbe. La phrase est valide jusqu'ici donc la phrase reste valide.
        if not(lvPhraseSplit):
            self.mbHasAdverb = False
            return True
        #Il reste des mots à traiter dans la phrase. Nous passons donc aux mots suivants.
        else:
            pass

        #Vérifier l'adverbe (puisque la phrase a des mots restants, il ne s'agit pas d'une phrase sans adverbe)
        print("Recherche de l'adverbe...")
        self.mwAdverb = checkGroupOfWordsInList(lvPhraseSplit, dico.gvAdverbs)

        #L'adverbe n'a pas été trouvé dans le dictionnaire
        if self.mwAdverb == "":
            self.mbHasAdverb = False
            return False
        #L'adverbe a été trouvé dans le dictionnaire
        else:
            self.mbHasAdverb = True

        return True

def checkGroupOfWordsInList(pvPhraseSplit : str, pvWordList : list):
    '''
    checkIsInDictionary()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Prend un groupe de mots et regarde si celui-ci est dans le dictionnaire.
        La fonction ajoute les mots un à un et regarde à chaque fois si le groupe de mots est valide.

    Entrées :
        pvPhraseSplit : la phrase à analyser
        pvWordList : la liste représentant les mots valides (le dictionnaire)

    Sorties :
        chaîne : la chaîne de caractères appartenant au dictionnaire, "" si la chaîne n'appartient pas au dictionnaire.
    '''

    lwString = pvPhraseSplit[0] #Chaîne de caractères représentant la phrase sans le verbe ni l'adverbe
    i = 0 #Compteur permettant de parcourir les mots de la liste

    #Parcours de la liste de mots tant qu'il reste des mots
    while i < len(pvPhraseSplit):

        #Le groupe de mots a été trouvé dans le dictionnaire. Il est donc valide.
        if lwString in pvWordList:
            print(f'"{lwString}" se trouve bien dans la liste.')
            del pvPhraseSplit[:i+1] #Supprimer les i premiers éléments de la liste
            return lwString

        #Le groupe de mots n'a pas été trouvé dans le dictionnaire. Nous ajoutons donc le mot suivant.
        else:
            i += 1
            try:
                lwString = lwString + ' ' + pvPhraseSplit[i]

            #Si les instructions échouent, cela signifie que la fin de la phrase est atteinte (puisque i >= len(pvPhraseSplit)).
            #Il n'y a plus de mots à tester. Le groupe de mots n'est donc pas dans le dictionnaire. La phrase n'est pas valide.
            except IndexError:
                print(f'"{lwString}" non trouvé dans la liste.')
                return ""
