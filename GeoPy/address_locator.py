from geopy.geocoders import Nominatim
from geopy import distance

# Informando o endereço desejado
endereco = input('\nInforme o endereço: ')

# Criando o objeto - OpenStreetMap
geolocator = Nominatim(user_agent="exemplo_geolocalizacao")

# Obtem os metadados a partir da localização informada
local_origem = geolocator.geocode(endereco)

# Exibindo os dados
print(f'\nORIGEM .....: {local_origem}')
print(f'\nCOORDENADAS : {local_origem.point}')
print(f'\nCOORDENADAS : {(local_origem.latitude, local_origem.longitude)}')
