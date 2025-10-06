from xml.dom import minidom
from ncclient import manager

import os
from dotenv import load_dotenv

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
    
    with manager.connect(**device) as m:
        print("=== Capabilities do dispositivo ===")
        for cap in m.server_capabilities:
            print(cap)

except Exception as err:
    print(f"❌ Erro ao conectar ou executar comando: {err}")
