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
        # Pega toda a configuração em execução (running)
        running_config = m.get_config(source="running")
        
        # Formata o XML para ficar legível
        xml_parsed = minidom.parseString(running_config.xml)
        pretty_xml = xml_parsed.toprettyxml(indent="  ")
        
        print("Configuração em XML formatado:\n", pretty_xml)

        # Conversão para dict
        dict_data = xmltodict.parse(running_config.xml)

        # Converter para JSON formatado
        json_data = json.dumps(dict_data, indent=2)
        print("Configuração em JSON:\n", json_data)



except Exception as err:
    print(f"❌ Erro ao conectar ou executar comando: {err}")
