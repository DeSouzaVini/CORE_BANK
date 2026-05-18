import pyodbc
import os

from dotenv import load_dotenv

load_dotenv()


def get_connection():

    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    conn_str = (
        "Driver={SQL Server};"
        f"Server={server};"
        f"Database={database};"
        f"UID={user};"
        f"PWD={password};"
    )

    try:

        conn = pyodbc.connect(conn_str)

        print("Conexão estabelecida com sucesso!")

        return conn

    except Exception as e:

        print(f"Erro ao conectar: {e}")

        return None