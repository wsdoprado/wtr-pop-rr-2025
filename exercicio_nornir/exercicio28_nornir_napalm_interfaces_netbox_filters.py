"""
Exercício 28 - 

"""

import os
from nornir import InitNornir
from nornir_rich.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env.dev
load_dotenv("../.env.dev")

USER_DEVICE = os.getenv("USER_DEVICE")
PASSW_DEVICE = os.getenv("PASSW_DEVICE")
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
                "filter_parameters": {"role": ["spine"]},
                "ssl_verify": False}
        })
    
    nr.inventory.defaults.username = USER_DEVICE
    nr.inventory.defaults.password = PASSW_DEVICE

    try:
        results = nr.run(
            task=napalm_get,
            getters=["get_interfaces"]
        )

        print_result(results)

    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")

if __name__ == "__main__":
    main()
