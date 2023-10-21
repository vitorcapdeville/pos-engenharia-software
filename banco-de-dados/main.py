from datetime import date
from esquema_carros_sqlalchemy import Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from gerar_dados_falsos import criar_dados

from esquema_carros_sqlalchemy import Automoveis, Revendedoras, Consumidores, Negocios, Garagens

engine = create_engine("sqlite:///carros.sqlite", echo=True)
def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')

from sqlalchemy import event
event.listen(engine, 'connect', _fk_pragma_on_connect)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

consumidor, revendedora, automovel, garagens, negocios = criar_dados(n_consumidores=10, n_revendedoras=2, n_automoveis=5, n_garagens=3, n_negocios=5)

consumidor = [Consumidores(**c) for c in consumidor]
revendedora = [Revendedoras(**r) for r in revendedora]
automovel = [Automoveis(**a) for a in automovel]
garagens = [Garagens(**g) for g in garagens]
negocios = [Negocios(**n) for n in negocios]

dados = (consumidor, revendedora, automovel, garagens, negocios)

for dado in dados:
    with Session(engine) as session:
        session.add_all(dado)
        session.commit()


with Session(engine) as session:
    query = select(Consumidores)
    ret = session.scalars(query).all()

ret

with Session(engine) as session:
    fakesell = Negocios(
        cpfComprador="000.000.000-00",
        cnpjRevenda="00.000.000/0000-00",
        codigoAutomovel=0,
        anoAutomovel="00",
        data=date(2021, 1, 1),
        preco=0.0,
    )
    session.add(fakesell)
    session.commit()


with Session(engine) as session:
    query = select(Negocios)
    ret = session.scalars(query).all()

ret