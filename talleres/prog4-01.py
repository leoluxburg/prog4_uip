import pymysql

db = pymysql.connect("localhost", "root","","test")
cursor = db.cursor()

# newtable = "CREATE TABLE EMPLEADOS( NOMBRE VARCHAR(20) NOT NULL , APELLIDO VARCHAR(20) , EDAD INT , SEXO CHAR(1) ,SALARIO FLOAT)"
# cursor.execute(newtable)
# db.close()
# e = int(input("edad"))
# salarios = []
# sql = "SELECT * FROM EMPLEADOS WHERE EDAD > '%d'" % e
# try:
#   cursor.execute(sql)
#   resultado = cursor.fetchall()
#   for registro in resultados:
#     salario = registro[4]
#     salarios.append(salario)
# except:
#     print ("error")
# db.close()
# if len(salarios) > 0:
#   print ("salario alto $" + str(max(salarios)))
# else:
#   print ("somethingelse")

# name = input("Nombre")
# lastname = input("Apellido")
# age = input("Edad")
# sex = input("Sexo")
# salary = input("Salario")
# sql = """INSERT INTO EMPLEADOS(NOMBRE,APELLIDO,EDAD,SEXO,SALARIO)
# VALUES( %s, %s, %s ,%s, %s)"""
# cursor.execute(sql,(name, lastname, age, sex,salary ))
# db.commit()
# db.close()

# sql = "UPDATE EMPLEADOS SET EDAD = EDAD + 1 WHERE EDAD = 21"
# cursor.execute(sql)
# db.commit()
# db.close()

sql = "DELETE FROM EMPLEADOS WHERE EDAD < 22"
cursor.execute(sql)
db.commit()
db.close()
