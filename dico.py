# -*- coding: utf-8 -*-

import sys

def open_txt(fileName: str):
    '''
    open_txt()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Ouvre un fichier texte et récupère les mots qui y sont. Une ligne représente une fonction grammaticale (sujet...).
        Enfin elle enlève les espaces et caractères inutiles ("\n"...) pour n'avoir que des lettres.

    Entrées :
        fileName : le chemin du fichier à lire

    Sorties :
        listStrings : la liste contenant les données du fichier lu
    '''

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
    '''
    open_dictionary()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Ouvre le dictionnaire en entier.
        Pour cela il ouvre les sujets puis les verbes et enfin les adverbes.

    Entrées :
        -

    Sorties :
        -
    '''

    global subjects
    global verbs
    global adverbs

    subjects = []
    verbs = []
    adverbs = []

    print(f'Lecture des sujets...')
    subjects = open_txt('words/sujets.txt')
    print(f'Lecture terminée.')

    print(f'Lecture des verbes...')
    verbs = open_txt('words/verbes.txt')
    print(f'Lecture terminée.')

    print(f'Lecture des adverbes...')
    adverbs = open_txt('words/adverbes.txt')
    print(f'Lecture terminée.')

def add_subject():
    '''
    add_subject()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Ajoute un sujet à la liste des sujets.
        La fonction regarde d'abord si le sujet souhaité est valide et n'existe pas encore puis l'ajoute.
        Un sujet est valide s'il commence par une majuscule (il peut donc contenir plusieurs mots pour par exemple avoir des adjectifs) et contient uniquement des lettres.

    Entrées :
        -

    Sorties :
        -
    '''

    sjt = input(f'Veuillez saisir le sujet que vous souhaitez ajouter. Nous supposons que vous tapez un sujet qui existe vraiment :\n')
    isValidString = True

    #Vérifier que la chaîne tapée est valide
    if not(sjt[0].isupper()):
        print(f'Le premier caractère n\'est pas une majuscule. Assurez-vous bien qu\'il s\'agisse d\'une majuscule.')
        isValidString = False

    for letter in sjt:
        if letter.isdigit():
            print(f'Un chiffre est présent dans la chaîne. Celle-ci ne doit contenir aucun chiffre.')
            isValidString = False
            break
        if letter != '\'' and not(letter.isalpha()):
            print(f'Une chaîne de caractères ne peut contenir que des lettres ou un \'. Vérifier par exemple qu\'elle ne contient pas de chiffres.')
            isValidString = False
            break

    if isValidString:
        sjt.strip() #Enlever les espaces inutiles
        if sjt not in subjects:
            subjects.append(sjt)
            print(f'"{sjt}" ajouté dans les sujets.')
        else:
            print(f'Le sujet "{sjt}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')

def add_verb():
    '''
    add_verb()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Ajoute un verbe à la liste des verbes.
        La fonction regarde d'abord si le verbe souhaité est valide et n'existe pas encore puis l'ajoute.
        Un verbe est valide s'il contient uniquement des lettres minuscules.

    Entrées :
        -

    Sorties :
        -
    '''

    verb = input(f'Veuillez saisir le verbe que vous souhaitez ajouter. Nous supposons que vous tapez un verbe qui existe vraiment :\n')
    isValidString = True

    #Vérifier que la chaîne tapée est valide
    for letter in verb:
        if letter.isupper():
            print(f'Une majuscule est présente dans la chaîne. Celle-ci ne doit contenir aucune majuscule.')
            isValidString = False
            break
        if not(letter.isalpha()):
            print(f'Un verbe ne peut contenir que des lettres minuscules. Vérifier par exemple qu\'elle ne contient pas de chiffres.')
            isValidString = False
            break

    if isValidString:
        verb.strip() #Enlever les espaces inutiles
        if verb not in verbs:
            verbs.append(verb)
            print(f'"{verb}" ajouté dans les verbes.')
        else:
            print(f'Le verbe "{verb}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')

def add_adverb():
    '''
    add_adverb()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Ajoute un adverbe à la liste des adverbes.
        La fonction regarde d'abord si l'adverbe souhaité est valide et n'existe pas encore puis l'ajoute.
        Un adverbe est valide s'il contient uniquement des lettres minuscules.

    Entrées :
        -

    Sorties :
        -
    '''

    adverb = input(f'Veuillez saisir l\'adverbe que vous souhaitez ajouter. Nous supposons que vous tapez un adverbe qui existe vraiment :\n')
    isValidString = True

    #Vérifier que la chaîne tapée est valide
    for letter in adverb:
        if letter.isupper():
            print(f'Une majuscule est présente dans la chaîne. Un adverbe ne doit contenir aucune majuscule.')
            isValidString = False
            break
        if not(letter.isalpha()):
            print(f'Un adverbe ne peut contenir que des lettres minuscules. Vérifier par exemple qu\'elle ne contient pas de chiffres.')
            isValidString = False
            break

    if isValidString:
        adverb.strip() #Enlever les espaces inutiles
        if adverb not in adverbs:
            adverbs.append(adverb)
            print(f'"{adverb}" ajouté dans les adverbes.')
        else:
            print(f'L\'adverbe "{adverb}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')

def remove_item(listWords: list):
    '''
    remove_item()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Demande une chaîne de caractères puis l'enlève de la liste souhaitée si celle-ci la contient.

    Entrées :
        listWords : la liste de mots qui doit avoir un élément retiré

    Sorties :
        -
    '''

    item = input(f'Veuillez saisir l\'objet que vous souhaitez retirer. Nous supposons que vous tapez un mot qui existe vraiment :\n')

    try:
        listWords.remove(item)
        print(f'"{item}" retiré du dictionnaire.')
    except ValueError:
        print(f'"{item}" non trouvé dans la liste. Vérifiez qu\'il s\'y trouve bien.')


def save_dictionary():
    '''
    save_dictionary()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Enregistre le dictionnaire dans les fichiers adéquats. Si le fichier n'existe pas il est crée.

    Entrées :
        -

    Sorties :
        -
    '''

    print(f'Écriture des sujets dans le fichier...')
    with open('words/sujets.txt', 'w') as fileSubjects:
        for sjt in subjects:
            fileSubjects.write("%s\n" % sjt)
    print(f'Écriture terminée.')

    print(f'Écriture des verbes dans le fichier...')
    with open('words/verbes.txt', 'w') as fileVerbs:
        for verb in verbs:
            fileVerbs.write("%s\n" % verb)
    print(f'Écriture terminée.')

    print(f'Écriture des adverbes dans le fichier...')
    with open('words/adverbes.txt', 'w') as fileAdverbs:
        for adverb in adverbs:
            fileAdverbs.write("%s\n" % adverb)
    print(f'Écriture terminée.')

def print_dictionary():
    '''
    print_dictionary()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Affiche le dictionnaire (sous formes de listes) sur le terminal dans l'ordre suivant : sujets, verbes puis adverbes.

    Entrées :
        -

    Sorties :
        -
    '''

    print("\n##### Dictionnaire #####\n")
    print(f'Sujets : {subjects}\n')
    print(f'Verbes : {verbs}\n')
    print(f'Adverbes : {adverbs}\n')
