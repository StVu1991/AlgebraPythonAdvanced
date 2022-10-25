import sqlite3

conn = sqlite3.connect("pizza.db")
cursor = conn.cursor()

sql_create_toppings = "CREATE TABLE toppings (id integer primary key, topping varchar(15) NOT NULL)"
sql_create_prices = "CREATE TABLE prices (product varchar(15) primary key, price decimal)"
cursor.execute(sql_create_toppings)
cursor.execute(sql_create_prices)

sql_insert_toppings = "INSERT INTO toppings (topping) VALUES (?)"
toppings = [
    ('Sausage',),
    ('Pepperoni',),
    ('Chickem',),
    ('Mushroom',),
    ('Black Olive',),
    ('Green Pepper',),
    ('Red Pepper',),
    ('Onion',)
]

cursor.executemany(sql_insert_toppings, toppings)

sql_insert_prices = "INSERT INTO prices (product, price) VALUES (?, ?)"
prices = {
    ("medium", 9.99),
    ("large", 12.99),
    ("x-large", 14.99),
    ("medium-toppings", 1.0),
    ("large-toppings", 1.5),
    ("x-large-toppings", 1.8)
}

cursor.executemany(sql_insert_prices, prices)

#sql_select = "SELECT * FROM prices"

#cursor_from_db = cursor.execute(sql_query)
#print(cursor_from_db)
conn.commit()
conn.close()