import requests

url = 'https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PLYDOLbV7ebXh1s59hNZSsa6nBcTl6P2r5&key=AIzaSyCkptmwWABYDIFQhwDVK6_L85Bbpfb9SQ0'

resposta = requests.get(url).json()

#chaves = resposta.keys()
#dict_keys(['kind', 'etag', 'pageInfo', 'items'])

itens = resposta['items']

for i in itens: 
   print(i['snippet']['publishedAt'])
   print(i['snippet']['title'])
   print(i['snippet']['resourceId']['videoId'])
   print('')