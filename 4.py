import mysql.connector
from pymongo import MongoClient
client     = MongoClient()
db         = client.test
collection = db.payment

cnx = mysql.connector.connect(
		user ='guillo07', 
		password ='123123', 
	    database ='examen_gr'
   )
cursor = cnx.cursor()
row_titles = (
		'payment_id',   
		'payment_cust_id',
		'payment_desc',
		'payment_refer', 
		'payment_amt',
		'payment_dt'
	)
query = ( "SELECT " 
          "payment_dbid, payment_customer_bid, "  
          "payment_desc_txt, payment_refer_txt, "
          "payment_amt, payment_dt "
          "FROM payment" )

cursor.execute( query )
cus = dict()                                       
cid = 0                                                 
for ( row ) in cursor:
    cid        += 1   
    cus['_id'] = cid                                    
    for i in range( 0, len( row ) ):
        if row[i] == None:
            continue
        else:
            row_title      = "".join( row_titles[i] )     
            field          = str( row[i] ) 
            cus[row_title] = field
    id = collection.insert_one( cus ).inserted_id
    print id 

cursor.close()
cnx.close()