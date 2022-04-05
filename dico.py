# -*- coding: utf-8 -*-

import string
import sys

def open_txt(fileName: string):
    listStrings = []
    try:
        with open(fileName, "r") as fileSubjects:
            listStrings = fileSubjects.readlines()
    except FileNotFoundError:
        print(f'Fichier "{fileName}" inexistant. Vérifiez que vous avez mis les bons noms.')
        sys.exit("Fin du programme. Fichier non trouvé.")

    #Enlever les espaces et '\n' inutiles
    for i in range(len(listStrings)):
        listStrings[i] = listStrings[i].strip()
    
    return listStrings

def open_dictionary():
    global subjects
    global verbs
    global adverbs

    subjects = []
    verbs = []
    adverbs = []

    subjects = open_txt('words/sujets.txt')
    verbs = open_txt('words/verbes.txt')
    adverbs = open_txt('words/adverbes.txt')

def add_subject():
    sjt = input(f'Veuillez saisir le sujet que vous souhaitez ajouter. Nous supposons que vous tapez un sujet qui existe vraiment :\n')
    isValidString = True

    if not(sjt[0].isupper()):
        print(f'Le premier caractère n\'est pas une majuscule. Assurez-vous bien qu\'il s\'agisse d\'une majuscule.')
        isValidString = False

    for letter in sjt:
        if letter.isdigit():
            print(f'Un chiffre est présent dans la chaîne. Celle-ci ne doit contenir aucun chiffre.')
            isValidString = False
            break

    if isValidString:
        sjt.strip()
        if sjt not in subjects:
            subjects.append(sjt)
            print(f'"{sjt}" ajouté dans les sujets.')
        else:
            print(f'Le sujet "{sjt}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')

def add_verb():
    verb = input(f'Veuillez saisir le verbe que vous souhaitez ajouter. Nous supposons que vous tapez un verbe qui existe vraiment :\n')
    isValidString = True

    for letter in verb:
        if letter.isupper():
            print(f'Une majuscule est présente dans la chaîne. Celle-ci ne doit contenir aucune majuscule.')
            isValidString = False
            break
        if letter.isspace():
            print(f'Un espace est présent dans la chaîne. Celle-ci ne doit contenir aucun espace.')
            isValidString = False
            break
        if letter.isdigit():
            print(f'Un chiffre est présent dans la chaîne. Celle-ci ne doit contenir aucun chiffre.')
            isValidString = False
            break

    if isValidString:
        verb.strip()
        if verb not in verbs:
            verbs.append(verb)
            print(f'"{verb}" ajouté dans les verbes.')
        else:
            print(f'Le verbe "{verb}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')

def add_adverb():
    adverb = input(f'Veuillez saisir l\'adverbe que vous souhaitez ajouter. Nous supposons que vous tapez un adverbe qui existe vraiment :\n')
    isValidString = True

    for letter in adverb:
        if letter.isupper():
            print(f'Une majuscule est présente dans la chaîne. Un adverbe ne doit contenir aucune majuscule.')
            isValidString = False
            break
        if letter.isspace():
            print(f'Un espace est présent dans la chaîne. Celle-ci ne doit contenir aucun espace.')
            isValidString = False
            break
        if letter.isdigit():
            print(f'Un chiffre est présent dans la chaîne. Celle-ci ne doit contenir aucun chiffre.')
            isValidString = False
            break

    if isValidString:
        adverb.strip()
        if adverb not in adverbs:
            adverbs.append(adverb)
            print(f'"{adverb}" ajouté dans les adverbes.')
        else:
            print(f'L\'adverbe "{adverb}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')

def remove_item(listWords: list):
    item = input(f'Veuillez saisir l\'objet que vous souhaitez retirer. Nous supposons que vous tapez un mot qui existe vraiment :\n')

    try:
        listWords.remove(item)
        print(f'"{item}" retiré du dictionnaire.')
    except ValueError:
        print(f'"{item}" non trouvé dans la liste. Vérifiez qu\'il s\'y trouve bien.')


def save_dico():
    with open('words/sujets.txt', 'w') as fileSubjects:
        for sjt in subjects:
            fileSubjects.write("%s\n" % sjt)

    with open('words/verbes.txt', 'w') as fileVerbs:
        for verb in verbs:
            fileVerbs.write("%s\n" % verb)

    with open('words/adverbes.txt', 'w') as fileAdverbs:
        for adverb in adverbs:
            fileAdverbs.write("%s\n" % adverb)

def print_dictionary():
    print("\n##### Dictionnaire #####\n")
    print(f'Sujets : {subjects}\n')
    print(f'Verbes : {verbs}\n')
    print(f'Adverbes : {adverbs}\n')
