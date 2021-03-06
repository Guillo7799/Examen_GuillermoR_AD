import couchdb
from pymongo import MongoClient
import json
import requests
URL='http://Guillo9977:guillo07@localhost:5984'
print(URL)
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

CLIENT = MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

db=server['examen_ad_guillermo']
for id_doc in db.view('_all_docs'):
	try:
		id=id_doc['id']
		data=db[id]
		print(data)
		CLIENT.examn.twitter.insert(data)
	except Exception as e:
		raise e

