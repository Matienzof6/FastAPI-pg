from fastapi import FastAPI
from models.user_connection import UserConnection
from schema.user_schema import UserSchema
app = FastAPI()
conn = UserConnection()




@app.get("/")
def root():
    items = []
    for data in conn.read_all():  #el metodo read_all nos devuelve un array con los datos que solicitamos mediante la consulta sql, utilizamos el for para recorrelos y le agregamos el diccionario para mejorar el formato de lectura
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary) #Agregamos el diccionario creado a la lista vacia de items
    return items




@app.get("/api/user/{id}")
def get_one(id:str): #le añadimos el str porque es lo que recibe la base de datos
    dictionary = {}
    data = conn.read_one(id) 
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    return dictionary




@app.post("/api/insert")
def insert(user_data:UserSchema): #Con esta funcion usamos el UserSchema para que se puedan pasar solo los datos indicados en la clase UserSchema 
    data = user_data.dict() #Listamos los datos en un diccionaro
    data.pop("id") #Pasamos por alto el id
    conn.write(data) #Introducimos los valores dentro de la base de datos mediante la funcion write creada anteriormente




@app.delete("/api/delete/{id}")
def delete(id:str):
    conn.delete(id)
