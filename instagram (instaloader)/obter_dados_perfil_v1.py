# ------------------------------------------------------------------------------------------
# Este exemplo exibe a quantidade de perfis seguidores, a quantidades de perfis 
# que são seguidos, a quantidade de postagens e a URL da foto do perfil de um 
# determinado perfil do Instagram.
#
# Necessário instalar a biblioteca INSTALOADER
#       pip install instaloader
#
# Documentação
#       https://pypi.org/project/instaloader/
#       https://instaloader.github.io/
# ------------------------------------------------------------------------------------------

import getpass, sys
from instaloader import Instaloader, Profile, exceptions

# Solicitando usuário e senha para efetuar login no Instagram
# Só é necessário para acessar dados de contas não públicas
user = input('\nInforme seu Login do Instagram .: ')
pwd  = getpass.getpass('Informe sua senha do Instagram .: ')

erro = True

try:
    # Instancia um objeto com base no usuário logado
    logged_profile = Instaloader()
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
    erro = True
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
        print(f'Seguidores .: {profile.get_followers().count}')
        print(f'Seguindo ...: {profile.get_followees().count}')
        print(f'Postagens ..: {profile.get_posts().count}')
        print(f'\nURL da foto do perfil:\n{profile.get_profile_pic_url()}')
        print('-'*80)
        logged_profile.close()