# -*- coding: utf-8 -*-

import sentence
import dico

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

    lnChoice = -1 #Représente l'option choisie l'utilisateur, réinitialisée à -1 après qu'une option soit effectuée

    print(f'Ouverture du dictionnaire...')
    dico.openDictionary()
    print(f'Ouverture terminée.')

    while(lnChoice != 0):
        lnChoice = -1

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
        try:
            lnChoice = int(input("Veuillez choisir un nombre entre 0 et 5 : "))

        except ValueError:
            print(f'\nERREUR : la saisie n\'est pas un nombre.')

        else:
            if lnChoice < 0 or lnChoice > 6:
                print(f'\nERREUR : Nombre hors portée.')

        #Effectuer le lnChoice de l'utilisateur
        if lnChoice == 1:
            dico.printDictionary()

        elif lnChoice == 2:
            lsSentenceRandom = sentence.Sentence() #phrase créée pour générer une phrase aléatoire
            lsSentenceRandom.generateRandomSentence()
            print(f'\nLa phrase générée est la suivante :')
            lsSentenceRandom.printSentence()

        elif lnChoice == 3:
            lwPhraseCheck = input("Veuillez saisir une phrase :\n") #phrase créée pour vérifier sa validité

            if(sentence.Sentence.checkIsInDictionary(lwPhraseCheck)):
                print(f'La phrase est bien valide.')
            else:
                print(f'La phrase n\'est pas valide.')

        elif lnChoice == 4:
            while(lnChoice != 0):
                lnChoice = -1

                print("\nSouhaitez-vous ajouter un sujet, un verbe ou un adverbe?\n",
                "0 - Annuler",
                "1 - Ajouter un sujet",
                "2 - Ajouter un verbe",
                "3 - Ajouter un adverbe",
                sep = '\n'
                )

                #Vérifier que la saisie est bien un chiffre représentant une action possible
                try:
                    lnChoice = int(input("Veuillez choisir un nombre entre 0 et 3 : "))

                except ValueError:
                    print(f'\nERREUR : la saisie n\'est pas un nombre.\n')

                else:
                    if lnChoice < 0 or lnChoice > 3:
                        print(f'\nERREUR : Nombre hors portée.\n')

                if lnChoice == 0:
                    lnChoice = -1
                    break

                #Ajouter dans la liste adéquate
                elif lnChoice == 1:
                    print(f'Sujets : {dico.gvSubjects}\n')
                    dico.addSubject()

                elif lnChoice == 2:
                    print(f'Verbes : {dico.gvVerbs}\n')
                    dico.addVerb()

                elif lnChoice == 3:
                    print(f'Adverbes : {dico.gvAdverbs}\n')
                    dico.addAdverb()

                else:
                    #L'utilisateur a tapé une option non reconnue
                    pass

        elif lnChoice == 5:
            while(lnChoice != 0):
                lnChoice = -1

                print("\nSouhaitez-vous retirer un sujet, un verbe ou un adverbe?\n",
                "0 - Annuler",
                "1 - Retirer un sujet",
                "2 - Retirer un verbe",
                "3 - Retirer un adverbe",
                sep = '\n'
                )

                #Vérifier que la saisie est bien un chiffre représentant une action possible
                try:
                    lnChoice = int(input("Veuillez choisir un nombre entre 0 et 3 : "))

                except ValueError:
                    print(f'\nERREUR : la saisie n\'est pas un nombre.\n')

                else:
                    if lnChoice < 0 or lnChoice > 3:
                        print(f'\nERREUR : Nombre hors portée.\n')

                if lnChoice == 0:
                    lnChoice = -1
                    break

                #Retirer de la liste adéquate
                elif lnChoice == 1:
                    print(f'Sujets : {dico.gvSubjects}\n')
                    dico.removeItem(dico.gvSubjects)

                elif lnChoice == 2:
                    print(f'Verbes : {dico.gvVerbs}\n')
                    dico.removeItem(dico.gvVerbs)

                elif lnChoice == 3:
                    print(f'Adverbes : {dico.gvAdverbs}\n')
                    dico.removeItem(dico.gvAdverbs)

                else:
                    #L'utilisateur a tapé une option non reconnue
                    pass

        elif lnChoice == 6:
            dico.saveDictionary()
            print(f'Les modifications ont été enregistrées.')

        else:
            #L'utilisateur a tapé une option non reconnue
            pass

    print(f'\nMerci d\'avoir utilisé ce dictionnaire! Au revoir!')

if __name__ == "__main__":
    main()
