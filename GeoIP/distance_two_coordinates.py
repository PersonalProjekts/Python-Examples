from geopy.geocoders import Nominatim
from geopy import distance

# Criando o objeto - OpenStreetMap
geolocator = Nominatim(user_agent = 'exemplo_geolocalizacao')

# Entrada das Localidades
origem  = input('\nInforme o endereço: ')
destino = input('Informe o endereço: ')

# Obtem a Localização a partir das Localidades informadas
local_origem  = geolocator.geocode(origem)
local_destino = geolocator.geocode(destino)

# Exibindo os dados da origem
print(f'\n\nORIGEM .....: {local_origem}')
print(f'COORDENADAS : {local_origem.point}')
print(f'COORDENADAS : {(local_origem.latitude, local_origem.longitude)}\n\n')

# Exibindo os dados do destino
print(f'DESTINO.....: {local_destino}')
print(f'COORDENADAS : {local_destino.point}')
print(f'COORDENADAS : {(local_destino.latitude, local_destino.longitude)}\n\n')

# Obtendo Latitude e Longitude 
latitude_origem, longitude_origem   = (local_origem.latitude), (local_origem.longitude) 
latitude_destino, longitude_destino = (local_destino.latitude), (local_destino.longitude) 

# Montando a TUPLA (latitude, longitude)
localizacao_origem  = (latitude_origem, longitude_origem)
localizacao_destino = (latitude_destino, longitude_destino)

# Calculando a Distância utilizando a TUPLA (origem, destino)
distancia_1 = distance.distance(localizacao_origem, localizacao_destino).kilometers

# Calculando a Distância utilizando a TUPLA (point, point)
distancia_2 = distance.distance(local_origem.point, local_destino.point).km

# Exibindo as Distâncias calculadas
print(f'A Distância entre {origem} e {destino} é de {distancia_1:.2f} Kilometros (usando (latitude, longitude))')
print(f'A Distância entre {origem} e {destino} é de {distancia_2:.2f} Kilometros (usando as Coordenadas -> .point)\n\n')