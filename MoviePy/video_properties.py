import moviepy.editor
import os

# Obtendo o diretório corrente
diretorio_atual = os.path.realpath(__file__)
diretorio_atual = os.path.dirname(diretorio_atual)

# Carregando o arquivo de vídeo
video = moviepy.editor.VideoFileClip(diretorio_atual + '\\crazy_frog_axel_f_official_video.mp4')

# Exibindo as propriedades do vídeo
print(f'Resolução do vídeo..........: {video.size}')
print(f'Duração do vídeo (segundos) : {video.duration}')
print(f'FPS ........................: {video.fps}')