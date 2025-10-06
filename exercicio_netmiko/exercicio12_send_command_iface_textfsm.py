from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env.dev
load_dotenv("../.env.dev")

USER_DEVICE = os.getenv("USER_DEVICE")
PASSW_DEVICE = os.getenv("PASSW_DEVICE")

# Configuração do dispositivo
device = {
    "device_type": "arista_eos",
    "ip": "2001:db8:100::101",
    "username": USER_DEVICE,
    "password": PASSW_DEVICE,
}

try:
    print(f"🔌 Conectando ao dispositivo {device['ip']}...")
    conn = ConnectHandler(**device)

    print("✅ Conexão estabelecida.\nExecutando comando 'show ip int brief'...\n")
    output = conn.send_command("show ip int brief", use_textfsm=True)
    
    if output:
        print("--- Interfaces encontradas ---")
        for interface in output:
            print(
                f"Interface: {interface.get('interface', 'N/A')}, "
                f"IP: {interface.get('ip_address', 'N/A')}, "
                f"Status: {interface.get('status', 'N/A')}, "
                f"Protocol: {interface.get('protocol', 'N/A')}"
                f"MTU: {interface.get('mtu', 'N/A')}"
            )
    else:
        print("⚠ Nenhuma interface encontrada ou erro no parsing do TextFSM.")

    conn.disconnect()
    print("\n🔒 Conexão encerrada.")

except Exception as err:
    print(f"❌ Erro ao conectar ou executar comando: {err}")
