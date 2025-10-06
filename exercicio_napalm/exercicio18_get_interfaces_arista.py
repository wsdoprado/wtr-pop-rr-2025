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

        # Obter informações das interfaces
        interfaces = device.get_interfaces()

        print("📌 Interfaces do dispositivo:")
        for iface_name, iface_data in interfaces.items():
            print(f"\nInterface: {iface_name}")
            for key, value in iface_data.items():
                print(f"  {key}: {value}")

    except Exception as e:
        print(f"❌ Erro ao conectar ou coletar dados: {e}")

    finally:
        if device:
            try:
                device.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
