import requests

def search_papers(query, rows=5):
    url = "https://api.crossref.org/works"
    params = {
        'query': query,
        'filter': 'type:journal-article',
        'rows': rows
    }
    response = requests.get(url, params=params)
    return response.json()['message']['items']

#actual search to try
papers = search_papers("clinic AND Oncology")
for paper in papers:
    print(paper['title'][0], "-", paper['URL'])
^