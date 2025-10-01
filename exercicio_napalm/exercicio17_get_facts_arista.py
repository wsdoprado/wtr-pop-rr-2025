"""
Exercício 17 - Uso básico do NAPALM
-------------------------------------
Este script demonstra como:
1. Conectar em um dispositivo de rede usando NAPALM.
2. Obter informações básicas do dispositivo.
"""

from napalm import get_network_driver

# Informações do dispositivo
HOST = "2001:db8:100::101"
USERNAME = "admin"
PASSWORD = "admin"

def main():
    try:
        # Obter driver para Arista EOS
        driver = get_network_driver("eos")

        # Criar conexão com o dispositivo
        device = driver(HOST, USERNAME, PASSWORD)
        device.open()

        # Obter informações básicas do dispositivo
        facts = device.get_facts()
        print("📌 Informações básicas do dispositivo:")
        for key, value in facts.items():
            print(f"  {key}: {value}")

    except Exception as e:
        print(f"❌ Erro ao conectar ou coletar dados: {e}")

    finally:
        try:
            device.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
