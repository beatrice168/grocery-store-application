import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1',
                              database='grocery_store')

cursor = cnx.cursor()

query=("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom "
       "FROM products INNER JOIN uom on products.uom_id=uom.uom_id")
cursor.execute(query)


for(product_id, name, uom_id, price_per_unit, uom) in cursor:
    print(product_id, name, uom_id, price_per_unit, uom)




cnx.close()
