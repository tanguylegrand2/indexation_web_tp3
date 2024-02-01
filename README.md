# Projet de Filtrage et Ranking de Pages Web

## Auteur
- Contributeur: Tanguy Legrand

## Description
Ce projet implémente un système de filtrage et de ranking de pages web en fonction d'une requête donnée. Le filtrage est effectué à l'aide d'un index de pages web, et le ranking est réalisé en fonction de la pertinence des résultats par rapport à la requête.

## Fonctionnalités Principales

1. **Pretraitement du Texte**
   - La fonction `preprocess_text(text)` est utilisée pour le prétraitement du texte, notamment la tokenization et la conversion en minuscules.

2. **Filtrage des Documents**
   - La fonction `filter_documents(query_tokens, title_index, content_index)` filtre les documents en fonction des tokens de la requête. Elle utilise un index de titres et de contenus pour identifier les pages web pertinentes.

3. **Ranking Linéaire**
   - La fonction `linear_ranking(documents, query_tokens, title_index, content_index)` attribue des scores aux documents en fonction de la présence des tokens dans les titres et le contenu. Le ranking final est effectué en combinant ces scores de manière linéaire.

4. **Génération des Résultats en JSON**
   - La fonction `generate_results_json(sorted_documents, documents)` crée un fichier JSON (`results.json`) contenant des informations sur les documents qui ont survécu au filtre et les présente dans un ordre de pertinence décroissante.

## Configuration et Prérequis

1. **Fichiers de Données**
   - Assurez-vous d'avoir les fichiers suivants dans le répertoire du projet:
     - `documents.json` : Contient les informations sur les pages web.
     - `title_pos_index.json` : Index des positions des mots-clés dans les titres des pages web.
     - `content_pos_index.json` : Index des positions des mots-clés dans le contenu des pages web.

2. **Dépendances Python**
   - Les dépendances nécessaires sont spécifiées dans le fichier `requirements.txt`. Vous pouvez les installer en utilisant la commande suivante:
     ```bash
     pip install -r requirements.txt
     ```

## Utilisation du Code

1. **Lancer le Programme**
   - Exécutez le fichier `main.py` en utilisant la commande:
     ```bash
     python main.py --query "votre requête ici"
     ```
   - La requête est optionnelle, et si elle n'est pas fournie, la valeur par défaut est "le président de la France".

2. **Résultats**
   - Le programme générera un fichier `results.json` contenant les résultats de la requête.

## Organisation du Projet et des Fichiers

- Le projet est divisé en deux fichiers principaux:
  1. `traitement_requete.py` : Contient les fonctions liées au prétraitement, au filtrage et au ranking.
  2. `main.py` : Fichier principal pour l'exécution du programme.

- Fichiers de Données:
  - `documents.json` : Contient les informations sur les pages web.
  - `title_pos_index.json` : Index des positions des mots-clés dans les titres des pages web.
  - `content_pos_index.json` : Index des positions des mots-clés dans le contenu des pages web.

## Remarque
Ce README assume que le projet est utilisé dans un environnement Python standard, et que les fichiers de données nécessaires sont présents dans le même répertoire que les scripts.

Merci de contacter Tanguy Legrand pour toute question ou contribution supplémentaire.
