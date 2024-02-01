
import click
from traitement_requete import preprocess_text, filter_documents, linear_ranking, generate_results_json
import json

@click.command()
@click.option('--query', default='le président de la France', help='Input str containing the query.')
def main(query):
    # Charger les données
    with open('documents.json', 'r') as f:
        documents = json.load(f)

    with open('title_pos_index.json', 'r') as f:
        title_index = json.load(f)

    with open('content_pos_index.json', 'r') as f:
        content_index = json.load(f)

    # Prétraiter la requête
    query_tokens = preprocess_text(query)

    # Filtrer les documents
    matching_docs = filter_documents(query_tokens, title_index, content_index)

    # Appliquer le ranking linéaire
    sorted_documents = linear_ranking(matching_docs, query_tokens, title_index, content_index)

    # Générer le fichier results.json
    generate_results_json(sorted_documents, documents)

if __name__ == '__main__':
    main()
