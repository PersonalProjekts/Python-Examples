# https://developers.google.com/youtube/v3/getting-started?hl=pt
# https://developers.google.com/youtube/v3/docs

#TODO: Obter os vídeos que não estão nas playlists
#TODO: Retirar a limitação de 5 playlists por página ("resultsPerPage": 5)
#TODO: Efetuar download dos vídeos
 
import os, sys
import youtube_lib
from youtube_constantes import *

# ------------------------------------------------------------------------------------------
# Limpando a Tela
os.system(COMANDOS['limpa_tela'][SO])

# ------------------------------------------------------------------------------------------
# URL do canal a ser pesquisado 
#strURL = 'https://www.youtube.com/channel/UCyDZDwafway1JnpdQtTJpMQ'
#strURL = 'https://www.youtube.com/@TVGuruPapaJerimum'
strURL = 'https://www.youtube.com/@JovemNerd'
#strURL = input('Informe a URL do Canal: ')

strChannel = strURL.rsplit('/',1)[1]
if strChannel[0] == '@':
   strChannelID = youtube_lib.getChannelID(strChannel)
   if not strChannelID[0]:
      print(strChannelID[2])
      sys.exit()
   strURL = f'https://www.youtube.com/channel/{strChannelID[1]}'

print(f'{COR_AVISO}\n{"-" * 140}\nCanal:\n{COR_PADRAO}{strURL}\n')

# ------------------------------------------------------------------------------------------
# Obtendo dados das Playlists do Canal
playlists = youtube_lib.getPlaylists(strURL, DEBUG)

# Se houve erro, exibe-o e sai do programa
if not playlists[0]:
   print(playlists[2])
   sys.exit()


# ------------------------------------------------------------------------------------------
# Montando URL de requisição - URLs Playlists do Canal
print(f'{COR_AVISO}\n{"-" * 140}\nResultado da Requisição - URLs das Playlists do Canal{COR_PADRAO}')

lstPlaylists = list()
strTOKEN = f'&key={API_TOKEN}' if API_TOKEN else ''
for i in playlists[1]:
   lstPlaylists.append((i[0], f'{URL_BASE_PLAYLIST}&playlistId={i[1]}{strTOKEN}'))

for playlist in lstPlaylists: print(playlist,'\n')

sys.exit()

# ------------------------------------------------------------------------------------------
# Montando URL de requisição - URLs Videos das Playlists
print(f'{COR_AVISO}\n{"-" * 140}\nResultado da Requisição - URLs dos Vídeos das Playlists do Canal{COR_PADRAO}')

# Obtendo dados dos Vídeos das Playlists
lstVideos = list()
for i in lstPlaylists:
   videos = youtube_lib.getVideos(i[1], DEBUG)
   if videos[0]:
      for v in videos[1]:
         lstVideos.append((v[0], v[1], f'{URL_BASE_VIDEO}{v[2]}'))

for video in lstVideos: print(video,'\n')