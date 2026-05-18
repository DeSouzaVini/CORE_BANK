from connect import get_connection
from data import gerar_perfil_cliente

def executar(n_clientes, n_transacoes):
    print(f"---Fase 1: Criando{n_clientes} clientes e contas---")
    for i in range(n_clientes):
        perfil = gerar_perfil_cliente()
        inserir_fluxo_completo(perfil)
        if (i+1) % 50 == 0: print(f"{i+1} cadastro realizados...")
        print(f"\n---Fase 2: Simulando {n_transacoes} transferências---")
    contas = get_contas_ativas()
    ok, erro = simular_movimentacoes(contas, n_transacoes)
    print(f"Sucesso: {ok} transferências realizadas.")
    print(f"Bloqueado: {erro} (Saldo insuficiente ou regras do banco.)")

if __name__ == "__main__":
    executar(n_clientes=300, n_transacoes=1000)