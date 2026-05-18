# Vira um "cliente" do seu banco e usa a sua Procedure.

import random
import uuid
from connect import get_connection

def simular_movimentacoes(ids_contas, total_transacoes):
    conn = get_connection()
    cursor = conn.cursor()
    aprovadas, recusadas = 0, 0

    for _ in range(total, transacoes):
        origem, destino = random.sample(ids_contas, 2)
        valor = round(random.uniform(50.0, 1000.0), 2)
        tipo = random.choice([1, 2, 3])# pix, ted, doc
        chave = str(uuid.uuid4())[:20] if tipo == 1 else None

        try :
            # Chama a procedure de transferência
            cursor.execute("{CALL PR_REALIZAR_TRANSFERENCIA (?, ?, ?, ?, ?)}",
                            (origem, destino, valor, tipo, chave))
            conn.commit()
            aprovadas += 1
        except Exception:
            conn. rollback()# Se a Procedure der THROW, ela cai aqui           
            recusadas += 1
    conn.close()
    return aprovadas, recusadas