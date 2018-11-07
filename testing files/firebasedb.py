import pyrebase

config = {
  "apiKey": "###",
  "authDomain": "###",
  "databaseURL": "###",
  "storageBucket": "###"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

data = {
    "url": 'https://www.coindesk.com/swiss-central-banker-state-backed-crypto-pose-incalculable-risks/',
    "text": 'None'
}
db.child("links").child("oe").set(data)





