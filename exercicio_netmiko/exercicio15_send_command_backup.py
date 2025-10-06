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

    # Entrar em modo enable se necessário
    if ">" in prompt:
        print("⚡ Entrando em modo enable...")
        conn.enable()

    print("💾 Obtendo configuração atual...")
    output = conn.send_command("show running-config")

    backup_file = "backup-ceos1.cfg"
    print(f"📄 Salvando configuração em '{backup_file}'...")
    with open(backup_file, "w") as f:
        f.write(output)

    print("✅ Backup realizado com sucesso.")

    conn.disconnect()
    print("🔒 Conexão encerrada.")

except Exception as err:
    print(f"❌ Erro ao conectar ou realizar backup: {err}")
