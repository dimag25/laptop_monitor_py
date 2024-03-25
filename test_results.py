from opensearchpy import OpenSearch

from monitoring import SERVICES

# Connect to OpenSearch
opensearch = OpenSearch([{'host': 'localhost', 'port': 9200}])

# Define your search query
search_query = {
    "query": {
        "match_all": {}
    }
}

for hit in opensearch.search(index='laptop_performance', body=search_query)['hits']['hits']:
    print('[laptop_performance]:', hit['_source'])

for service in SERVICES:
    for hit in opensearch.search(index=service, body=search_query)['hits']['hits']:
        print(f'[{service}]:', hit['_source'])
