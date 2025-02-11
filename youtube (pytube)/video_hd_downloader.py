import os, sys
from pytube import YouTube

# Definindo o diretório de salvamento
DIR_APP = os.path.dirname(__file__)

# Solicitando a URL do vídeo
strURLVideo = input('\nInforme a URL do vídeo: ')

try:
    # Criando o objeto 
    yt = YouTube(strURLVideo)
except:
    sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
else:
    try:
        # Obtem o vídeo de maior resolução
        videoDownload = yt.streams.get_highest_resolution()
    except:
        sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
    else:
        try:
            # Efetua o download do vídeo
            print(f'\nBaixando: {strURLVideo}\n')
            videoDownload.download(output_path=DIR_APP)
        except:
            sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
        else:
            print(f'\nDownload do vídeo {videoDownload.title} efetuado com sucesso...\n')