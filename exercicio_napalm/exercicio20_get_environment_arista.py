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

        # Coletar informações ambientais
        environment = device.get_environment()

        print("📌 Informações do Ambiente:")
        for key, value in environment.items():
            print(f"\n{key.upper()}:")
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    print(f"  {subkey}: {subvalue}")
            else:
                print(f"  {value}")

    except Exception as e:
        print(f"❌ Erro ao conectar ou coletar informações ambientais: {e}")

    finally:
        if device:
            try:
                device.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
