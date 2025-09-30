from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env.dev
load_dotenv("../.env.dev")

USER_DEVICE = os.getenv("USER_DEVICE")
PASSW_DEVICE = os.getenv("PASSW_DEVICE")

device = {
    "device_type": "arista_eos",
    "ip": "2001:db8:100::101",
    "username": f"{USER_DEVICE}",
    "password": f"{PASSW_DEVICE}",
}

try:
    conn = ConnectHandler(**device)

    prompt=conn.find_prompt()

    if '>' in prompt:
        print('Entering enable mode')
        conn.enable()

    commands = ["interface Ethernet 2", "switchport mode trunk",  "switchport trunk allowed vlan 10,20,100"]
    
    output = conn.send_config_set(commands)
    
    print(output)

    conn.disconnect()

except Exception as err:
    print(err)
