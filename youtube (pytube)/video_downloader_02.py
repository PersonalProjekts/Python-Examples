'''
    Este exemplo efetua o download do vídeo com a maior resolução a partir
    de uma URL do Youtube

    Necessário instalar a biblioteca PYTUBE
        pip install pytube

    Documentação
        https://pytube.io/en/latest/
'''

import os, sys
from pytube import YouTube

# Definindo o diretório de salvamento
DIR_APP = os.path.dirname(os.path.realpath(__file__))

# Solicitando a URL do vídeo
url_video = input('\nInforme a URL do vídeo: ')

try:
    # Criando o objeto 
    yt = YouTube(url_video)
except:
    sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
else:
    try:
        # Obtem o vídeo de maior resolução
        video_download = yt.streams.get_highest_resolution()
    except:
        sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
    else:
        try:
            # Efetua o download do vídeo
            print(f'\nBaixando: {url_video}\n')
            video_download.download(output_path=DIR_APP)
        except:
            sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
        else:
            print(f'\nDownload do vídeo {video_download.title} efetuado com sucesso...\n')