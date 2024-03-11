import requests, sys
from youtube_constantes import *
from urllib import parse

# ------------------------------------------------------------------------------------------
# Variável contendo o TOKEN a ser utilizado nas requisições
strTOKEN = f'&key={API_TOKEN}' if API_TOKEN else ''


# ------------------------------------------------------------------------------------------
tuplaHeaders = ('scheme','netloc','path','params','query','fragment')


# ------------------------------------------------------------------------------------------
# Obter o Channel ID quando for informado o @nome_canal
def getChannelID(channel_name: str):
   boolSucesso  = False
   strRetorno   = None
   strErro      = None
    
   dictParametros = {'part': 'snippet', 'q': channel_name, 'type': 'channel', 'key': API_TOKEN}

   try:
      response = requests.get(URL_BASE_SEARCH, params=dictParametros)
   except:
      strErro = f'{MSG_ERRO}{sys.exc_info()[0]} ... (Linha: 31)\n'
   else:
      if response.status_code != 200:
         strErro = f'{MSG_ERRO}Erro ao Fazer a Solicitação:\n{response.status_code} - {response.text}\n'
      else:
         data = response.json()
         if len(data['items']) == 0:
            strErro = f'{MSG_ERRO}Canal Não Encontrado...\n'
         else:
            strRetorno  = data['items'][0]['id']['channelId']
            boolSucesso = True
   finally:
      return boolSucesso, strRetorno, strErro


# ------------------------------------------------------------------------------------------
# Retorna dados das playlists de um determinado canal
def getPlaylists(urlChannel: str, debug: bool):
   boolSucesso      = False
   lstRetorno       = None
   strErro          = None
   
   # Decompondo a URL
   strURLAnalisada = parse.urlparse(urlChannel)
   if debug: print(f'\n{MSG_DEBUG}URL Decomposta\n{strURLAnalisada}')

   # Montando Dicionário com resultado da URL analisada  
   dictParametros = dict(zip(tuplaHeaders, strURLAnalisada))
   if debug: print(f'\n{MSG_DEBUG}Dados para Requisição\n{dictParametros}')

   # Montando URL de requisição - Playlists do Canal
   strChannelID     = dictParametros['path'].replace('/channel/','')
   strURLReqChannel = f'{URL_BASE_CHANNEL}&channelId={strChannelID}{strTOKEN}'
   if debug: print(f'\n{MSG_DEBUG}URL da Requisição\n{strURLReqChannel}\n')

   contador = 1
   while True:
      try:
         # Requisição de metadados do canal
         print(PARAMS_REQUEST)
         channelMetaData = requests.get(strURLReqChannel, params=PARAMS_REQUEST).json()
      except:
         strErro = f'{MSG_ERRO}{sys.exc_info()[0]} ... (Linha: 66)\n'
      else:
         # Se não existe a chave 'pageToken' em PARAMS_REQUESTS, adiciona
         #if 'pageToken' not in PARAMS_REQUEST.keys():
         strNextPageToken = channelMetaData.get('nextPageToken')
         print(contador, ' - ', strNextPageToken)
         PARAMS_REQUEST['nextPageToken'] = strNextPageToken

         if not channelMetaData.get('nextPageToken'): break
         
         try:
            # Montando lista de URLs das playlists do Canal
            lstRetorno = list()
            for i in channelMetaData['items']:
               lstRetorno.append((i['snippet']['title'], i['id']))
         except:
            strErro = f'{MSG_ERRO}{sys.exc_info()[0]} ... (Linha: 74)\n'
            boolSucesso = False
         else:
            contador += 1
            boolSucesso = True
   
   return boolSucesso, lstRetorno, strErro


# ------------------------------------------------------------------------------------------
# Retorna os dados dos vídeos de uma determinada playlist
def getVideos(urlPlaylist: str, debug: bool):
   boolSucesso  = False
   lstRetorno   = None
   strErro      = None
   try:
      # Requisição de metadados da playlist
      playlistMetaData = requests.get(urlPlaylist).json()
   except:
      strErro = f'{MSG_ERRO}{sys.exc_info()[0]} ... (Linha: 91)\n'
   else:
      try:
         # Montando lista de URLs das playlists do Canal
         lstRetorno = list()
         for i in playlistMetaData['items']:
            lstRetorno.append((i['snippet']['title'], i['snippet']['publishedAt'], i['snippet']['resourceId']['videoId']))
      except:
         strErro = f'{MSG_ERRO}{sys.exc_info()[0]} ... (Linha: 99)\n'
      else:
         boolSucesso = True
   finally:
      return boolSucesso, lstRetorno, strErro
