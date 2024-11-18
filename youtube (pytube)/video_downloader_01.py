'''
    Este exemplo lista os formatos de vídeo e áudio a partir de uma URL do
    Youtube e permite que se efetue o download de uma das opções listadas

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
        # Lista todos os formatos disponíveis
        videos = yt.streams.all()
    except:
        sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
    else:
        # Indexa os formatos em uma lista
        print('\nLista de Vídeos Disponíveis:\n')
        lista_videos = list(enumerate(videos))
        # Exibe os formatos disponíveis
        for video in lista_videos: print(video)
        # Solicita qual o formato a ser baixado
        opcao_download = int(input('\nInforme a Opção para baixar o formato desejado: ')) 
        try:
            # Efetua o download do vídeo
            video_download = videos[opcao_download]
            video_download.download(output_path=DIR_APP)
        except:
            sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
        else:
            print(f'\nDownload do vídeo {video_download.title} efetuado com sucesso...\n')