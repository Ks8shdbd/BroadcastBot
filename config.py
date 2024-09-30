import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6078755818:AAHx7-Kp_kzyhANs6igib8ZtQ_i_rqYEe5Y")
API_ID = int(os.environ.get("API_ID", "3334521"))
API_HASH = os.environ.get("API_HASH", "29edd7420d528140c7a04bd47486886f")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002407546059"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5079629749").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://fakeone:fakeone@cluster0.hkpcv31.mongodb.net/fakeone?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "fakeone")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
