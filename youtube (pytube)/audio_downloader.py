import os, sys
from pytube import YouTube

# Definindo o diretório de salvamento
DIR_APP = os.path.dirname(__file__)
print(DIR_APP)
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
        audioDownload = yt.streams.filter(only_audio=True)[0]
    except:
        sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
    else:
        try:
            # Efetua o download do apenas do áudio
            audioDownload.download(output_path=DIR_APP)
        except:
            sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
        else:
            print(f'\nDownload do áudio {audioDownload.title} efetuado com sucesso...\n')