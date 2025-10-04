"""
Exercício 30 - 

"""

from load_environment import load_environment
from nornir_setup import init_nornir
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError
from nornir_netmiko.tasks import netmiko_send_command


def main():
    try:
        print("🚀 Starting Netmiko configuration retrieval...")
        
        env = load_environment()
        
        nr = init_nornir(env)
           
        results = nr.run(
            task=netmiko_send_command,
            command_string="show interfaces",
            read_timeout=120
        )
        
        print_result(results)

    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")

if __name__ == "__main__":
    main()
