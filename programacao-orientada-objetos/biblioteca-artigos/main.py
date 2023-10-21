from biblioteca_artigos import Autor, Biblioteca
from biblioteca_artigos import Artigo

bib = Biblioteca()

jsilva = Autor("José da Silva", "SILVA, J.", "UFRJ")
fdias = Autor("Fátima Dias", "DIAS, F.", "UFF")

artigo1 = Artigo("Um artigo com um nome grande", [jsilva], 2021)
artigo2 = Artigo("Um artigo com um nome maior ainda", [fdias, jsilva], 2023)
# Impedir que um artigo tenha autores repetidos.

bib.imprimir_artigos()

bib.publicar_artigo(artigo1)
bib.publicar_artigo(artigo2)

bib.imprimir_artigos()

try:
    bib.publicar_artigo(artigo1)
except ValueError as erro:
    print(erro)

try:
    Artigo("Um artigo com um nome maior ainda", [Autor("Fátima Dias", "DIAS, F.", "UFF"), Autor("Fátima Dias", "DIAS, F.", "UFF")], 2023)
except ValueError as erro:
    print(erro)

