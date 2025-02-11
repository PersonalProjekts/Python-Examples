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
        # Lista todos os formatos disponíveis
        lstVideos = yt.streams.all()
    except:
        sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
    else:
        # Indexa os formatos em uma lista
        print('\nLista de Vídeos Disponíveis:\n')
        lstVideos = list(enumerate(lstVideos))
        # Exibe os formatos disponíveis
        for video in lstVideos: print(video)
        # Solicita qual o formato a ser baixado
        intOpcao = int(input('\nInforme a Opção para baixar o formato desejado: ')) 
        try:
            # Efetua o download do vídeo
            videoDownload = lstVideos[intOpcao]
            videoDownload.download(output_path=DIR_APP)
        except:
            sys.exit(f'\nERRO..: {sys.exc_info()[0]}\n')
        else:
            print(f'\nDownload do vídeo {videoDownload.title} efetuado com sucesso...\n')