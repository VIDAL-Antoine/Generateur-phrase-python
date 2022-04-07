# -*- coding: utf-8 -*-

import sys

def openTxt(pwFileName: str):
    '''
    openTxt()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Ouvre un fichier texte et récupère les mots qui y sont. Une ligne représente une fonction grammaticale (sujet...).
        Enfin elle enlève les espaces et caractères inutiles ("\n"...) pour n'avoir que des lettres.

    Entrées :
        lwFileName : le chemin du fichier à lire

    Sorties :
        listStrings : la liste contenant les données du fichier lu
    '''

    lvListStrings = [] #La liste des mots que le dictionnaire va recevoir

    try:
        with open(pwFileName, "r") as lwFileSubjects:
            lvListStrings = lwFileSubjects.readlines()
    except FileNotFoundError:
        print(f'Fichier "{pwFileName}" inexistant. Vérifiez que vous avez mis les bons noms.')
        sys.exit("Fin du programme. Fichier non trouvé.")

    #Enlever les espaces et '\n' inutiles
    for i in range(len(lvListStrings)):
        lvListStrings[i] = lvListStrings[i].strip()
    
    return lvListStrings

def openDictionary():
    '''
    openDictionary()

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

    global gvSubjects #La liste des sujets du dictionnaire
    global gvVerbs #La liste des verbes du dictionnaire
    global gvAdverbs #La liste des adverbes du dictionnaire

    gvSubjects = []
    gvVerbs = []
    gvAdverbs = []

    print(f'Lecture des sujets...')
    gvSubjects = openTxt('words/sujets.txt')
    print(f'Lecture terminée.')

    print(f'Lecture des verbes...')
    gvVerbs = openTxt('words/verbes.txt')
    print(f'Lecture terminée.')

    print(f'Lecture des adverbes...')
    gvAdverbs = openTxt('words/adverbes.txt')
    print(f'Lecture terminée.')

def addSubject():
    '''
    addSubject()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Ajoute un sujet à la liste des sujets.
        La fonction regarde d'abord si le sujet souhaité est valide et n'existe pas encore puis l'ajoute.
        Un sujet est valide s'il commence par une majuscule et s'il contient uniquement des lettres, des espaces ou des apostrophes.

    Entrées :
        -

    Sorties :
        -
    '''

    lwString = input(f'Veuillez saisir la chaîne que vous souhaitez ajouter. Nous supposons que vous tapez un sujet qui existe vraiment :\n') #Chaîne de caractères représentant le sujet à ajouter

    #Vérifier que la chaîne tapée est valide
    if lwString:
        print(f'La chaîne n\'est pas vide. Vérification de la validité de la chaîne...')
    else:
        print(f'La chaîne est vide. Veuillez saisir des caractères pour pouvoir ajouter une chaîne.')
    if lwString[0].isupper():
        print(f'Le premier caractère est bien une majuscule.')
    else:
        print(f'Le premier caractère n\'est pas une majuscule. Assurez-vous bien qu\'il s\'agisse d\'une majuscule.')
        return

    for liLetter in lwString[1:len(lwString)]:
        print(liLetter)
        if (liLetter.isalpha() and liLetter.islower()) or liLetter == '\'' or liLetter.isspace():
            #Le caractère est correct, on passe au suivant
            pass
        else:
            print(f'Une chaîne ne peut contenir que des lettres ou un \'. Vérifier par exemple qu\'elle ne contient pas de chiffres ou des majuscules (en dehors de la première lettre).')
            return

    print(f'Les caractères de la chaîne sont corrects.')

    lwString = lwString.strip() #Enlever les espaces inutiles
    if lwString not in gvSubjects:
        gvSubjects.append(lwString)
        print(f'"{lwString}" ajouté dans la liste.')
    else:
        print(f'"{lwString}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')

def addVerbAdverb(pvListWords : list):
    '''
    addVerbAdverb()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Ajoute une chaîne saisie à la liste pvListWords.
        La fonction regarde d'abord si la chaîne saisie est valide et n'existe pas encore puis l'ajoute.
        Une chaîne est valide si elle contient uniquement des lettres, des espaces ou des apostrophes.

    Entrées :
        pvListWords : la liste dans laquelle la chaîne saisie sera ajoutée

    Sorties :
        -
    '''

    lwString = input(f'Veuillez saisir la chaîne que vous souhaitez ajouter. Nous supposons que vous tapez un sujet qui existe vraiment :\n') #Chaîne de caractères représentant le sujet à ajouter

    #Vérifier que la chaîne tapée est valide
    if lwString:
        print(f'La chaîne n\'est pas vide. Vérification de la validité de la chaîne...')
    else:
        print(f'La chaîne est vide. Veuillez saisir des caractères pour pouvoir ajouter une chaîne.')

    for liLetter in lwString:
        if (liLetter.isalpha() and liLetter.islower()) or liLetter == '\'' or liLetter.isspace():
            #Le caractère est correct, on passe au suivant
            pass
        else:
            print(f'Une chaîne ne peut contenir que des lettres ou un \'. Vérifier par exemple qu\'elle ne contient pas de chiffres ou des majuscules (dans le cas d\'un verbe ou adverbe).')
            return

    print(f'Les caractères de la chaîne sont corrects.')

    lwString = lwString.strip() #Enlever les espaces inutiles
    if lwString not in pvListWords:
        pvListWords.append(lwString)
        print(f'"{lwString}" ajouté dans la liste.')
    else:
        print(f'"{lwString}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')

def removeItem(pvListWords: list):
    '''
    removeItem()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Demande une chaîne de caractères puis l'enlève de la liste souhaitée si celle-ci la contient.

    Entrées :
        pvListWords : la liste de mots qui doit avoir un élément retiré

    Sorties :
        -
    '''

    lwItem = input(f'Veuillez saisir l\'objet que vous souhaitez retirer. Nous supposons que vous tapez un mot qui existe vraiment :\n') #Chaîne de caractères représentant l'objet à supprimer

    try:
        pvListWords.remove(lwItem)
        print(f'"{lwItem}" retiré du dictionnaire.')
    except ValueError:
        print(f'"{lwItem}" non trouvé dans la liste. Vérifiez qu\'il s\'y trouve bien.')


def saveDictionary():
    '''
    saveDictionary()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
        Enregistre le dictionnaire dans les fichiers adéquats. Si le fichier n'existe pas il est crée.

    Entrées :
        -

    Sorties :
        -
    '''

    print()
    print(f'Écriture des sujets dans le fichier...')
    with open('words/sujets.txt', 'w') as lwFileSubjects:
        for liSubject in gvSubjects:
            lwFileSubjects.write("%s\n" % liSubject)
    print(f'Écriture terminée.')

    print(f'Écriture des verbes dans le fichier...')
    with open('words/verbes.txt', 'w') as lwFileVerbs:
        for liVerb in gvVerbs:
            lwFileVerbs.write("%s\n" % liVerb)
    print(f'Écriture terminée.')

    print(f'Écriture des adverbes dans le fichier...')
    with open('words/adverbes.txt', 'w') as lwFileAdverbs:
        for liAdverb in gvAdverbs:
            lwFileAdverbs.write("%s\n" % liAdverb)
    print(f'Écriture terminée.')

def printDictionary():
    '''
    printDictionary()

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
    print(f'Sujets : {gvSubjects}\n')
    print(f'Verbes : {gvVerbs}\n')
    print(f'Adverbes : {gvAdverbs}\n')
