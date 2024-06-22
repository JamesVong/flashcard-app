import os
import pyrebase
from dotenv import load_dotenv

load_dotenv()

config={
  "apiKey": os.getenv("APIKEY"),
  "authDomain": os.getenv("AUTHDOMAIN"),
  "databaseURL": os.getenv("DB"),
  "storageBucket": os.getenv("STORAGEBUCKET")
}
#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
