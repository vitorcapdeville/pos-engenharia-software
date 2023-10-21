SET SCHEMA 'carros';

CREATE TABLE carros.Automoveis (
    codigo integer NOT NULL,
    ano character(2) NOT NULL,
    fabricante character(20),
    modelo character(20),
    preco_tabela numeric(8,2),
    pais character(20)
);


CREATE TABLE carros.Revendedoras (
    cnpj character(18) NOT NULL,
    nome character(15),
    cpfProprietario character(12) NOT NULL,
    estado character(2)
);

CREATE TABLE carros.Consumidores (
    cpf character(12) NOT NULL,
    nome character(15),
    sobrenome character(15),
    dataNascimento DATE,
    estado character(2)
);

CREATE TABLE carros.Negocios (
    cpfComprador character(12) NOT NULL,
    cnpjRevenda character(18) NOT NULL,
    codigoAutomovel integer NOT NULL,
    anoAutomovel character(2) NOT NULL,
    data date,
    preco numeric(8,2),
);

CREATE TABLE carros.Garagens (
    cnpjRevenda character(18) NOT NULL,
    codigoAutomovel integer NOT NULL,
    anoAutomovel character(2) NOT NULL,
    quantidade integer,
);
