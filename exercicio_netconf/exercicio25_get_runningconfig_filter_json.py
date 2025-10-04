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
from dotenv import load_dotenv

import os
import xmltodict
import json


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
        filter_xml = """
        <filter>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
        </filter>
        """

        running_interfaces = m.get_config(source="running", filter=filter_xml)
        
        # Conversão para dict
        dict_data = xmltodict.parse(running_interfaces.xml)

        # Converter para JSON formatado
        json_data = json.dumps(dict_data, indent=2)
        print("Configuração em JSON:\n", json_data)

except Exception as err:
    print(f"❌ Erro ao conectar ou executar comando: {err}")
