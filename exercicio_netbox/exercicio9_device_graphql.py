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

# ----------------------------------------------------
# Função para consultar dispositivos via GraphQL
# ----------------------------------------------------
def get_data_device(device_id=None):
    """
    Consulta devices no NetBox via GraphQL.

    Args:
        device_id (int, opcional): ID do device a ser filtrado.
                                    Se None, retorna todos os devices.

    Returns:
        dict: Dados retornados pelo NetBox (device_list).
    """

    # Monta o filtro dinamicamente caso device_id seja fornecido
    filters = f"(filters: {{id: {device_id}}})" if device_id else ""

    # Query GraphQL
    GRAPHQL_QUERY = f"""
    query {{
        device_list{filters} {{
            id
            name
            role {{
                name
            }}
            site {{
                name
            }}
            tenant {{
                name
            }}
            primary_ip4 {{
                address
            }}
            interfaces {{
                name
                ip_addresses {{
                    address
                }}
                description
                mtu
                mac_addresses {{
                    mac_address
                }}
            }}
        }}
    }}
    """

    url = f"{NETBOX_URL}/graphql/"
    payload = {"query": GRAPHQL_QUERY}

    try:
        response = requests.post(url, headers=HEADERS, json=payload, verify=False)
        response.raise_for_status()

        result = response.json()

        if "errors" in result:
            print(f"❌ Erros na query GraphQL: {result['errors']}")
            return None

        return result.get("data", {})

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição GraphQL: {e}")
        return None

# ----------------------------------------------------
# Execução principal do script
# ----------------------------------------------------
if __name__ == "__main__":
    print("🔍 Consultando dispositivos no NetBox via GraphQL...")
    data = get_data_device()

    if not data:
        print("⚠️ Nenhum dado retornado.")
    else:
        devices = data.get("device_list", [])
        print(f"📌 Total de dispositivos encontrados: {len(devices)}\n")

        for device in devices:
            print(f"Nome: {device.get('name')}")
            print(f"ID: {device.get('id')}")
            print(f"Site: {device.get('site', {}).get('name', 'N/A')}")
            print(f"Role: {device.get('role', {}).get('name', 'N/A')}")
            print(f"Tenant: {device.get('tenant', {}).get('name', 'N/A')}")
            print(f"IP de Gerenciamento: {device.get('primary_ip4', {}).get('address', 'N/A')}")

            print("Interfaces:")
            for iface in device.get("interfaces", []):
                ips = [ip.get("address") for ip in iface.get("ip_addresses", [])]
                print(f"  - {iface.get('name')} | Desc: {iface.get('description', '')} | MTU: {iface.get('mtu')} | MACs: {[m.get('mac_address') for m in iface.get('mac_addresses', [])]} | IPs: {ips}")
            print("-" * 60)
