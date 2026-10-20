import os
from dotenv import load_dotenv

load_dotenv()

app_env = os.getenv("APP_ENV", "dev")
port = os.getenv("PORT", "8017")

if app_env == "dev":
    print("🛠️ Mode développement : Prêt pour le test local.")
elif app_env == "prod":
    print("🚀 Mode PRODUCTION : Sécurité maximale activée !")