import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    trusted = os.getenv('DB_TRUSTED_CONNECTION')

    dados_conexao = (
        f"Driver={{SQL Server}};"
        f"Server={server};"
        f"Database={database};"
        f"Trusted_Connection={trusted};"
    )
    
    return pyodbc.connect(dados_conexao)

try:
    conexao = get_connection()
    print('Conexão Bem Sucedida')
except Exception as e:
    print(f"ERRO! ao conectar: {e}")