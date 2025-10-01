"""
Exercício 26 - 

"""

import os
from nornir import InitNornir
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env.dev
load_dotenv("../.env.dev")

NETBOX_URL = os.getenv("NETBOX_URL")
NETBOX_TOKEN = os.getenv("NETBOX_TOKEN")

def main():
    # Inicializa Nornir com inventário e runner
    nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 20}},
        inventory={
            "plugin": "NetBoxInventory2",
            "options": {
                "nb_url": NETBOX_URL,
                "nb_token": NETBOX_TOKEN,
                "ssl_verify": False}
        })
    
    print(nr.inventory.hosts)
    
    print(nr.inventory.hosts['leaf-01'].data)

if __name__ == "__main__":
    main()
