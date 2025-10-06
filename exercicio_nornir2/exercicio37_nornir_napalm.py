from load_environment import load_environment
from nornir_setup import init_nornir
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError
from nornir_napalm.plugins.tasks import napalm_get


def main():
    try:
        print("🚀 Starting Napalm configuration retrieval...")
        
        env = load_environment()
        
        nr = init_nornir(env)
           
        results = nr.run(
            task=napalm_get, 
            getters=["get_interfaces"]
        )
        
        print_result(results)

    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")

if __name__ == "__main__":
    main()
