from napalm import get_network_driver

# Informações do dispositivo
HOST = "2001:db8:100::101"
USERNAME = "admin"
PASSWORD = "admin"

def main():
    device = None
    try:
        # Obter driver para Arista EOS
        driver = get_network_driver("eos")

        # Criar conexão
        device = driver(HOST, USERNAME, PASSWORD)
        device.open()

        # Obter tabela ARP
        arp_table = device.get_arp_table()

        print("📌 Tabela ARP:")
        for entry in arp_table:
            print(
                f"IP: {entry.get('ip')}, MAC: {entry.get('mac')}, Interface: {entry.get('interface')}, "
                f"Age: {entry.get('age')}"
            )

    except Exception as e:
        print(f"❌ Erro ao conectar ou coletar ARP table: {e}")

    finally:
        if device:
            try:
                device.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
