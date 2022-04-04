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
        sep = '\n'
        )

        try:
            choix = int(input("Veuillez choisir un nombre entre 0 et 5 : "))
            print(f'\n##### Choix {choix} #####')

        except ValueError:
            print(f'\nERREUR : la saisie n\'est pas un nombre.\n')

        else:
            if choix < 0 or choix > 5:
                print(f'\nERREUR : Nombre hors portée.\n')

        if choix == 1:
            dico.print_dictionary()

        if choix == 2:
            phrase = sentence.Sentence()
            phrase.generate_random_sentence()
            print(f'\nLa phrase générée est la suivante :')
            phrase.print_sentence()

        if choix == 3:
            phrase = input("Veuillez tapez une phrase : ")

            if(sentence.Sentence.check_is_in_dico(phrase)):
                print(f'La phrase est bien valide.')
            else:
                print(f'La phrase n\'est pas valide.')

    print(f'\nMerci d\'avoir utilisé ce dictionnaire! Au revoir!')

if __name__ == "__main__":
    main()
