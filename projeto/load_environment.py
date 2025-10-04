import os
from dotenv import load_dotenv


def load_environment():
    """
    Loads environment variables from .env file.
    """
    load_dotenv("../.env.dev")

    nb_token = os.getenv("NETBOX_TOKEN")
    nb_url = os.getenv("NETBOX_URL")
    user = os.getenv("USER_DEVICE")
    passw = os.getenv("PASSW_DEVICE")

    if not nb_token or not nb_url or not user or not passw:
        raise EnvironmentError("Missing required environment variables in the .env file.")

    return {"nb_url": nb_url, "nb_token": nb_token, "user": user, "passw": passw}