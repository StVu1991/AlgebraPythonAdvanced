import sqlite3

def create_topping(topping_data):
    try:
        conn = sqlite3.connect("pizza.db")
        cursor = conn.cursor()

        sql_select_topping = "SELECT topping FROM toppings WHERE topping LIKE(?)"
        topping_from_db = cursor.execute()
        for row in topping_from_db

        topping_from_db = cursor.execute(sql_select_topping, topping_data)

        if topping_from_db == topping_data:
            conn.close()
            return 1

        sql_create = "INSERT INTO toppings (topping) VALUES (?)"
        cursor.execute(sql_create, topping_data)

        conn.commit()
    except Exception as ex:
        print(f"")
    finally:


def update_data(sql_query: str, data: tuple)

