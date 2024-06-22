import os
import pyrebase


config={
  "apiKey": os.getenv("APIKEY"),
  "authDomain": os.getenv("AUTHDOMAIN"),
  "databaseURL": os.getenv("DB"),
  "storageBucket": os.getenv("STORAGEBUCKET")
}
#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
