import sqlite3

db = sqlite3.connect('data/prueba')

cursor = db.cursor()

cursor.execute('''CREATE TABLE usuario(id INTEGER PRIMARY KEY, nombre TEXT, telefono TEXT, email TEXT UNIQUE, password TEXT)''' )

db.commit()

    # nombre = input("nombre: ")
    # telefono = input("Telefono: ")
    # email = input("Email: ")
    # password = input("Password: ")

    # cursor.execute('''INSERT INTO usuario(nombre, telefono, email, password)
    #                VALUES(?,?,?,?)''',(nombre, telefono, email, password))

    # db.commit


db.close()
