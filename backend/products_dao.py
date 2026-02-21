from sql_connection import  get_sql_connection

def get_all_products(connection):
    
    cursor_obj = connection.cursor() 

    query=("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom "
       "FROM products INNER JOIN uom on products.uom_id=uom.uom_id")
    cursor_obj.execute(query) #running the query 

    response = [] #empty shopping list 

     #for each product found add it to our list
    for(product_id, name, uom_id, price_per_unit, uom) in cursor_obj:
     response.append({
        'product_id': product_id,
        'name': name, 
        'uom_id': uom_id, 
        'price_per_unit': price_per_unit, 
        'uom': uom
     })


    return response  #return the list

def insert_new_product(connection, product):
   cursor_obj=connection.cursor()
   query=("INSERT INTO products "
          " (name, uom_id, price_per_unit)"
          " VALUES (%s, %s, %s)")
   
   data=(product['product_name'], product['uom_id'], product['price_per_unit'])

   cursor_obj.execute(query, data) #add the new product
   connection.commit() # save te changes permanently 
   return cursor_obj.lastrowid # returning the new product's id 

def delete_product(connection, product_id):
   cursor_obj = connection.cursor()
   query = ("DELETE FROM products where product_id=" + str(product_id))
   cursor_obj.execute(query)
   connection.commit()




if __name__=='__main__':
    connection = get_sql_connection() #first connect to db 
    print(get_all_products(connection))

    # print(delete_product(connection, 3)) #the delete the product with id 3 