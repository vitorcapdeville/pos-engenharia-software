from biblioteca_artigos import Autor, Biblioteca, Tema
from biblioteca_artigos import Artigo

bib = Biblioteca()

jsilva = Autor("José da Silva", "SILVA, J.", "UFRJ")
fdias = Autor("Fátima Dias", "DIAS, F.", "UFF")

artigo1 = Artigo("Um artigo com um nome grande", [jsilva], 2021)
artigo2 = Artigo("Um artigo com um nome maior ainda", [fdias, jsilva], 2023)

bib.imprimir_artigos()

bib.publicar_artigo(artigo1, Tema.COMPUTACAO)
bib.publicar_artigo(artigo2, Tema.FISICA)


try:
    bib.publicar_artigo(artigo1, Tema.MATEMATICA)
    bib.publicar_artigo(artigo1, Tema.COMPUTACAO)
except ValueError as erro:
    print(erro)

try:
    Artigo(
        "Um artigo com um nome maior ainda",
        [
            Autor("Fátima Dias", "DIAS, F.", "UFF"),
            Autor("Fátima Dias", "DIAS, F.", "UFF"),
        ],
        2023,
    )
except ValueError as erro:
    print(erro)

bib.imprimir_artigos()
