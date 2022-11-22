import mysql.connector as bbdd
from Scraping import *

def insertar_datos():

    lista_perros = web_scraping()


    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="webscraping",
                            user="root",
                            password="1234",
                            autocommit=True)

    cursor = conexion.cursor()

    cursor.execute("delete from webscraping where id is not null")

    cursor.execute("alter table webscraping auto_increment=1")

    script_insert ="insert into webscraping (imagen, nombre, precio, marca)" "values (%s, %s, %s, %s)"

    for perro in lista_perros:

        cursor.execute(script_insert, (perro["imagen"],
                                       perro["nombre"],
                                       perro["precio"],
                                       perro["marca"]))

    print("Datos insertados correctamente")


def consultar_datos():

    #Abrir conexión
    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="webscraping",
                            user="root",
                            password="1234",
                            autocommit=True)

    #Lista
    lista_perros = []

    #Abrir cursor
    cursor = conexion.cursor()

    #Script de bd
    consulta = "select * from webscraping"

    #Ejecuta la consulta
    cursor.execute(consulta)


    for dato in cursor.fetchall():
        perro = tuple([dato[0], dato[2], dato[3], dato[4]])

        lista_perros.append(perro)
    return lista_perros
    print("Datos Consultados")

consultar_datos()