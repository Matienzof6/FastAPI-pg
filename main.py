from fastapi import FastAPI
from models.user_connection import UserConnection

app = FastAPI()
conn = UserConnection()

@app.get("/")
def root():
    conn
    return "Hi Im FastAPI"