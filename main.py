# -*- coding: utf-8 -*-

import sentence
import dico

def main():
    dico.open_dictionary()
    
    choix = -1

    while(choix != 0):
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

        try:
            choix = int(input("Veuillez choisir un nombre entre 0 et 5 : "))
            print(f'\n##### Choix {choix} #####')

        except ValueError:
            print(f'\nERREUR : la saisie n\'est pas un nombre.\n')

        else:
            if choix < 0 or choix > 6:
                print(f'\nERREUR : Nombre hors portée.\n')

        if choix == 1:
            dico.print_dictionary()

        elif choix == 2:
            phrase = sentence.Sentence()
            phrase.generate_random_sentence()
            print(f'\nLa phrase générée est la suivante :')
            phrase.print_sentence()

        elif choix == 3:
            phrase = input("Veuillez tapez une phrase : ")

            if(sentence.Sentence.check_is_in_dico(phrase)):
                print(f'La phrase est bien valide.')
            else:
                print(f'La phrase n\'est pas valide.')

        elif choix == 4:
            while(choix != 0):
                print("\nSouhaitez-vous ajouter un sujet, un verbe ou un adverbe?\n",
                "0 - Annuler",
                "1 - Ajouter un sujet",
                "2 - Ajouter un verbe",
                "3 - Ajouter un adverbe",
                sep = '\n'
                )

                try:
                    choix = int(input("Veuillez choisir un nombre entre 0 et 3 : "))
                    print(f'\n##### Choix {choix} #####')

                except ValueError:
                    print(f'\nERREUR : la saisie n\'est pas un nombre.\n')

                else:
                    if choix < 0 or choix > 3:
                        print(f'\nERREUR : Nombre hors portée.\n')

                if choix == 0:
                    choix = -1
                    break

                elif choix == 1:
                    print(f'Sujets : {dico.subjects}\n')
                    dico.add_subject()

                elif choix == 2:
                    print(f'Verbes : {dico.verbs}\n')
                    dico.add_verb()

                elif choix == 3:
                    print(f'Adverbes : {dico.adverbs}\n')
                    dico.add_adverb()

        elif choix == 5:
            while(choix != 0):
                print("\nSouhaitez-vous retirer un sujet, un verbe ou un adverbe?\n",
                "0 - Annuler",
                "1 - Retirer un sujet",
                "2 - Retirer un verbe",
                "3 - Retirer un adverbe",
                sep = '\n'
                )

                try:
                    choix = int(input("Veuillez choisir un nombre entre 0 et 3 : "))
                    print(f'\n##### Choix {choix} #####')

                except ValueError:
                    print(f'\nERREUR : la saisie n\'est pas un nombre.\n')

                else:
                    if choix < 0 or choix > 3:
                        print(f'\nERREUR : Nombre hors portée.\n')

                if choix == 0:
                    choix = -1
                    break

                elif choix == 1:
                    print(f'Sujets : {dico.subjects}\n')
                    dico.remove_item(dico.subjects)

                elif choix == 2:
                    print(f'Verbes : {dico.verbs}\n')
                    dico.remove_item(dico.verbs)

                elif choix == 3:
                    print(f'Adverbes : {dico.adverbs}\n')
                    dico.remove_item(dico.adverbs)

        elif choix == 6:
            dico.save_dico()
            print(f'Les modifications ont été enregistrées.')

    print(f'\nMerci d\'avoir utilisé ce dictionnaire! Au revoir!')

if __name__ == "__main__":
    main()
