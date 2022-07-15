import moviepy.editor
import os

# Obtendo o diretório corrente
diretorio_atual = os.path.realpath(__file__)
diretorio_atual = os.path.dirname(diretorio_atual)

# Carregando o arquivo de vídeo
video = moviepy.editor.VideoFileClip(diretorio_atual + '\\crazy_frog_axel_f_official_video.mp4')

# Extraindo o audio
audio_data = video.audio

# Salvando o audio extraído 
audio_data.write_audiofile(diretorio_atual + '\\saida.mp3', )