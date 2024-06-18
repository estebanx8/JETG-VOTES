import requests
from time import sleep
from random import randint
from itertools import cycle

def print_ascii_art():
    print(r"""
 ▄▄▄██▀▀▀▓█████▄▄▄█████▓  ▄████     ██▒   █▓ ▒█████  ▄▄▄█████▓▓█████   ██████ 
   ▒██   ▓█   ▀▓  ██▒ ▓▒ ██▒ ▀█▒   ▓██░   █▒▒██▒  ██▒▓  ██▒ ▓▒▓█   ▀ ▒██    ▒ 
   ░██   ▒███  ▒ ▓██░ ▒░▒██░▄▄▄░    ▓██  █▒░▒██░  ██▒▒ ▓██░ ▒░▒███   ░ ▓██▄   
▓██▄██▓  ▒▓█  ▄░ ▓██▓ ░ ░▓█  ██▓     ▒██ █░░▒██   ██░░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒
 ▓███▒   ░▒████▒ ▒██▒ ░ ░▒▓███▀▒      ▒▀█░  ░ ████▓▒░  ▒██▒ ░ ░▒████▒▒██████▒▒
 ▒▓▒▒░   ░░ ▒░ ░ ▒ ░░    ░▒   ▒       ░ ▐░  ░ ▒░▒░▒░   ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░
 ▒ ░▒░    ░ ░  ░   ░      ░   ░       ░ ░░    ░ ▒ ▒░     ░     ░ ░  ░░ ░▒  ░ ░
 ░ ░ ░      ░    ░      ░ ░   ░         ░░  ░ ░ ░ ▒    ░         ░   ░  ░  ░  
 ░   ░      ░  ░              ░          ░      ░ ░              ░  ░      ░  
                                        ░                                     
    """)

def main_menu():
    print("\n----- Menú Principal -----")
    print("1. Configurar votación")
    print("2. Salir")
    choice = input("Seleccione una opción: ")
    return choice

def configure_voting():
    url = input("Ingrese la URL de la página de votación (usa HTTP / HTTPS): ")
    option_id = input("Ingrese el ID de la opción a votar: ")
    
    proxies = []
    print("Ingrese la lista de proxies (escriba 'fin' para terminar):")
    while True:
        proxy = input()
        if proxy.lower() == 'fin':
            break
        proxies.append(proxy)
    
    return url, option_id, proxies

def start_voting(url, option_id, proxies):
    proxy_pool = cycle(proxies)
    session = requests.Session()
    
    try:
        num_votes = int(input("Ingrese el número de votos: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    for i in range(num_votes):
        proxy = next(proxy_pool)
        proxies_dict = {"http": proxy, "https": proxy}
        
        # Simulación de comportamiento humano
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = session.post(url, data={"optionId": option_id}, proxies=proxies_dict, headers=headers)
        print(f"Voto {i + 1}: {response.text}")
        
        # Pausa aleatoria entre solicitudes
        sleep(randint(1, 5))

if __name__ == "__main__":
    print_ascii_art()
    while True:
        choice = main_menu()
        if choice == '1':
            url, option_id, proxies = configure_voting()
            start_voting(url, option_id, proxies)
        elif choice == '2':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
