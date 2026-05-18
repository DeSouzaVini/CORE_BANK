import pandas as pd
from core_bank_fake.config import get_connection

def visualizar_resumo_banco():
    conn = get_connection()
    
    print("--- 1. ÚLTIMAS 10 TRANSAÇÕES (VIA VIEW) ---")
    query_extrato = "SELECT TOP 10 * FROM VW_EXTRATO_DETALHADO ORDER BY [Data/Hora] DESC"
    df_extrato = pd.read_sql(query_extrato, conn)
    print(df_extrato)
    print("\n")

    print("--- 2. TOP 5 MAIORES SALDOS ---")
    query_saldos = """
        SELECT TOP 5 C.NM_CLIENTE, ACC.VL_SALDO_ATUAL 
        FROM TB_CONTA ACC
        INNER JOIN TB_CLIENTE C ON ACC.ID_CLIENTE = C.ID_CLIENTE
        ORDER BY ACC.VL_SALDO_ATUAL DESC
    """
    df_saldos = pd.read_sql(query_saldos, conn)
    print(df_saldos)
    
    conn.close()

if __name__ == "__main__":
    visualizar_resumo_banco()


