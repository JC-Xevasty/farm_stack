from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Get configuration values from .env file
load_dotenv()

# MONGODB URI CONNECTION
uri = os.getenv("MONGO_URI")


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Database Name
db = client[os.getenv("DB_NAME")]

# Tables / Collections
object_collection = db["objects"]
