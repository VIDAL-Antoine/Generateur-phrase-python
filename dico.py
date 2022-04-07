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
        Un sujet est valide s'il commence par une majuscule (il peut donc contenir plusieurs mots pour par exemple avoir des adjectifs) et contient uniquement des lettres.

    Entrées :
        -

    Sorties :
        -
    '''

    lwSubject = input(f'Veuillez saisir le sujet que vous souhaitez ajouter. Nous supposons que vous tapez un sujet qui existe vraiment :\n') #Chaîne de caractères représentant le sujet à ajouter
    lbIsValidString = True #Booléen permettant de savoir si une chaîne de caractères est valide.

    if not(lwSubject):
        print("La chaîne est vide. Veuillez saisir des caractères pour pouvoir les ajouter au dictionnaire.")
        lbIsValidString = False
        return
    else:
        print(f'La chaîne n\'est pas vide. Vérification de la validité de la chaîne...')

    #Vérifier que la chaîne tapée est valide
    if not(lwSubject[0].isupper()):
        print(f'Le premier caractère n\'est pas une majuscule. Assurez-vous bien qu\'il s\'agisse d\'une majuscule.')
        lbIsValidString = False
    else:
        print(f'Le premier caractère est bien une majuscule.')

    for liLetter in lwSubject:
        if liLetter.isdigit():
            print(f'Un chiffre est présent dans la chaîne. Un sujet ne doit contenir aucun chiffre.')
            lbIsValidString = False
            break
        else:
            #La chaîne reste valide.
            pass
        if (liLetter != '\'') and (not(liLetter.isalpha())) and not(liLetter.isspace()):
            print(f'Un sujet ne peut contenir que des lettres ou un \'. Vérifier par exemple qu\'il ne contient pas de chiffres.')
            lbIsValidString = False
            break
        else:
            #La chaîne reste valide.
            pass

    if lbIsValidString:
        lwSubject = lwSubject.strip() #Enlever les espaces inutiles
        if lwSubject not in gvSubjects:
            gvSubjects.append(lwSubject)
            print(f'"{lwSubject}" ajouté dans les sujets.')
        else:
            print(f'Le sujet "{lwSubject}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')
    else:
        #La chaîne n'est pas valide. On ne la cherche donc pas dans la liste.
        pass

def addVerb():
    '''
    addVerb()

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

    lwVerb = input(f'Veuillez saisir le verbe que vous souhaitez ajouter. Nous supposons que vous tapez un verbe qui existe vraiment :\n') #Chaîne de caractères représentant le verbe à ajouter
    lbIsValidString = True #Booléen permettant de savoir si une chaîne de caractères est valide.

    if not(lwVerb):
        print("La chaîne est vide. Veuillez saisir des caractères pour pouvoir les ajouter au dictionnaire.")
        lbIsValidString = False
        return
    else:
        print(f'La chaîne n\'est pas vide. Vérification de la validité de la chaîne...')

    #Vérifier que la chaîne tapée est valide
    for liLetter in lwVerb:
        if liLetter.isupper():
            print(f'Une majuscule est présente dans la chaîne. Un verbe ne doit contenir aucune majuscule.')
            lbIsValidString = False
            break
        else:
            #La chaîne reste valide.
            pass
        if not(liLetter.isalpha()):
            print(f'Un verbe ne peut contenir que des lettres minuscules. Vérifier par exemple qu\'il ne contient pas de chiffres ou d\'espaces.')
            lbIsValidString = False
            break
        else:
            #La chaîne reste valide.
            pass

    if lbIsValidString:
        lwVerb = lwVerb.strip() #Enlever les espaces inutiles
        if lwVerb not in gvVerbs:
            gvVerbs.append(lwVerb)
            print(f'"{lwVerb}" ajouté dans les verbes.')
        else:
            print(f'Le verbe "{lwVerb}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')
    else:
        #La chaîne n'est pas valide. On ne la cherche donc pas dans la liste.
        pass

def addAdverb():
    '''
    addAdverb()

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

    lwAdverb = input(f'Veuillez saisir l\'adverbe que vous souhaitez ajouter. Nous supposons que vous tapez un adverbe qui existe vraiment :\n') #Chaîne de caractères représentant l'adverbe à ajouter
    lbIsValidString = True #Booléen permettant de savoir si une chaîne de caractères est valide.

    if not(lwAdverb):
        print("La chaîne est vide. Veuillez saisir des caractères pour pouvoir les ajouter au dictionnaire.")
        lbIsValidString = False
        return
    else:
        print(f'La chaîne n\'est pas vide. Vérification de la validité de la chaîne...')

    #Vérifier que la chaîne tapée est valide
    for liLetter in lwAdverb:
        if liLetter.isupper():
            print(f'Une majuscule est présente dans la chaîne. Un adverbe ne doit contenir aucune majuscule.')
            lbIsValidString = False
            break
        else:
            #La chaîne reste valide.
            pass

        if not(liLetter.isalpha()):
            print(f'Un adverbe ne peut contenir que des lettres minuscules. Vérifier par exemple qu\'elle ne contient pas de chiffres ou d\'espaces.')
            lbIsValidString = False
            break
        else:
            #La chaîne reste valide.
            pass

    if lbIsValidString:
        lwAdverb = lwAdverb.strip() #Enlever les espaces inutiles
        if lwAdverb not in gvAdverbs:
            gvAdverbs.append(lwAdverb)
            print(f'"{lwAdverb}" ajouté dans les adverbes.')
        else:
            print(f'L\'adverbe "{lwAdverb}" est déjà dans le dictionnaire. Inutile de l\'ajouter.')
    else:
        #La chaîne n'est pas valide. On ne la cherche donc pas dans la liste.
        pass

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
