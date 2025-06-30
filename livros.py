class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

    def exibir_info(self):
        print(f"titulo: {self.titulo}, autor: {self.autor}, ano: {self.ano}, genero: {self.genero}")

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for item in self.livros:
            item.exibir_info()

    def buscar_por_autor(self, autor):
        for item in self.livros:
            if item.autor == autor:
                item.exibir_info()

    def buscar_por_titulo(self, titulo):
        for item in self.livros:
            if item.titulo == titulo:
                item.exibir_info()




livro1 = Livro("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Ficção")
livro3 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia")


biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)


biblioteca.listar_livros()

biblioteca.buscar_por_autor("Miguel de Cervantes")

biblioteca.buscar_por_titulo("O Hobbit")
