from enum import Enum


class Autor:
    def __init__(self, nome_completo: str, nome_citacao: str, afiliacao: str) -> None:
        self._nome_completo = nome_completo
        self._nome_citacao = nome_citacao
        self._afiliacao = afiliacao

    @property
    def nome_completo(self):
        return self._nome_completo

    @property
    def nome_citacao(self):
        return self._nome_citacao

    @property
    def afiliacao(self):
        return self._afiliacao

    def __eq__(self, __value: "Autor") -> bool:
        return (
            self._nome_completo == __value.nome_completo
            and self._nome_citacao == __value.nome_citacao
            and self._afiliacao == __value.afiliacao
        )


class Artigo:
    def __init__(self, titulo: str, autores: list[Autor], ano_publicacao: int) -> None:
        self._verificar_autores_duplicados(autores)
        self._titulo = titulo
        self._autores = autores
        self._ano_publicacao = ano_publicacao

    def _verificar_autores_duplicados(self, autores: list[Autor]):
        for autor in autores:
            if autores.count(autor) > 1:
                raise ValueError(
                    f"O autor '{autor.nome_completo}' está repetido na lista de autores."
                )

    def _nomes_citacao(self):
        return ", ".join([autor.nome_citacao for autor in self._autores])

    @property
    def titulo(self):
        return self._titulo

    @property
    def autores(self):
        return self._autores

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    def __str__(self):
        return f"{self._nomes_citacao()}, {self.titulo}, {self.ano_publicacao}."

    def __eq__(self, other: "Artigo") -> bool:
        if len(self._autores) != len(other.autores):
            return False
        return (
            self._titulo == other.titulo
            and all(
                [este == outro for este, outro in zip(self._autores, other.autores)]
            )
            and self._ano_publicacao == other.ano_publicacao
        )


class Tema(Enum):
    COMPUTACAO = "Computação"
    FISICA = "Física"
    MATEMATICA = "Matemática"


def imprimir_artigos(artigos: list[Artigo], tema: Tema) -> None:
    if len(artigos) == 0:
        print(f"=== Nenhum artigo publicado sob o tema '{tema.value}'.")
        return

    print(f"=== Artigos publicados com o tema '{tema.value}':")
    for artigo in artigos:
        print("  * ", end="")
        print(artigo)

class Biblioteca:
    def __init__(self) -> None:
        self._artigos = {Tema.COMPUTACAO: [], Tema.FISICA: [], Tema.MATEMATICA: []}

    def publicar_artigo(self, artigo: Artigo, tema: Tema) -> None:
        if self._artigos[tema].count(artigo) != 0:
            raise ValueError(f"O artigo '{artigo.titulo}' já existe nesta biblioteca sob o tema {tema.value}.")
        self._artigos[tema].append(artigo)
        print(f"*** Artigo '{artigo.titulo}' publicado com sucesso sob o tema '{tema.value}'!")

    def imprimir_artigos(self) -> None:
        for tema in self._artigos.keys():
            imprimir_artigos(self._artigos[tema], tema)
