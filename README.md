# Générateur de Phrase #
## VIDAL Antoine ##

### Installation et exécution ###

Il s'agit d'un générateur de phrases sous Python. Pour l'exécuter, il faut avoir Python 3 installé et supporter l'UTF8. Il suffit ensuite de lancer la commande `python3 main.py`.

### Format des fichiers ###
Le générateur se base sur un dictionnaire. Le dictionnaire se trouve dans le dossier `words`. Un fichier .txt représente une fonction grammaticale. Sans ces fichiers .txt le programme ne peut pas démarrer.
Dans ces fichiers une ligne représente un mot (ou un groupe de mot), il n'y a pas de limite de mots.

### Format des mots et d'une phrase ###
Le dictionnaire doit respecter les contraintes suivantes :
- un mot ne peut contenir que des lettres minuscules (sauf pour le sujet) ou l'apostrophe "'". Les chiffres ne sont pas inclus (puisqu'une phrase simple n'est pas censée en inclure).
- le sujet doit commencer par une majuscule. Il peut également contenir d'autres majuscules (par exemple pour les sigles).
- une fonctionnalité grammaticale peut contenir autant de mots que possible. Les espaces sont ainsi gérés.
- l'existence du mot ne sera pas vérifiée. On suppose donc que les mots saisis sont corrects.

Une phrase doit respecter les contraintes suivantes :
- une phrase commence par une majuscule (ici le début de la phrase est toujours le sujet).
- une phrase se termine par un point.
- une phrase contient un (et uniquement un) sujet, un (et uniquement un) verbe et peut contenir un (et uniquement un) adverbe.

### Fonctionnalités ###
Le programme permet de faire les choses suivantes :

- Afficher le dictionnaire (en se basant sur les fichiers .txt)
- Générer une phrase aléatoire
- Entrer une phrase et vérifier si elle est correcte
- Ajouter un mot au dictionnaire
- Retirer un mot au dictionnaire
- Enregistrer les modifications faites au dictionnaire (pour pouvoir le réutiliser plus tard)

/!\ Les modifications faites ne sont pas enregistrées automatiquement. Vérifier que vous utilisez bien l'option d'enregistrement avant de quitter. /!\

### Exemples de mots et phrases valides ###
- Sujets valides : "Monsieur", "L'ISTY", Un grand homme"
- Verbes valides : "mange", "se lave", "s'assoit"
- Adverbes valides : "souvent", "n'importe ecomment" "sans conteste"

Voici donc quelques phrases valides :
"Monsieur mange souvent."
"L'ISTY se lave."
"Un grand homme s'assoit n'importe comment."