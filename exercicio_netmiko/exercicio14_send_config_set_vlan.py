from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env.dev
load_dotenv("../.env.dev")

USER_DEVICE = os.getenv("USER_DEVICE")
PASSW_DEVICE = os.getenv("PASSW_DEVICE")

# Definição do dispositivo
device = {
    "device_type": "arista_eos",
    "ip": "2001:db8:100::101",
    "username": USER_DEVICE,
    "password": PASSW_DEVICE,
}

try:
    print(f"🔌 Conectando ao dispositivo {device['ip']}...")
    conn = ConnectHandler(**device)

    prompt = conn.find_prompt()
    print(f"Prompt atual: {prompt}")

    # Verifica se precisa entrar em modo enable
    if ">" in prompt:
        print("⚡ Entrando em modo enable...")
        conn.enable()

    # Lista de comandos a serem enviados
    commands = [
        "interface Ethernet 2",
        "switchport mode trunk",
        "switchport trunk allowed vlan 10,20,100"
    ]

    print("🛠 Enviando comandos de configuração...")
    output = conn.send_config_set(commands)

    print("\n--- Saída dos comandos ---")
    print(output)

    conn.disconnect()
    print("\n🔒 Conexão encerrada.")

except Exception as err:
    print(f"❌ Erro ao conectar ou enviar comandos: {err}")