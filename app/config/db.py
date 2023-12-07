from pymongo.mongo_client import MongoClient
import os

# Get the MongoDB connection string from the environment variable
URI = os.environ.get("MONGO_URI")

# Create a new client and connect to the server
mongo_client = MongoClient(URI)
