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

    def write(self, data):
        with self.conn.cursor() as cur: #Con el with creamos un contexto en el cual va a estar funcionando la base de datos, el cual terminara la conexion al dejar de usarlo, para eso se usa el contexto
            cur.execute("""
                INSERT INTO "user"(name, phone) VALUES(%(name)s, %(phone)s)
            """, data) # Con estas lineas le decimos a nuesrta base de datos que queremos insertar datos en los camos name y phone de user con los valores que le pasamos mediante %()s el diccionario que contiene el parametro data 
        self.conn.commit()





    def __def__(self):  #Luego de ejecutar cualquier cosa dentro de la clase queremos cerrar la conexion a la base de datos
        self.conn.close()