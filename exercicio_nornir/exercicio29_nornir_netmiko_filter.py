from nornir import InitNornir
from nornir_rich.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command

def main():
    # Inicializa Nornir com inventário e runner
    nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 20}},
        config_file="./hosts.yaml"
    )

    comando = "show interfaces"

    r1 = nr.filter(name="R1")
    
    try:
        results = r1.run(
            task=netmiko_send_command,
            read_timeout=120,
            command_string=comando
        )

        print_result(results)

    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")

if __name__ == "__main__":
    main()
