from datetime import date
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Segurado(Base):
    __tablename__ = "segurado"
    cpf: Mapped[int] = mapped_column(primary_key=True)
    sexo: Mapped[str] = mapped_column(String(1))
    dataNascimento: Mapped[date]


class Produto(Base):
    __tablename__ = "produto"
    produtoId: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))


class Tabua(Base):
    __tablename__ = "tabua"
    tabuaId: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    tipo: Mapped[str] = mapped_column(String(50))


class Juros(Base):
    
    __tablename__ = "juros"
    jurosId: Mapped[int] = mapped_column(primary_key=True)
    juros: Mapped[float]


class ProdutoTabua(Base):
    __tablename__ = "produtotabua"
    produtoTabuaId: Mapped[int] = mapped_column(primary_key=True)
    produtoId: Mapped[int] = mapped_column(ForeignKey("produto.produtoId"))
    tabuaId: Mapped[int] = mapped_column(ForeignKey("tabua.tabuaId"))
    sexo: Mapped[str] = mapped_column(String(1))


class ProdutoJuros(Base):
    __tablename__ = "produtojuros"
    produtoJurosId: Mapped[int] = mapped_column(primary_key=True)
    produtoId: Mapped[int] = mapped_column(ForeignKey("produto.produtoId"))
    jurosId: Mapped[int] = mapped_column(ForeignKey("juros.jurosId"))
    prazoPagamento: Mapped[int]



class Matricula(Base):
    __tablename__ = "matricula"
    matriculaId: Mapped[int] = mapped_column(primary_key=True)
    cpfSegurado: Mapped[int] = mapped_column(ForeignKey("segurado.cpf"))
    produtoId: Mapped[int] = mapped_column(ForeignKey("produto.produtoId"))
    dataAssinatura: Mapped[date]
    dataInicioVigencia: Mapped[date]
    prazoCobertura: Mapped[int]
    prazoPagamento: Mapped[int]
