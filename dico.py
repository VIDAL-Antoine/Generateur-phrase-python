# -*- coding: utf-8 -*-

def open_txt(fileName):
    listStrings = []
    with open(fileName, "r") as fileSubjects:
        listStrings = fileSubjects.readlines()

    #Enlever les espaces et \n inutiles
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

def print_dictionary():
    print("\n##### Dictionnaire #####\n")
    print(f'Sujets : {subjects}\n')
    print(f'Verbes : {verbs}\n')
    print(f'Adverbes : {adverbs}\n')
