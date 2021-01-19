
import sys
import couchdb
from tweepy import Stream 
from tweepy import OAuthHandler 
from tweepy.streaming import StreamListener 
import json


###API ########################
ckey = "4BwkVPna1QDYpUehrnG7dJEd5"
csecret = "oH1q0nChKwSjyxKpGfqrLmRPnBoFzy5cYoW2jzyqiCNtvm7VfO"
atoken = "711211480264396801-HUWmZDfR8pzrbHp0kwjMTnV2SG5K7fN"
asecret = "xfiAQyTXCbNaYVVqMCYQlqAFqX1NDuztK0pvCXxXDShTw"
#####################################


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Guillo9977:guillo07@localhost:5984/')  
try:
    db = server.create('examen_ad_guillermo')
except:
    db = server('examen_ad_guillermo')
    
#CRITERIO DE FILTRACIÓN
twitterStream.filter(track=['pokemon','2021','diamante','perla','remake'])
