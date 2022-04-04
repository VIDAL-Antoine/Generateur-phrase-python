# -*- coding: utf-8 -*-

from fileinput import filename
import main

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
    print(f'Sujets : {subjects}')
    print(f'Verbes : {verbs}')
    print(f'Adverbes : {adverbs}')

    