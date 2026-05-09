from fastapi import FastAPI

app = FastAPI()

books = [
        "A Dança da Morte",
        "Carrie, a Estranha",
        "O Iluminado",
        "Salem",
        "It: A Coisa",
        "Mr. Mercedes",
        "Achados e Perdidos",
        "Boneco de Neve",
        "A Fundação",
        "Código Limpo"
]

# path parameters: fazem parte da URL (identificar recursos específicos... ex.: ID)
# query parameters: vêm após o ? (filtros, buscas, paginações, opções)

# rota raiz (informações da API)
@app.get("/")
def root():
    return {
            "message": "welcome to the Book's API!",
            "endpoints": {
                "/": "rota raiz.",
                "/books": "rota com operações sobre os livros.",
                "/books/{book_id}": "buscar livro pelo ID.",
                "/books/search/title": "saber se livro está presente pelo nome (opcional)."
            }
    }

# listar todo os livros
@app.get("/books")
def list_books():
    return {
            "total": len(books),
            "books": books
    }


# obter livro por ID (path parameter)
# fatsapi conta também com validação automática dos tipos de dados passados
@app.get("/books/{book_id}")
def get_book(book_id: int): # naturalmente, o nome do parâmetro deve ser o mesmo daquele presente na rota
    book_title = books[book_id]
    return {
            "book_title": book_title
    }


# saber se o livro está presente pelo nome em uma query (query parameter)
# ou seja, o nome do livro a ser buscado é um parâmetro opcional, diferente do path parameter
@app.get("/books/search/title")
def search_by_title(q: str = ""):
    # q vem de ?q=termo_busca
    # o = "" define um valor padrão
    book_exists = q in books
    return {
            "book_exists": book_exists
    }

# é possível também utilizar múltiplos parâmetros
# Ex.: filtar livros baseado em um ano mínimo e um ano máximo
# --------------
# @app.get("/livros/filtrar/ano")
# def filtrar_por_ano(ano_min: int = 2000, ano_max: int = 2024):
#     # Múltiplos parâmetros com valores padrão
#     ...
