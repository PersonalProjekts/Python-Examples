# ------------------------------------------------------------------------------------------
# Este exemplo lista as redes WIFI disponíveis.
# ------------------------------------------------------------------------------------------

import subprocess 

devices = subprocess.check_output(['netsh','wlan','show','network']) 
devices = devices.decode('utf-8', errors ='backslashreplace').split('\n')

redes_list     = [a.split(":")[1][1:-1] for a in devices if 'SSID' in a]
autentica_list = [a.split(":")[1][1:-1] for a in devices if 'Autentica' in a]
cripto_list    = [a.split(":")[1][1:-1] for a in devices if 'Criptografia' in a]
tipo_list      = [a.split(":")[1][1:-1] for a in devices if 'Tipo' in a]

redes_dict = dict()
posicao = 0
for rede in redes_list:
    redes_dict[rede] = {
            'TipoRede'    : tipo_list[posicao],
            'Autenticacao': autentica_list[posicao],
            'Criptografia': cripto_list[posicao]
        }
    posicao += 1

for key in redes_dict.keys():
    print(f'{key:<30} | {redes_dict[key]["TipoRede"]:<20} | {redes_dict[key]["Autenticacao"]:<20} | {redes_dict[key]["Criptografia"]}')

