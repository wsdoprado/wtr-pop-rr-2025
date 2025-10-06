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

# Headers padrão para requisições REST API
HEADERS = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json"
}

# ----------------------------------------------------
# Função para consultar dispositivos
# ----------------------------------------------------
def get_devices(params=None):
    """
    Consulta dispositivos no NetBox.

    Args:
        params (dict, optional): Parâmetros de filtro para a API.

    Returns:
        list: Lista de dispositivos (dicionários).
    """
    url = f"{NETBOX_URL}/api/dcim/devices/"

    try:
        response = requests.get(url, headers=HEADERS, params=params, verify=False)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao consumir API de dispositivos: {e}")
        return []

# ----------------------------------------------------
# Função para consultar interfaces de um dispositivo
# ----------------------------------------------------
def get_interfaces(device_id):
    """
    Consulta as interfaces de um dispositivo no NetBox.

    Args:
        device_id (int): ID do dispositivo no NetBox.

    Returns:
        list: Lista de interfaces (dicionários).
    """
    url = f"{NETBOX_URL}/api/dcim/interfaces/"

    try:
        params = {"device_id": device_id}
        response = requests.get(url, headers=HEADERS, params=params, verify=False)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao consultar interfaces do dispositivo {device_id}: {e}")
        return []

# ----------------------------------------------------
# Execução principal do script
# ----------------------------------------------------
if __name__ == "__main__":
    devices = get_devices()

    print(f"📌 Total de dispositivos encontrados: {len(devices)}\n")

    for device in devices:
        # Obter IP de gerenciamento
        if device.get("primary_ip"):
            ip_address = device["primary_ip"]["address"].split("/")[0]
        else:
            ip_address = "N/A"

        device_id = device.get("id")

        # Consultar interfaces do dispositivo
        interface_list = get_interfaces(device_id)

        # Montar lista resumida de interfaces
        interfaces = []
        for interface in interface_list:
            iface = {
                "name": interface.get("name", "N/A"),
                "description": interface.get("description", ""),
                "mtu": interface.get("mtu", "N/A"),
                "mac_address": interface.get("mac_address", "N/A")
            }
            interfaces.append(iface)

        # Exibir informações resumidas
        print(
            f"📍 Device: {device.get('name', 'N/A')} | "
            f"Site: {device.get('site', {}).get('name', 'N/A')} | "
            f"Role: {device.get('role', {}).get('name', 'N/A')} | "
            f"Tenant: {device.get('tenant', {}).get('name', 'N/A')} | "
            f"MGMT: {ip_address} | "
            f"Interfaces: {interfaces}"
        )
