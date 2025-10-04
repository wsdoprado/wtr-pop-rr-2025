from load_environment import load_environment
from nornir_setup import init_nornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir.core.task import Task, Result


def get_config(task: Task) -> Result:
    """
    Executes Napalm getter for interfaces
    """
    try:
        print(task.host)
        response = task.run(
            task=napalm_get,
            getters=["get_interfaces"]
        )

        interfaces = response.result.get("get_interfaces", {})


        for iface_name, iface_data in interfaces.items():
            print(f"{iface_name}: UP={iface_data['is_up']}, ENABLED={iface_data['is_enabled']}")


        return Result(
            host=task.host,
            result=interfaces
        )

    except Exception as e:
        return Result(
            host=task.host,
            result=f"❌ Error: {str(e)}",
            failed=True
        )


def main():
    try:
        print("🚀 Starting Napalm interface check...")

        env = load_environment()
        nr = init_nornir(env)

        results = nr.run(task=get_config)
        #print_result(results)

    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")


if __name__ == "__main__":
    main()
