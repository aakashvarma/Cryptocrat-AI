import pyrebase

config = {
  "apiKey": "AIzaSyAT1llqLb19Zp76JrAOXdgPpb4BGAak1GI",
  "authDomain": "cryptocrat-83570.firebaseapp.com",
  "databaseURL": "https://cryptocrat-83570.firebaseio.com",
  "storageBucket": "cryptocrat-83570.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

data = {
    "url": 'https://www.coindesk.com/swiss-central-banker-state-backed-crypto-pose-incalculable-risks/',
    "text": 'None'
}
db.child("links").child("oe").set(data)





