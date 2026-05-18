from config import get_connection

def inserir_fluxo_completo(perfil):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Cliente
        cursor.execute("INSERT INTO TB_CLIENTE (NM_CLIENTE, NR_CPF_CNPJ, DT_NASCIMENTO, ID_TIPO_PESSOA_FK) OUTPUT INSERTED.ID_CLIENTE VALUES (?,?,?,?)", 
                       (perfil['cliente']['nome'], perfil['cliente']['documento'], perfil['cliente']['data_nascimento'], perfil['cliente']['tipo_pessoa']))
        id_cliente = cursor.fetchone()[0]

        # Endereço
        cursor.execute("INSERT INTO TB_ENDERECO (ID_CLIENTE, DS_LOGRADOURO, NR_CEP, NM_CIDADE, SG_ESTADO) VALUES (?,?,?,?,?)",
                       (id_cliente, perfil['endereco']['logradouro'], perfil['endereco']['cep'], perfil['endereco']['cidade'], perfil['endereco']['estado']))

        # Conta com Saldo
        cursor.execute("INSERT INTO TB_CONTA (ID_CLIENTE, NR_AGENCIA, NR_CONTA, VL_SALDO_ATUAL, ID_STATUS_CONTA) OUTPUT INSERTED.ID_CONTA VALUES (?,?,?,?,?)",
                       (id_cliente, perfil['conta']['agencia'], perfil['conta']['numero_conta'], perfil['conta']['saldo_inicial'], perfil['conta']['status']))
        id_conta = cursor.fetchone()[0]

        # Limite
        cursor.execute("INSERT INTO TB_LIMITE_CONTA (ID_CONTA, VL_LIMITE_PIX, VL_LIM_CREDITO) VALUES (?,?,?)",
                       (id_conta, perfil['limite']['pix'], perfil['limite']['credito']))

        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Erro: {e}")
        return False
    finally:
        conn.close()

def get_contas_ativas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID_CONTA FROM TB_CONTA WHERE ID_STATUS_CONTA = 1")
    ids = [row[0] for row in cursor.fetchall()]
    conn.close()
    return ids