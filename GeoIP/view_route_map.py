from geopy.geocoders import Nominatim
import webbrowser, os

# Obtendo o diretório corrente
diretorio_atual = os.path.dirname(os.path.realpath(__file__))

# Criando o objeto - OpenStreetMap
geolocator = Nominatim(user_agent = 'exemplo_geolocalizacao')

# Entrada das Localidades
origem  = 'Natal'
destino = 'Minas Gerais'

# Obtem a Localização a partir das Localidades informadas
local_origem  = geolocator.geocode(origem)
local_destino = geolocator.geocode(destino)

# Obtendo Latitude e Longitude 
latitude_origem, longitude_origem   = (local_origem.latitude), (local_origem.longitude) 
latitude_destino, longitude_destino = (local_destino.latitude), (local_destino.longitude)  

# URL base
google_api_key = 'YOUR_API_KEY'
url_mapa  = f'https://www.google.com/maps/embed/v1/directions?key={google_api_key}&'
url_mapa += f'origin={latitude_origem},{longitude_origem}&'
url_mapa += f'destination={latitude_destino},{longitude_destino}'

# HTML base
html_base  = f'<html>\n<head>\n\t<title>Exemplo de Mapas - Google Maps</title>\n</head>\n'
html_base += f'<body>\n\t<iframe width=\"100%\" height=\"100%\" frameborder=\"0\" style=\"border:0\"'
html_base += f'src=\"{url_mapa}\"</iframe>\n</body>\n</html>'

# Gerando HTML
nome_arquivo = diretorio_atual + '\exemplo_mapa_rota_gerado.html'
arquivo = open(nome_arquivo, 'w')
arquivo.write(html_base)
arquivo.close()

# Abrindo o Arquivo HTML gerado
browser = webbrowser.get('windows-default')
browser.open(nome_arquivo)