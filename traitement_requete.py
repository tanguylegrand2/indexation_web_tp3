
import json



def preprocess_text(text):
    # Fonction pour le prétraitement du texte (tokenization et lowercasing)
    tokens = text.lower().split()
    return tokens


def filter_documents(query_tokens, title_index, content_index):
    # Initialiser l'ensemble de documents correspondants avec l'ensemble de tous les documents
    matching_docs = set(title_index.keys()).union(content_index.keys())

    for token in query_tokens:
        # Retirer les documents qui ne contiennent pas le token dans le titre ou dans le contenu
        matching_docs.intersection_update(
            set(title_index.get(token, {}).keys()) | set(content_index.get(token, {}).keys())
        )

    return matching_docs







def linear_ranking(documents, query_tokens, title_index, content_index):
    rankings = {}

    for doc_id in documents:
        score_title = 0
        score_content = 0

        for token in query_tokens:
            # Vérifier si le doc_id existe dans l'index de titre
            if doc_id in title_index.get(token, {}):
                score_title += title_index[token].get(doc_id, {}).get('count', 0)

            # Vérifier si le doc_id existe dans l'index de contenu
            if doc_id in content_index.get(token, {}):
                score_content += content_index[token].get(doc_id, {}).get('count', 0)

        # On peut ajuster cette formule en fonction de ce qu'on veut
        score = 0.8 * score_title + 0.2 * score_content

        rankings[doc_id] = score

    # Trier les documents par score décroissant
    sorted_documents = sorted(rankings.items(), key=lambda x: x[1], reverse=True)
    return sorted_documents




def generate_results_json(sorted_documents, documents):
    #Crée le JSON avec le résultat de la requête
    results = []

    for doc_id, score in sorted_documents:
        doc_info = {
            'Titre': documents[int(doc_id)]['title'],
            'Url': documents[int(doc_id)]['url']
        }
        results.append(doc_info)

    result_data = {
        'Nombre de documents dans l’index': len(documents),
        'Nombre de documents qui ont survécu au filtre': len(sorted_documents),
        'Documents': results
    }

    with open('results.json', 'w') as f:
        json.dump(result_data, f, indent=2)
