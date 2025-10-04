from load_environment import load_environment
from nornir_setup import init_nornir
from nornir_rich.functions import print_result     
from nornir_netmiko.tasks import netmiko_send_config, netmiko_commit
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.task import Task, Result

import os
import requests
import urllib3

from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv("../.env.dev")

NETBOX_URL = os.getenv("NETBOX_URL")
NETBOX_TOKEN = os.getenv("NETBOX_TOKEN")

# Desabilita avisos SSL/TLS (não recomendado em produção)
urllib3.disable_warnings()

# Headers padrão para requisições GraphQL
HEADERS = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json"
}

def validation_nsot(task: Task) -> Result:
    
    url_graphql = NETBOX_URL+"graphql/"
    
    device_id = task.host['id']
    
    GRAPHQL_QUERY = {"query": f"""
    {{
        device_list(
            filters: 
            {{
                id: {device_id}
            }}
        )
    {{
        name
        primary_ip4
        {{
            address
        }}
        primary_ip6
        {{
            address
        }}
        platform
        {{
            name
        }}
        status
        interfaces
        {{
            name
            description
            mtu
            enabled
        }}
    }}
    }}"""}
    
    device_interfaces_netbox = requests.post(url=url_graphql, json=GRAPHQL_QUERY, headers=HEADERS, verify=False).json()['data']['device_list'][0]['interfaces']
    
    data_device = task.run(task=napalm_get,getters=["get_interfaces"])
    data_device = data_device.result['get_interfaces']
      
    for iface_nbx in device_interfaces_netbox:
        iface_name_nbx = iface_nbx.get('name')
        iface_description_nbx = iface_nbx.get('description')
        iface_status_nbx = iface_nbx.get('enabled')
        iface_mtu_nbx = iface_nbx.get('mtu')
    
        if data_device[iface_name_nbx]:
            if iface_name_nbx != "Management0":
                #print("Interface existe no equipamento")
                iface_name_device = data_device[iface_name_nbx].get('name')
                iface_description_device = data_device[iface_name_nbx].get('description')
                iface_status_device = data_device[iface_name_nbx].get('is_enabled')
                iface_mtu_device = data_device[iface_name_nbx].get('mtu')
                #print(f"NETBOX:  {iface_description_nbx} - {iface_status_nbx} - {iface_mtu_nbx}")
                #print(f"DEVICE:  {iface_description_device} - {iface_status_device} - {iface_mtu_device}")
                configurations=["interface "+str(iface_name_nbx)]
                
                if iface_status_device != iface_status_nbx:
                    if iface_status_nbx == True:
                        configurations.append("no shutdown")
                    if iface_status_nbx == False:
                        configurations.append("shutdown")
                        
                if iface_description_device != iface_description_nbx:
                    if iface_description_nbx == "":
                        configurations.append("no description")
                    else:        
                        configurations.append("description "+str(iface_description_nbx))
                        
                if iface_mtu_device != iface_mtu_nbx:
                    if iface_mtu_nbx != None:
                        configurations.append("mtu "+str(iface_mtu_nbx))
                    
                if len(configurations) > 1:
                    command = task.run(netmiko_send_config, config_commands=configurations)
                    print_result(command)

        
def main():
    try:
        print("🚀 Starting Final Project - WTR POP RR ")

        print("🚀 Carregando variaveis de ambiente ")
        env = load_environment()
        
        print("🚀 Inicializando inventario com nornir ")
        nr = init_nornir(env)

        print("🚀Rodando Task de Validacao dos dados ")
        results = nr.run(task=validation_nsot)

    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")


if __name__ == "__main__":
    main()