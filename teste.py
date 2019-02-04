import firebase_admin
from firebase_admin import credentials

cred = credentials.Cert('path/to/serviceKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://my-db.firebaseio.com'
})