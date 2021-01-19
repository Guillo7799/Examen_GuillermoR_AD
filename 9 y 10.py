from argparse import ArgumentParser
import requests
from pymongo  import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.errors import ServerSelectionTimeoutError
from bson import json_util, ObjectId
import pandas as pd
try:
    client=pymongo.MongoClient('mongodb+srv://esfot_prueba:esfotesfot@cluster0.tddsj.mongodb.net/examen?retryWrites=true&w=majority')
    client.server_info()
    print('Conexión con Atlas satisfactorio')
    
except pymongo.errors.ServerSelectionTimeoutError as e:
    print('Conexión con Atlas fallido: ',e)
    
except pymongo.errors.ConnectionFailure as e:
    print('Conexión con Atlas fallido: ',e)
    db=client.examen
datos=db.examen
data=datos.find()
collection=[]
for i in data:
    collection.append(i)
pd.DataFrame([collection]).to_csv('examen.csv', index=False)