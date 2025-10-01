"""
Exercício 21 - Consulta ARP Table usando Scrapli
---------------------------------------------------
Este script demonstra como:
1. Conectar a um dispositivo Arista EOS usando Scrapli.
2. Coletar a tabela ARP.
"""

from scrapli.driver.core import EOSDriver

# Informações do dispositivo
HOST = "2001:db8:100::101"
USERNAME = "admin"
PASSWORD = "admin"

def main():
    try:
        # Criar conexão com o dispositivo
        device = EOSDriver(
            host=HOST,
            auth_username=USERNAME,
            auth_password=PASSWORD,
            transport="paramiko"  # Pode ser "paramiko" para SSH
            #transport="asyncssh"  # Pode ser "paramiko" para SSH
            #transport="https"  # Pode ser "paramiko" para SSH
            #transport="telnet"  # Pode ser "paramiko" para SSH
        )

        device.open()

        # Enviar comando para coletar ARP Table
        result = device.send_command("show arp")

        # Imprimir saída bruta
        print("📌 Saída bruta:")
        print(result.result)

        # Imprimir saída estruturada (se houver parser)
        if result.failed:
            print("❌ Erro ao executar comando.")
        else:
            print("\n✅ Comando executado com sucesso.")

    except Exception as e:
        print(f"❌ Erro de conexão ou execução: {e}")

    finally:
        try:
            device.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
