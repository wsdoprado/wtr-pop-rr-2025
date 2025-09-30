from netmiko import ConnectHandler
from dotenv import load_dotenv
import requests
import os

# Carregar variáveis de ambiente do arquivo .env.dev
load_dotenv("../.env.dev")

NETBOX_URL = os.getenv("NETBOX_URL")
NETBOX_TOKEN = os.getenv("NETBOX_TOKEN")
USER_DEVICE = os.getenv("USER_DEVICE")
PASSW_DEVICE = os.getenv("PASSW_DEVICE")

HEADERS = {
    "Authorization": f"Token {NETBOX_TOKEN}", # Autenticação via token
    "Content-Type": "application/json"        # Informar que o payload é JSON
}

url = f"{NETBOX_URL}/api/dcim/devices/"

try:
    response = requests.get(url, headers=HEADERS, verify=False)
    data = response.json()  # converte o corpo da resposta em dict/list
    
    for device in data['results']:
        if device.get('primary_ip'):
            ip_address = device['primary_ip']['address']
            ip_address = ip_address.split("/")[0]  # pega só o IP sem máscara
        else:
            ip_address = "N/A" 

        if device['platform']['name'] == "eos":       
            device_dict = {
                "device_type": "arista_eos",
                "ip": ip_address,
                "username": f"{USER_DEVICE}",
                "password": f"{PASSW_DEVICE}",
            }
            
            try:
                conn = ConnectHandler(**device_dict)
    
                prompt=conn.find_prompt()

                if '>' in prompt:
                    print('Entering enable mode')
                    conn.enable()

                output = conn.send_command("show running-config")
                archive = f"{device["name"]}.cfg"
                with open(f"{device["name"]}.cfg", "w") as f:
                    f.write(output)

                conn.disconnect()

            except Exception as err:
                print(err)

except requests.exceptions.RequestException as e:
    print(f"❌ Erro ao consumir API: {e}")
