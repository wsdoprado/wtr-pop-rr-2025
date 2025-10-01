"""
Exercício 7 - Consulta de Dispositivos via NetBox REST API
------------------------------------------------------------
Este script demonstra como:
1. Carregar credenciais do arquivo `.env.dev`.
2. Consultar a API REST do NetBox para listar dispositivos.
3. Aplicar filtros opcionais.
4. Exibir informações relevantes dos dispositivos.
"""

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
# Função para consultar dispositivos via REST API
# ----------------------------------------------------
def get_devices(params=None):
    """
    Consulta dispositivos cadastrados no NetBox.

    Args:
        params (dict, optional): Parâmetros para filtro, ex:
                                 {"site": "pop-sp", "role": "spine"}.

    Returns:
        list: Lista de dispositivos (dicts) retornados pela API.
    """
    url = f"{NETBOX_URL}/api/dcim/devices/"

    try:
        response = requests.get(url, headers=HEADERS, params=params, verify=False)
        response.raise_for_status()  # Lança erro para códigos HTTP inválidos

        data = response.json()
        return data.get("results", [])

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao consumir API: {e}")
        return []

# ----------------------------------------------------
# Execução principal do script
# ----------------------------------------------------
if __name__ == "__main__":
    # Exemplo de uso:
    devices = get_devices()  # Sem filtro
    # devices = get_devices(params={"site": "sp-site", "role": "pe"})

    print(f"📌 Total de dispositivos encontrados: {len(devices)}\n")

    for device in devices:
        # Obter IP de gerenciamento
        if device.get("primary_ip"):
            ip_address = device["primary_ip"]["address"].split("/")[0]
        else:
            ip_address = "N/A"

        # Exibir informações do dispositivo
        print(
            f"Nome: {device.get('name', 'N/A')} | "
            f"Site: {device.get('site', {}).get('name', 'N/A')} | "
            f"Role: {device.get('role', {}).get('name', 'N/A')} | "
            f"Tenant: {device.get('tenant', {}).get('name', 'N/A')} | "
            f"MGMT: {ip_address} | "
            f"Platform: {device.get('platform', {}).get('name', 'N/A')}"
        )
