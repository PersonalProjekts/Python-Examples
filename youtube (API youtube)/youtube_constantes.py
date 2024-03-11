import platform

# ------------------------------------------------------------------------------------------
# Constantes Youtube
API_TOKEN         = 'AIzaSyCkptmwWABYDIFQhwDVK6_L85Bbpfb9SQ0'

URL_BASE_API      = 'https://youtube.googleapis.com/youtube/v3'

URL_BASE_CHANNEL  = f'{URL_BASE_API}/playlists?part=snippet'
URL_BASE_PLAYLIST = f'{URL_BASE_API}/playlistItems?part=snippet'
URL_BASE_VIDEO    = 'https://www.youtube.com/watch?v='
#URL_BASE_SEARCH   = "https://www.googleapis.com/youtube/v3/search"
URL_BASE_SEARCH   = f'{URL_BASE_API}/search'

PARAMS_REQUEST = {
    'part': 'snippet',
    'maxResults': 5,  # Número padrão de resultados por página
    'key': API_TOKEN,
    'nextPageToken': None
}

# ------------------------------------------------------------------------------------------
# Outras Constantes
DEBUG = False

# Definindos comandos de sistema
SO = platform.system().lower()
COMANDOS = {'limpa_tela': {'windows': 'cls', 'linux': 'clear'}
            }

# ------------------------------------------------------------------------------------------
# Definindo as constantes das cores de texto
COR_ERRO      = '\033[40;31;1m' #Vermelha
COR_ACERTO    = '\033[40;32;1m' #Verde
COR_AVISO     = '\033[40;33;1m' #Amarela
COR_PADRAO    = '\033[40;30;1m' #Branca

# Definindo templates de mensagens
MSG_ERRO   = f'{COR_ERRO}ERRO.....: {COR_PADRAO}'
MSG_AVISO  = f'{COR_AVISO}AVISO...: {COR_PADRAO}'
MSG_DEBUG  = f'{COR_AVISO}DEBUG...: {COR_PADRAO}'
