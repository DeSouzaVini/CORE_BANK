# CORE_BANK

> Sistema bancário desenvolvido com SQL Server e Python.

Projeto focado em modelagem relacional, administração SQL Server e integração entre Python e banco de dados.

---

## Tecnologias

* SQL Server
* T-SQL
* Python
* pyodbc
* python-dotenv

---

## Funcionalidades

* Cadastro de clientes
* Contas bancárias
* Controle de saldo
* Controle de limites
* Backup e Restore
* Fluxo transacional
* Integração Python + SQL Server

---

## Estrutura

```txt
CORE_BANK/
│
├── database/
│   ├── CORE_BANK.sql
│   ├── Manutencao_Backup.sql
│   └── Restauracao_banco_core.sql
│
├── docs/
│   └── DER_CORE_BANK.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Modelo Relacional

![DER](docs/DER_CORE_BANK.png)

---

## Instalação

### Clonar repositório

```bash
git clone https://github.com/DeSouzaVini/CORE_BANK.git
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configuração

Crie um arquivo `.env`:

```env
DB_SERVER=localhost\SQLEXPRESS
DB_NAME=CORE_BANK
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

---

## Scripts SQL

Execute os scripts:

```sql
CORE_BANK.sql
Manutencao_Backup.sql
Restauracao_banco_core.sql
```

---

## Conceitos Aplicados

* Modelagem Relacional
* Integridade Referencial
* Transactions
* Backup e Restore
* Administração SQL Server
* Integração Python + Banco de Dados

---

## Autor

Vinicius Martins
