"""
Exercício 13 - Backup Automático de Dispositivos do NetBox
-----------------------------------------------------------
Este script demonstra como:
1. Consumir API do NetBox para listar dispositivos.
2. Filtrar dispositivos com plataforma Arista EOS.
3. Conectar via Netmiko.
4. Obter a configuração em execução.
5. Salvar a configuração em arquivo.
"""

from netmiko import ConnectHandler
from dotenv import load_dotenv
import requests
import os

# Carregar variáveis de ambiente
load_dotenv("../.env.dev")

NETBOX_URL = os.getenv("NETBOX_URL")
NETBOX_TOKEN = os.getenv("NETBOX_TOKEN")
USER_DEVICE = os.getenv("USER_DEVICE")
PASSW_DEVICE = os.getenv("PASSW_DEVICE")

HEADERS = {
    "Authorization": f"Token {NETBOX_TOKEN}",  # Autenticação via token
    "Content-Type": "application/json"
}

url = f"{NETBOX_URL}/api/dcim/devices/"

try:
    print("🔍 Consultando NetBox para obter lista de dispositivos...")
    response = requests.get(url, headers=HEADERS, verify=False)
    response.raise_for_status()  # Lança exceção para erros HTTP

    data = response.json()  # Converte a resposta em dict/list

    for device in data.get("results", []):
        # Extrair IP principal do dispositivo
        if device.get("primary_ip"):
            ip_address = device["primary_ip"]["address"].split("/")[0]
        else:
            ip_address = None

        # Filtrar apenas dispositivos EOS
        if device.get("platform") and device["platform"].get("name") == "eos" and ip_address:
            print(f"\n📡 Processando dispositivo: {device['name']} - IP: {ip_address}")

            device_dict = {
                "device_type": "arista_eos",
                "ip": ip_address,
                "username": USER_DEVICE,
                "password": PASSW_DEVICE,
            }

            try:
                conn = ConnectHandler(**device_dict)

                prompt = conn.find_prompt()
                print(f"Prompt detectado: {prompt}")

                # Entrar em modo enable se necessário
                if ">" in prompt:
                    print("⚡ Entrando em modo enable...")
                    conn.enable()

                print("💾 Obtendo configuração em execução...")
                output = conn.send_command("show running-config")

                backup_file = f"{device['name']}.cfg"
                print(f"📄 Salvando backup em: {backup_file}")
                with open(backup_file, "w") as f:
                    f.write(output)

                conn.disconnect()
                print(f"✅ Backup finalizado para {device['name']}")

            except Exception as err:
                print(f"❌ Erro ao conectar/dispositivo {device['name']}: {err}")

except requests.exceptions.RequestException as e:
    print(f"❌ Erro ao consumir API do NetBox: {e}")
