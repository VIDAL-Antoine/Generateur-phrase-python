### Générateur de Phrase ###
## VIDAL Antoine ##

# Installation et exécution #

Il s'agit d'un générateur de phrases sous Python. Pour l'exécuter, il faut avoir Python 3 installé et supporter l'UTF8. Il suffit ensuite de lancer la commande `python3 main.py`.

# Format des fichiers #
Le générateur se base sur un dictionnaire. Le dictionnaire se trouve dans le dossier `words`. Un fichier .txt représente une fonction grammaticale. Sans ces fichiers .txt le programme ne peut pas démarrer.
Dans ces fichiers une ligne représente un mot (ou un groupe de mot), il n'y a pas de limite de mots.

# Format des mots et d'une phrase #
Le dictionnaire doit respecter les contraintes suivantes :
- un mot ne peut contenir que des lettres minuscules (sauf pour la première lettre du sujet). Les chiffres ne sont pas inclus (puisqu'une phrase simple n'est pas censée en inclure).
- le verbe et l'adverbe ne sont composés que d'un seul mot. Ainsi ils ne peuvent pas avoir d'espaces.
- le sujet doit commencer par une majuscule étant donné qu'il représente le début de la phrase. Il est la seule fonction grammaticale pouvant supporter des espaces. Ceci permet donc d'insérer par exemple des adjectifs.

Une phrase doit respecter les contraintes suivantes :
- une phrase commence par une majuscule (ici le début de la phrase est toujours le sujet).
- une phrase se termine par un point.
- une phrase contient un sujet, un verbe et peut contenir un adverbe.

# Fonctionnalités #

Le programme permet de faire les choses suivantes :

- Afficher le dictionnaire (en se basant sur les fichiers .txt)
- Générer une phrase aléatoire
- Entrer une phrase et vérifier si elle est correcte
- Ajouter un mot au dictionnaire
- Retirer un mot au dictionnaire
- Enregistrer les modifications faites au dictionnaire (pour pouvoir le réutiliser plus tard)

/!\ Les modifications faites ne sont pas enregistrées automatiquement. Vérifier que vous utilisez bien  l'option d'enregistrement avant de quitter. /!\


# Exemples de mots et phrases valides #

- Sujets valides : "Monsieur", "L'ISTY", "Le joueur", "Un grand homme"
- Verbes valides : "mange", "boit", "joue"
- Adverbes valides : "souvent", "rapidement" "lentement"

Voici donc quelques phrases valides :
"Monsieur mange souvent."
"Le joueur boit."
"Un grand homme joue lentement."