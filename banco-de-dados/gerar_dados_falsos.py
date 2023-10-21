from faker import Faker
import random
import pandas as pd

fake = Faker("pt_BR")



def criar_consumidor(fake: Faker):
    return {
        "cpf": fake.cpf(),
        "nome": fake.first_name(),
        "sobrenome": fake.last_name(),
        "dataNascimento": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "estado": fake.estado_sigla(),
    }


def criar_revendedora(fake: Faker, cpfProprietario):
    return {
        'cnpj': fake.cnpj(),
        'nome': fake.company(),
        'cpfProprietario': cpfProprietario,
        'estado': fake.estado_sigla(),
    }

def criar_automovel(fake: Faker):
    return {
        'codigo': fake.random_int(0, 50000),
        'ano': fake.year()[2:4],
        'fabricante': fake.company(),
        'modelo': fake.word(),
        'preco_tabela': fake.random_number(7, fix_len=True) / 100,
        'pais': fake.country(),
    }

def criar_negocios(
    fake: Faker, cpfComprador, cnpjRevenda, codigoAutomovel, anoAutomovel, preco_tabela
):
    return {
        'cpfComprador': cpfComprador,
        'cnpjRevenda': cnpjRevenda,
        'codigoAutomovel': codigoAutomovel,
        'anoAutomovel': anoAutomovel,
        'data': fake.date_object(),
        'preco': preco_tabela + fake.random_int(-100000, 100000) / 100,
    }

def criar_garagens(fake: Faker, cnpjRevenda, codigoAutomovel, anoAutomovel):
    return {
        'cnpjRevenda': cnpjRevenda,
        'codigoAutomovel': codigoAutomovel,
        'anoAutomovel': anoAutomovel,
        'quantidade': fake.random_int(0, 50),
    }


def criar_dados(
    n_consumidores: int,
    n_revendedoras: int,
    n_automoveis: int,
    n_negocios: int,
    n_garagens,
):
    consumidor = []
    revendedora = []
    automovel = []
    garagens = []
    negocios = []
    for _ in range(n_consumidores):
        consumidor += [criar_consumidor(fake)]
    for _ in range(n_revendedoras):
        consumidor_atual = random.choice(consumidor)
        revendedora += [criar_revendedora(fake, consumidor_atual["cpf"])]
    for _ in range(n_automoveis):
        automovel += [criar_automovel(fake)]
    for _ in range(n_garagens):
        revendedora_atual = random.choice(revendedora)
        automovel_atual = random.choice(automovel)
        garagens += [
            criar_garagens(
                fake,
                revendedora_atual["cnpj"],
                automovel_atual["codigo"],
                automovel_atual["ano"],
            )
        ]
    for _ in range(n_negocios):
        consumidor_atual = random.choice(consumidor)
        revendedora_atual = random.choice(revendedora)
        automovel_atual = random.choice(automovel)
        negocios += [
            criar_negocios(
                fake,
                consumidor_atual["cpf"],
                revendedora_atual["cnpj"],
                automovel_atual["codigo"],
                automovel_atual["ano"],
                automovel_atual["preco_tabela"],
            )
        ]

    consumidor = pd.DataFrame.from_records(consumidor).drop_duplicates(["cpf"]).to_dict(orient="records")
    revendedora = pd.DataFrame.from_records(revendedora).drop_duplicates(["cnpj"]).to_dict(orient="records")
    automovel = pd.DataFrame.from_records(automovel).drop_duplicates(["codigo", "ano"]).to_dict(orient="records")
    garagens = pd.DataFrame.from_records(garagens).drop_duplicates(["cnpjRevenda", "codigoAutomovel"]).to_dict(orient="records")
    negocios = pd.DataFrame.from_records(negocios).drop_duplicates(["cpfComprador", "cnpjRevenda", "codigoAutomovel", "anoAutomovel"]).to_dict(orient="records")
    
    return consumidor, revendedora, automovel, garagens, negocios
