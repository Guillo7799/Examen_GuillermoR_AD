import pymongo 
import dns
from argparse import ArgumentParser
import requests
from bson import json_util, ObjectId
from pymongo.errors import ConnectionFailure
import json
import couchdb


CLIENT = couchdb.Server('http://Guillo9977:guillo07@localhost:5984')

try:
    print('couch connection: Success')
except ConnectionFailure as e:
    print('Couch connection: failed', e)
    
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

client = pymongo.MongoClient("mongodb+srv://esfot_prueba:esfotesfot@cluster0.tddsj.mongodb.net/examen?retryWrites=true&w=majority")
DBm = client.get_database('examen')
DBma =DBm.examgr

try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)
    
DBc=CLIENT['examen_ad_guillermo']

for db in DBc:
    try:
        DBma.insert_one(DBc[db])
        print('Data saved mongoDB Atlas')
    except TypeError as et:
        print('current document raised error: {}'.format(et))
        SKIPPED.append(db)
        continue
    except Exception as e:
        raise e
