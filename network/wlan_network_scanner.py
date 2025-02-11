import subprocess, platform

# --------------------------------------------------------------------------------
# Obtém a lista de redes Wi-Fi no Windows usando o comando netsh
def getWifiNetworkWindows():
   try:
      devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
      devices = devices.decode('utf-8', errors='backslashreplace').split('\n')
        
      lstRedes     = [a.split(":")[1][1:-1] for a in devices if 'SSID' in a]
      lstAutentica = [a.split(":")[1][1:-1] for a in devices if 'Autentica' in a]
      lstCripto    = [a.split(":")[1][1:-1] for a in devices if 'Criptografia' in a]
      lstTipo      = [a.split(":")[1][1:-1] for a in devices if 'Tipo' in a]

      redes_dict = {}
      for posicao, rede in enumerate(lstRedes):
         redes_dict[rede] = {
            'TipoRede': lstTipo[posicao],
            'Autenticacao': lstAutentica[posicao],
            'Criptografia': lstCripto[posicao] }
         return redes_dict
   except Exception as e:
      print(f'ERRO: Erro ao listar redes Wi-Fi no Windows: {e}')
      return {}

# --------------------------------------------------------------------------------
# Obtém a lista de redes Wi-Fi no Linux usando o comando nmcli
def getWifiNetworkLinux():
   try:
      devices = subprocess.check_output(['nmcli', '-t', '-f', 'SSID,SECURITY', 'dev', 'wifi'])
      devices = devices.decode('utf-8', errors='backslashreplace').split('\n')
        
      dictRedesDetectadas = dict()
      for device in devices:
         if device:
            ssid, security = device.split(':')
            dictRedesDetectadas[ssid] = {
               'TipoRede': 'Infraestrutura',  # Assume-se que todas são do tipo Infraestrutura
               'Autenticacao': security.split(' ')[0] if security else 'N/A',
               'Criptografia': security.split(' ')[-1] if security else 'N/A' }
         return dictRedesDetectadas
   except Exception as e:
      print(f'ERRO: Erro ao listar redes Wi-Fi no Linux: {e}')
      return {}

# --------------------------------------------------------------------------------
# Função principal que chama as funções específicas para cada sistema operacional
def main():
   strSistOpera = platform.system()
   if strSistOpera == 'Windows':
      dictRedes = getWifiNetworkWindows()
   elif strSistOpera == 'Linux':
      dictRedes = getWifiNetworkLinux()
   else:
      print('ERRO: Sistema operacional não suportado.')
      return

   if not dictRedes:
      print('ERRO: Nenhuma rede Wi-Fi encontrada ou erro ao listar redes.')
      return

   print(f"{'SSID':<30} | {'Tipo de Rede':<20} | {'Autenticação':<20} | {'Criptografia'}")
   print('-' * 90)
   for key, value in dictRedes.items():
      print(f"{key:<30} | {value['TipoRede']:<20} | {value['Autenticacao']:<20} | {value['Criptografia']}")

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == "__main__":
   main()