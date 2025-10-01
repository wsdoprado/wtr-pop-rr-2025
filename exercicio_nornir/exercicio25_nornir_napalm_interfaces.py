"""
Exercício 24 - 

"""

from nornir import InitNornir
from nornir_rich.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

def main():
    # Inicializa Nornir com inventário e runner
    nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 20}},
        config_file="./hosts.yaml"
    )
    
    try:
        results = nr.run(
            task=napalm_get,
            getters=["get_interfaces"]
        )

        print_result(results)

    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")

if __name__ == "__main__":
    main()
