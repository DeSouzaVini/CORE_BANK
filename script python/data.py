from faker import Faker
import random 

fake = Faker('pt_BR')

def gerar_perfil_cliente():
    tipo_pessoa = random.choice([1, 2])

    if tipo_pessoa ==1:
        nome = fake.name()
        doc = fake.cpf(mask=False)
    else:
        nome = fake.company()
        doc = fake.cnpj(mask=False)

    return{

        "cliente":{
            "nome": nome,
            "documento": doc,
            "data_nascimento": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"),
            "tipo_pessoa": tipo_pessoa
        },

        "endereco":{
            "logradouro": fake.street_address(),
            "cep": fake.postcode().replace('-', ''),
            "cidade": fake.city(),
            "estado": fake.state_abbr()
        },

        "conta":{
            "agencia": f"{random.randint(1000, 9999)}",
            "numero_conta": f"{random.randint(100000, 999999)}-{random.randint(0, 9)}",
            "saldo_inicial": round(random.uniform(1000.0, 50000.0), 2),
            "status": 1
        },

        "limite":{
            "pix": round(random.uniform(500.0, 2000.0), 2),
            "credito": round(random.uniform(0.0, 5000.0), 2)
        }
    }