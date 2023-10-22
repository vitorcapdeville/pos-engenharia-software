from datetime import date
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session
from modelo import (
    Base,
    ProdutoPrazo,
    Segurado,
    Produto,
    Tabua,
    Juros,
    ProdutoTabua,
    Matricula,
)


engine = create_engine("sqlite:///seguros.sqlite", echo=True)


def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute("pragma foreign_keys=ON")


from sqlalchemy import event

event.listen(engine, "connect", _fk_pragma_on_connect)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    segurado = Segurado(cpf=12345678900, sexo="M", dataNascimento=date(1990, 1, 1))
    
    produtos = [
        Produto(produtoId=1, nome="Peculio por morte"),
        Produto(produtoId=2, nome="Outro peculio por morte")
    ]

    tabuas = [
        Tabua(tabuaId=1, nome="AT-2000", tipo="Morte"),
        Tabua(tabuaId=2, nome="BREMS MT M", tipo="Morte"),
        Tabua(tabuaId=3, nome="BREMS MT F", tipo="Morte")
    ]

    produto_tabua = [
        ProdutoTabua(produtoId=1, sexo = "M", tabuaId=1),
        ProdutoTabua(produtoId=1, sexo = "F", tabuaId=1),
        ProdutoTabua(produtoId=2, sexo = "M", tabuaId=2),
        ProdutoTabua(produtoId=2, sexo = "F", tabuaId=3),
    ]


    juros = [
        Juros(jurosId=1, juros=0.02),
        Juros(jurosId=2, juros=0.04),
        Juros(jurosId=3, juros=0.06),
    ]

    produto_prazo = [
        ProdutoPrazo(produtoId=1, prazoPagamento=10, prazoCobertura=10, jurosId=1),
        ProdutoPrazo(produtoId=1, prazoPagamento=20, prazoCobertura=20, jurosId=2),
        ProdutoPrazo(produtoId=1, prazoPagamento=30, prazoCobertura=30, jurosId=3),
        ProdutoPrazo(produtoId=2, prazoPagamento=15, prazoCobertura=15, jurosId=1),
        ProdutoPrazo(produtoId=2, prazoPagamento=30, prazoCobertura=30, jurosId=3),
    ]
    

    matricula = [
        Matricula(
            matriculaId=1,
            cpfSegurado=12345678900,
            produtoId=1,
            dataAssinatura=date(2020, 1, 1),
            dataInicioVigencia=date(2020, 2, 1),
            prazoCobertura = 10,
            prazoPagamento = 10,
        ),
        Matricula(
            matriculaId=2,
            cpfSegurado=12345678900,
            produtoId=2,
            dataAssinatura=date(2020, 1, 1),
            dataInicioVigencia=date(2020, 2, 1),
            prazoCobertura = 15,
            prazoPagamento = 15,
        ),
    ]

    session.add(segurado)
    session.commit()
    session.add_all(produtos)
    session.commit()
    session.add_all(tabuas)
    session.commit()
    session.add_all(produto_tabua)
    session.commit()
    session.add_all(juros)
    session.commit()
    session.add_all(produto_prazo)
    session.commit()
    session.add_all(matricula)
    session.commit()

# Testar se eu consigo fazer o join de query.sql usando ORM.