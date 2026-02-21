import mysql.connector

__cnx=None #stores connection (starts empty)


def get_sql_connection():
    global __cnx #use the connection we saved before
    if __cnx is None: #if no connection exists yet
        #create a connection to the database 
        __cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1',
                              database='grocery_store')
    return __cnx #give back the connection
