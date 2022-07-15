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
        audio_download = yt.streams.filter(only_audio=True)[0]
    except:
        print('\nERRO..: ', sys.exc_info()[0])
        baixado = False
    else:
        try:
            # Efetua o download do apenas do áudio
            audio_download.download(output_path=diretorio)
            baixado = True
        except:
            print('\nERRO..: ', sys.exc_info()[0])
            baixado = False
finally:
    if baixado: 
        print('\nÁudio Baixado com Sucesso...\n')
    else:
        print('\nProblema no Download do Áudio...\n')
