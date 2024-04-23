from database.db_mysql import create_server_connection, execute_query
from model.model_item import Item
import uuid

connection = create_server_connection("localhost", "root", "root123", "fastcrud")

def create_item(item: Item):
    item.id = str(uuid.uuid4())
    query = """
    INSERT INTO items (id, name, description, price, on_offer) 
    VALUES (%s, %s, %s, %s, %s);
    """
    vals = (item.id, item.name, item.description, item.price, item.on_offer)
    execute_query(connection, query, vals)
    return item

def get_all_items():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM items;"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def update_item(item_id: str, item: Item):
    query = """
    UPDATE items 
    SET name = %s, description = %s, price = %s, on_offer = %s 
    WHERE id = %s;
    """
    vals = (item.name, item.description, item.price, item.on_offer, item_id)
    execute_query(connection, query, vals)
    return item

def delete_item(item_id: str):
    query = "DELETE FROM items WHERE id = %s;"
    vals = (item_id,)
    execute_query(connection, query, vals)
    return {"message": "Item deleted successfully"}

def execute_query(connection, query, vals=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, vals)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
