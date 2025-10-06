from ncclient import manager
from dotenv import load_dotenv

import os


# Carregar variáveis de ambiente do arquivo .env.dev
load_dotenv("../.env.dev")

USER_DEVICE = os.getenv("USER_DEVICE")
PASSW_DEVICE = os.getenv("PASSW_DEVICE")

# Definição do dispositivo
device = {
    "host": "2001:db8:100::101",
    "port": 830,
    "username": USER_DEVICE,
    "password": PASSW_DEVICE,
    "hostkey_verify": False,
}

try:
    print(f"Conectando ao dispositivo {device['host']}...")
    
    new_hostname = "WTR-ROUTER"

    config_payload = f"""
    <config>
    <system xmlns="http://openconfig.net/yang/system">
        <config>
        <hostname>{new_hostname}</hostname>
        </config>
    </system>
    </config>
    """

    with manager.connect(**device) as m:
        m.edit_config(target="running", config=config_payload)
        print(f"Hostname alterado para {new_hostname}")

except Exception as err:
    print(f"❌ Erro ao conectar ou executar comando: {err}")
