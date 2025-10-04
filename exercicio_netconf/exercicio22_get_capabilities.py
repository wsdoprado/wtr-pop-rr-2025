"""
Exercício 21 - Automação de Redes com Netmiko
---------------------------------------------
Este script demonstra como conectar a um dispositivo de rede usando Netmiko,
executar um comando e exibir o resultado.

Objetivos:
1. Carregar credenciais de um arquivo .env.
2. Conectar a um dispositivo de rede.
3. Executar comandos.
4. Tratar erros de conexão.
"""

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
