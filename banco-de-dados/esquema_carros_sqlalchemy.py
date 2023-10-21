from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import date


class Base(DeclarativeBase):
    pass


class Automoveis(Base):
    __tablename__ = "automoveis"

    codigo: Mapped[int] = mapped_column(primary_key=True)
    ano: Mapped[str] = mapped_column(String(2), primary_key=True)
    fabricante: Mapped[str] = mapped_column(String(20))
    modelo: Mapped[str] = mapped_column(String(50))
    preco_tabela: Mapped[float]
    pais: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f"<Automoveis(codigo={self.codigo}, ano={self.ano}, fabricante={self.fabricante}, modelo={self.modelo}, preco_tabela={self.preco_tabela}, pais={self.pais})>"


class Revendedoras(Base):
    __tablename__ = "revendedoras"

    cnpj: Mapped[str] = mapped_column(String(18), primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    cpfProprietario: Mapped[str] = mapped_column(ForeignKey("consumidores.cpf"))
    estado: Mapped[str] = mapped_column(String(2))

    def __repr__(self):
        return f"<Revendedoras(cnpj={self.cnpj}, nome={self.nome}, cpfProprietario={self.cpfProprietario}, estado={self.estado})>"


class Consumidores(Base):
    __tablename__ = "consumidores"

    cpf: Mapped[str] = mapped_column(String(14), primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    sobrenome: Mapped[str] = mapped_column(String(50))
    dataNascimento: Mapped[date]
    estado: Mapped[str] = mapped_column(String(2))

    def __repr__(self):
        return f"<Consumidores(cpf={self.cpf}, nome={self.nome}, sobrenome={self.sobrenome}, dataNascimento={self.dataNascimento}, estado={self.estado})>"


class Negocios(Base):
    __tablename__ = "negocios"

    cpfComprador: Mapped[str] = mapped_column(
        ForeignKey("consumidores.cpf"), primary_key=True
    )
    cnpjRevenda: Mapped[str] = mapped_column(
        ForeignKey("revendedoras.cnpj"), primary_key=True
    )
    codigoAutomovel: Mapped[int] = mapped_column(primary_key=True)
    anoAutomovel: Mapped[str] = mapped_column(primary_key=True)
    __table_args__ = (
        ForeignKeyConstraint(
            [codigoAutomovel, anoAutomovel], [Automoveis.codigo, Automoveis.ano]
        ),
        {},
    )
    data: Mapped[date]
    preco: Mapped[float]

    def __repr__(self):
        return f"<Negocios(cpfComprador={self.cpfComprador}, cnpjRevenda={self.cnpjRevenda}, codigoAutomovel={self.codigoAutomovel}, anoAutomovel={self.anoAutomovel}, data={self.data}, preco={self.preco})>"


class Garagens(Base):
    __tablename__ = "garagens"

    cnpjRevenda: Mapped[str] = mapped_column(
        ForeignKey("revendedoras.cnpj"), primary_key=True
    )
    codigoAutomovel: Mapped[int] = mapped_column(primary_key=True)
    anoAutomovel: Mapped[str] = mapped_column(primary_key=True)
    quantidade: Mapped[int]

    __table_args__ = (
        ForeignKeyConstraint(
            [codigoAutomovel, anoAutomovel], [Automoveis.codigo, Automoveis.ano]
        ),
        {},
    )

    def __repr__(self):
        return f"<Garagens(cnpjRevenda={self.cnpjRevenda}, codigoAutomovel={self.codigoAutomovel}, anoAutomovel={self.anoAutomovel}, quantidade={self.quantidade})>"
