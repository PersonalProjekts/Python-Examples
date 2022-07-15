import os, sys
from pytube import YouTube

# Definindo o diretório de salvamento
diretorio = os.path.dirname(os.path.realpath(__file__))

# Solicitando a URL do vídeo
url_video = input('\nInforme a URL do vídeo: ')

try:
    # Criando o objeto 
    yt = YouTube(url_video)
except:
    print('\nERRO..: ', sys.exc_info()[0])
    baixado = False
else:
    try:
        # Obtem o vídeo de maior resolução
        video_download = yt.streams.get_highest_resolution()
    except:
        print('\nERRO..: ', sys.exc_info()[0])
        baixado = False
    else:
        try:
            # Efetua o download do vídeo
            video_download.download(output_path=diretorio)
            baixado = True
        except:
            print('\nERRO..: ', sys.exc_info()[0])
finally:
    if baixado: 
        print('\nVídeo Baixado com Sucesso...\n')
    else:
        print('\nProblema no Download do Vídeo...\n')
