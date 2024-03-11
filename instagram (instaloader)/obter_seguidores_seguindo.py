# ------------------------------------------------------------------------------------------
# Este exemplo salva em um arquivo a listagem de perfis seguidores e em outro 
# arquivo a listagem perfis que são seguido de um determinado perfil do Instagram.
#
# Necessário instalar a biblioteca INSTALOADER
#       pip install instaloader
#
# Documentação
#       https://pypi.org/project/instaloader/
#       https://instaloader.github.io/
# ------------------------------------------------------------------------------------------

import getpass, sys, os
from pstats import FunctionProfile
from time import sleep
from instaloader import Instaloader, Profile, exceptions
import instaloader

# Obtendo o diretório corrente
DIR_APP = os.path.dirname(os.path.realpath(__file__))

# Solicitando usuário e senha para efetuar login no Instagram
user = input('\nInforme seu Login do Instagram .: ')
pwd  = getpass.getpass('Informe sua senha do Instagram .: ')

erro = True

try:
    # Instancia um objeto com base no usuário logado
    logged_profile = instaloader.Instaloader()
    logged_profile.login(user, pwd)
except exceptions.BadCredentialsException:
    print('\nERRO: Credenciais Inválidas...')
except exceptions.TwoFactorAuthRequiredException:
    print('\nERRO: Autenticação em 2 Fatores exigida...')    
except exceptions.InvalidArgumentException:
    print('\nERRO: Argumentos Inválidos...')    
except exceptions.ConnectionException:
    print('\nERRO: Erro de Conexão...')    
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
else:
    erro = False
finally:
    if erro: sys.exit()
    erro = False
    # Solicita o perfil alvo
    target_profile = input('\nInforme o perfil alvo do Instagram .: ')
    try:
        # Objeto contendo os metadados do perfil alvo
        print('\n' + '-'*80)
        print(f'Obtendo dados do perfil @{target_profile}\n')
        profile = Profile.from_username(logged_profile.context, target_profile)
    except exceptions.ProfileNotExistsException:     
        print(f'\nERRO: Perfil @{target_profile} não existe...')    
    except:
        print(f'\nERRO: {sys.exc_info()[0]}')
    else:
        erro = False
    finally:
        if erro: sys.exit()
        BASE_NAME = DIR_APP + '\\' + target_profile
        followers_list = profile.get_followers()
        print(f'Gerando arquivo de SEGUIDORES (FOLLOWERS) .: {followers_list.count}')
        arqOutput = open(BASE_NAME + '_FOLLOWERS.txt', 'w', encoding='utf-8') 
        for followers in followers_list:
            arqOutput.write(f'@{followers.username}\n')
        arqOutput.close()
        followees_list = profile.get_followees()
        print(f'Gerando arquivo de SEGUINDO (FOLLOWEES) ...: {followees_list.count}')
        arqOutput = open(BASE_NAME + '_FOLLOWEES.txt', 'w', encoding='utf-8') 
        for followees in followees_list:
            arqOutput.write(f'@{followees.username}\n')
        arqOutput.close()
        print('-'*80)
        logged_profile.close()
