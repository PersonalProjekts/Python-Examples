import requests

api_key = 'YOUR_API_KEY_HERE'
playlist_url = 'https://youtube.googleapis.com/youtube/v3/playlists?part=snippet&channelId=UCmEClzCBDx-vrt0GuSKBd9g&key=AIzaSyCkptmwWABYDIFQhwDVK6_L85Bbpfb9SQ0'
#playlist_url = 'https://www.googleapis.com/youtube/v3/playlists'

# Primeira requisição para obter as primeiras playlists
params = {
    'part': 'snippet',
    'maxResults': 5,  # Número padrão de resultados por página
    'key': api_key
}

response = requests.get(playlist_url, params=params)
data = response.json()

# Processar os resultados da primeira página
#for playlist in data['items']:
#    print(playlist['snippet']['title'])

# Obter o token da próxima página
next_page_token = data.get('nextPageToken')

# Fazer requisições adicionais para obter mais playlists
while next_page_token:
    print(next_page_token)
    params['pageToken'] = next_page_token
    response = requests.get(playlist_url, params=params)
    data = response.json()

    # Processar os resultados da página atual
#    for playlist in data['items']:
#        print(playlist['snippet']['title'])

    # Obter o token da próxima página ou sair do loop se não houver mais páginas
    next_page_token = data.get('nextPageToken', None)
