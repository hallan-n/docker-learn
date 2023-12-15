from fastapi import FastAPI
import mysql.connector

app = FastAPI()


@app.get("/")
def try_conn():
    resp = get_conn()
    return {"message": resp}


def get_conn():
    try:
        _create_db()
        mysql.connector.connect(
            host="172.21.0.3",
            user="root",
            password="123456",
            database="db_teste",
        )
        return "Conectou no banco"
    except:
        return "Não conectou no banco"


def _create_db():
    try:
        mydb = mysql.connector.connect(
            host="172.21.0.3", user="root", password="123456"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS db_teste")
    except:
        raise Exception("Erro ao criar o banco")
