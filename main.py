from fastapi import FastAPI
from models.user_connection import UserConnection
from schema.user_schema import UserSchema
app = FastAPI()
conn = UserConnection()

@app.get("/")
def root():
    conn
    return "Hi Im FastAPI"


@app.post("/api/insert")
def insert(user_data:UserSchema): #Con esta funcion usamos el UserSchema para que se puedan pasar solo los datos indicados en la clase UserSchema 
    data = user_data.dict() #Listamos los datos en un diccionaro
    data.pop("id") #Pasamos por alto el id
    conn.write(data) #Introducimos los valores dentro de la base de datos mediante la funcion write creada anteriormente