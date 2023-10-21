from datetime import date
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session
from modelo import (
    Base,
    Segurado,
    Produto,
    Tabua,
    Juros,
    ProdutoTabua,
    ProdutoJuros,
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
    produto = Produto(produtoId=1, nome="Peculio por morte")

    tabua1 = Tabua(tabuaId=1, nome="AT-2000", tipo="Morte")

    produto_tabua1 = ProdutoTabua(produtoTabuaId=1, produtoId=1, sexo = "M", tabuaId=1)
    produto_tabua2 = ProdutoTabua(produtoTabuaId=2, produtoId=1, sexo = "F", tabuaId=1)

    juros1 = Juros(jurosId=1, juros=0.02)
    juros2 = Juros(jurosId=2, juros=0.04)
    juros3 = Juros(jurosId=3, juros=0.06)

    produto_juros1 = ProdutoJuros(produtoJurosId=1, prazoPagamento=10, produtoId=1, jurosId=1)
    produto_juros2 = ProdutoJuros(produtoJurosId=2, prazoPagamento=20, produtoId=1, jurosId=2)
    produto_juros3 = ProdutoJuros(produtoJurosId=3, prazoPagamento=30, produtoId=1, jurosId=3)

    matricula = Matricula(
        matriculaId=1,
        cpfSegurado=12345678900,
        produtoId=1,
        dataAssinatura=date(2020, 1, 1),
        dataInicioVigencia=date(2020, 2, 1),
        prazoCobertura=10,
        prazoPagamento=10,
    )

    session.add(segurado)
    session.commit()
    session.add(produto)
    session.commit()
    session.add_all([tabua1])
    session.commit()
    session.add_all([produto_tabua1, produto_tabua2])
    session.commit()
    session.add_all([juros1, juros2, juros3])
    session.commit()
    session.add_all([produto_juros1, produto_juros2, produto_juros3])
    session.commit()
    session.add(matricula)
    session.commit()

# with engine.connect() as con:
#     con.execute(
#         text("select dataNascimento, dataAssinatura, dataInicioVigencia, prazoCobertura ")
#     )