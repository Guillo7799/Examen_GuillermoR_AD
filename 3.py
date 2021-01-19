from facebook_scraper import get_posts
import time
from pymongo import MongoClient
import json
import time

if __name__ == '__main__':
	db_client = MongoClient('localhost:27017')
    datos = db_client.Examen_AD_GuillermoR
    facebook = datos.posts

	i=1
	for post in get_posts('nokia', pages=100, extra_info=True):
	    print(i)
	    i=i+1
	    time.sleep(5)
	    
	    id=post['post_id']
	    doc={} 
	    doc['id']=id  
	    mydate=post['time']
	    try:
	        doc['texto']=post['text']
	        doc['date']=mydate.timestamp()
	        doc['likes']=post['likes']
	        doc['comments']=post['comments']
	        doc['shares']=post['shares']
	        doc['post_url']=post.insert['post_url']
	        db_client.Examen_AD_GuillermoR.insert(doc)
	        print("Se registro exitosamente")
	    except Exception as e:    
	        print("No se pudo registrar: "+str(e))