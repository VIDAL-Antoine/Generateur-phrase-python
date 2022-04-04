# -*- coding: utf-8 -*-

import sys

def open_txt(fileName):
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
