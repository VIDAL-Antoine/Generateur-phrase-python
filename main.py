# -*- coding: utf-8 -*-

import sentence
import dico

def getUserChoice(pnUpperBound : int):
    '''
    getUserChoice()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
    Cette fonction demande à l'utilisateur un entier représentant l'action qu'il souhaite effectuer.
    La fonction réalise différents tests pour s'assurer que la saisie est bien correcte.
    Elle vérifie que la saisie est bien un nombre et que celui-ci se situe dans les bornes appropriées.

    Entrées :
        pnUpperBound : l'entier maximal représentant la dernière action possible (vaut 5 par exemple s'il y a 5 actions possibles).

    Sorties :
        lEChoice : entier représentant l'action souhaitée.
    '''

    lEChoice = -1
    try:
        lEChoice = int(input("Veuillez choisir un nombre entre 0 et 5 : "))

    except ValueError:
        print(f'\nERREUR : la saisie n\'est pas un nombre.')

    else:
        if lEChoice < 0 or lEChoice > pnUpperBound:
            print(f'\nERREUR : Nombre hors portée.')

    return lEChoice

def main():
    '''
    main()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
    La fonction principale du programme. L'utilisateur doit saisir un nombre représentant son action désirée.
    Pour quitter, l'utilisateur doit saisir 0.

    Entrées :
        -

    Sorties :
        -
    '''

    lEChoice = -1 #Représente l'option choisie par l'utilisateur, réinitialisée à -1 après qu'une option soit effectuée

    print(f'Ouverture du dictionnaire...')
    dico.openDictionary()
    print(f'Ouverture terminée.')

    while(lEChoice != 0):
        lEChoice = -1

        print("\nBienvenue dans le générateur de phrases. Voici la liste des options disponibles :\n",
        "0 - Quitter",
        "1 - Afficher le dictionnaire",
        "2 - Générer une phrase automatique",
        "3 - Entrer une phrase et vérifier si elle est correcte",
        "4 - Ajouter un mot au dictionnaire",
        "5 - Retirer un mot au dictionnaire",
        "6 - Enregistrer les modifications faites au dictionnaire",
        sep = '\n'
        )

        #Vérifier que la saisie est bien un chiffre représentant une action possible
        lEChoice = getUserChoice(6)

        #Effectuer le lEChoice de l'utilisateur
        if lEChoice == 1:
            dico.printDictionary()

        elif lEChoice == 2:
            lsSentenceRandom = sentence.Sentence() #phrase créée pour générer une phrase aléatoire
            lsSentenceRandom.generateRandomSentence()
            print(f'\nLa phrase générée est la suivante :')
            lsSentenceRandom.printSentence()

        elif lEChoice == 3:
            lwPhraseCheck = input("\nVeuillez saisir une phrase :\n") #phrase créée pour vérifier sa validité
            if not(lwPhraseCheck):
                print("La phrase est vide. Veuillez saisir une phrase pour pouvoir la vérifier.")
            else:
                if(sentence.Sentence.checkIsInDictionary(lwPhraseCheck)):
                    print(f'La phrase est bien valide.')
                else:
                    print(f'La phrase n\'est pas valide.')

        elif lEChoice == 4:
            while(lEChoice != 0):
                lEChoice = -1

                print("\nSouhaitez-vous ajouter un sujet, un verbe ou un adverbe?\n",
                "0 - Annuler",
                "1 - Ajouter un sujet",
                "2 - Ajouter un verbe",
                "3 - Ajouter un adverbe",
                sep = '\n'
                )

                #Vérifier que la saisie est bien un chiffre représentant une action possible
                lEChoice = getUserChoice(3)

                if lEChoice == 0:
                    lEChoice = -1
                    break

                #Ajouter dans la liste adéquate
                if lEChoice == 1:
                    print(f'Sujets : {dico.gvSubjects}\n')
                    dico.addSubject()

                elif lEChoice == 2:
                    print(f'Verbes : {dico.gvVerbs}\n')
                    dico.addVerb()

                elif lEChoice == 3:
                    print(f'Adverbes : {dico.gvAdverbs}\n')
                    dico.addAdverb()

                else:
                    #L'utilisateur a tapé une option non reconnue
                    pass

        elif lEChoice == 5:
            while(lEChoice != 0):
                lEChoice = -1

                print("\nSouhaitez-vous retirer un sujet, un verbe ou un adverbe?\n",
                "0 - Annuler",
                "1 - Retirer un sujet",
                "2 - Retirer un verbe",
                "3 - Retirer un adverbe",
                sep = '\n'
                )

                #Vérifier que la saisie est bien un chiffre représentant une action possible
                lEChoice = getUserChoice(3)

                if lEChoice == 0:
                    lEChoice = -1
                    break

                #Retirer de la liste adéquate
                elif lEChoice == 1:
                    print(f'\nSujets : {dico.gvSubjects}\n')
                    dico.removeItem(dico.gvSubjects)

                elif lEChoice == 2:
                    print(f'\nVerbes : {dico.gvVerbs}\n')
                    dico.removeItem(dico.gvVerbs)

                elif lEChoice == 3:
                    print(f'\nAdverbes : {dico.gvAdverbs}\n')
                    dico.removeItem(dico.gvAdverbs)

                else:
                    #L'utilisateur a tapé une option non reconnue
                    pass

        elif lEChoice == 6:
            dico.saveDictionary()
            print(f'Les modifications ont été enregistrées.')

        else:
            #L'utilisateur a tapé une option non reconnue
            pass

    print(f'\nMerci d\'avoir utilisé ce dictionnaire! Au revoir!')

if __name__ == "__main__":
    main()
