class Livro:
    livros = [] #lista de livros
    def __init__(self, titulo, autor, ano_lancamento):
        self.titulo = titulo
        self.autor = autor
        self.ano_lancamento = ano_lancamento
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return(f"O livro {self.titulo} escrito por {self.autor} em {self.ano_lancamento} está {self.disponivel}")
    
    def emprestar(self):
        self.disponivel = not self.disponivel

    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_lancamento == ano and livro.disponivel]
        return livros_disponiveis
    
livro_teste1 = Livro("teste1", "autor1", 2004)
livro_teste2 = Livro("teste2", "autor2", 2004)
Livro.emprestar(livro_teste2)

print(livro_teste1)
print(livro_teste2)