import psycopg 

#Se instancia la clase Userconnection para conectarnos a la base de datos

class UserConnection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_maty user=postgres password=Ma22200118 host=localhost port=5432") # Le indicamos los datos de la base para conectarnos
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close() #En el caso de que haya algun error al conectar, se cierra la base de datos


    def __def__(self):  #Luego de ejecutar cualquier cosa dentro de la clase queremos cerrar la conexion a la base de datos
        self.conn.close()