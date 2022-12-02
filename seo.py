# SEO By: Euronymou5
# SEO en fase de desarrollo (v1.0)

import os
import requests
import time
from googlesearch import search
import random
import json
import re
from config import intel_api, verify_email

class Colores:
  rojo = "\033[31m"
  verde = "\033[32m"

logo_sc = """
\033[36m      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣴⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[34m       ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣧⣝⠛⠛⠃⣾⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[36m⠀⠀      ⠀⠀⠀⠀⠀⠀⣄⡻⠿⠟⠃⢀⣀⣀⣌⣽⣯⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[34m⠀⠀⠀⠀      ⠀⠀⠀⠀⣿⣿⡿⠁⠐⠉⠈⣿⣷⡻⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[36m⠀⠀⠀⠀      ⠀⠀⠀⠀⣩⣶⣥⡀⠀⠀⢀⣘⣿⠿⢋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[34m⠀⠀⠀⠀⠀      ⠀⠀⠀⣿⣯⣷⣶⣦⢠⡞⢡⣿⣻⡿⣻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[36m  ⠀⠀⠀    ⢀⣠⡿⠻⣄⣘⢻⣿⣿⣿⣿⠷⣛⢿⢟⣵⡟⣾⣷⣿⣶⣤⣴⣤⠀⠀⠀
\033[34m   ⠀⠀   ⣼⠟⣡⣤⣤⣬⣿⣣⣅⣿⣿⣿⣿⣿⣿⣞⠉⣘⣿⠋⡝⠛⢿⣿⣿⣷⣀⠀
\033[36m⠀      ⢀⡇⢰⣿⢡⡴⠽⣷⣾⡿⠿⣷⣹⡛⠿⢿⣭⡝⠛⠃⠀⠻⠄⠀⠸⣿⣿⣿⣧
\033[34m      ⠐⠉⠀⠈⣿⢸⡇⢰⡟⠿⠿⠛⠛⠉⡤⢾⠃⣏⠁⠟⠀⠀⠀⠀⣴⣿⠿⠛⣛⡋
\033[36m⠀      ⠀⠀⠀⣻⢘⡇⢸⠏⠀⣰⣭⠻⠿⣿⠎⠀⠈⠀⠀⠀⠀⠀⠀⡿⠃⠀⣀⣿⠃
\033[34m⠀⠀      ⠀⠈⠁⠀⣻⠹⣆⢰⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠟⠁⠀
\033[36m⠀⠀⠀      ⠀⠀⠘⠁⠀⡾⢸⣿⣟⣿⣶⣶⣶⣤⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
\033[34m⠀⠀⠀⠀      ⠀⠀⠀⠀⠀⠀⢿⢸⣿⣿⣿⣿⠿⠻⠿⠛⠋⠙⠃⠀⠀⠀⠀⠀⠀⠀
\033[36m⠀⠀⠀⠀⠀      ⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠁⠻⠷⢦⠶⠖⠂⠀⠀⠀⠀⠀⠀⠀⠀
"""
logo = """
      --------------------------------------------
      |        ███████ ███████  ██████           |
      |        ██      ██      ██    ██          |
      |        ███████ █████   ██    ██          |
      |             ██ ██      ██    ██          |
      |        ███████ ███████  ██████           |
      |                                          | 
      |                v1.0                      |
      ------ :[ Scorpion Email Osint] : ----------
"""

dom = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]

def main():
  os.system("clear")
  print(logo_sc)
  print(logo)
  email = input(f'\n{Colores.verde}[-] Introduce un email: ')
  if len(email) == 0 or email == " ":
    print(f'\n{Colores.rojo}[!] Error debes ingresar algun email.')
    time.sleep(3)
    main()
  else:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
      print('\n[?] Valido: Email valido')
    else:
      print(f'\n{Colores.rojo}[?] Valido: Email invalido')
      exit()
    response = requests.get(f'https://verifymail.io/api/{email}?key={verify_email}')
    data = json.loads(response.content.decode())
    time.sleep(1)
    try: 
      if data['disposable'] == False:
        print('\n[?] Email desechable: No')
      else:
        print('\n[?] Email desechable: Si')
      time.sleep(2)
      print('\n[~] Dominio: ', data['domain'])
      time.sleep(2)
      if data['block'] == False:
        print('\n[?] Bloqueado: No')
      else:
       print('\n[?] Bloqueado: Si')
    except KeyError:
      print(f'{Colores.rojo}\n[!] Ha ocurrido un error.')
    print(f'\n{Colores.verde}[~] Buscando datos...')
    time.sleep(1)
    # Dorking
    print(f'\n{Colores.verde}[~] Iniciando busqueda de Google dorking...')
    tld = random.choice(dom)
    command = f'intext:{email}' # Simple busqueda de dorking intext
    command2 = f"site:@ filetype:PDF intext:{email}" # Busqueda de el email en archivos .pdf 
    command3 = f"site:facebook.com intext:{email}"
    command4 = f"site:twitter.com intext:{email}"
    command5 = f"site:instagram.com intext:{email}"
    for j in search(command, tld, num=10, stop=10, pause=2):
     print(f'\nResultados encontrados!: {j}')
    print('\n[~] Buscando email en archivos pdf...')
    time.sleep(4)
    for i in search(command2, tld, num=10, stop=10, pause=2):
      print(f'\nResultados encontrados!: {i}')
    print('\n[~] Buscando correo electronico en redes sociales...')
    for a in search(command3, tld, num=10, stop=10, pause=2):
      print(f'\nResultados encontrados!: {a}')
    for b in search(command4, tld, num=10, stop=10, pause=2):
      print(f'\nResultados encontrados!: {b}')
    for c in search(command5, tld, num=10, stop=10, pause=2):
      print(f'\nResultados encontrados!: {c}')
    # Socialscan
    print('\n[~] Iniciando socialscan...')
    time.sleep(4)
    print('')
    os.system(f"socialscan {email}")
    # H8mail
    print('\n[~] Iniciando h8mail...')
    time.sleep(4)
    print('')
    os.system(f"h8mail -t {email}")
    # Intel X
    print(f'{Colores.verde}\n[~] Iniciando Intelligence X...')
    os.system(f"python3 modules/intelx.py -search {email} -apikey {intel_api}")

    
main()
