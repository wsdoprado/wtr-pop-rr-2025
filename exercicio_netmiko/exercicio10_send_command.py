"""
Exercício 10 - Automação de Redes com Netmiko
---------------------------------------------
Este script demonstra como conectar a um dispositivo de rede usando Netmiko,
executar um comando e exibir o resultado.

Objetivos:
1. Carregar credenciais de um arquivo .env.
2. Conectar a um dispositivo de rede.
3. Executar comandos.
4. Tratar erros de conexão.
"""

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
    print(f"Conectando ao dispositivo {device['ip']}...")
    conn = ConnectHandler(**device)

    print("Conexão estabelecida com sucesso.\nExecutando comando 'show version'...\n")
    output = conn.send_command("show version")

    print("--- Resultado do comando ---")
    print(output)

    conn.disconnect()
    print("\nConexão encerrada.")

except Exception as err:
    print(f"❌ Erro ao conectar ou executar comando: {err}")
