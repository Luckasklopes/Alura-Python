#A
class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def __str__(self):
        return(f"{self.nome}({self.duracao}) by {self.artista}")
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome}({musica.duracao}) by {musica.artista}")

musica_high_hopes = Musica("High Hopes", "Panic!", 3.50)
musica_meu_amor = Musica("Meu amor", "O Grilo", 3.20)

Musica.listar_musicas()

#B
#1
class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def listar_carros():
        for carro in Carro.carros:
            print(f"\nSeu carro é um {carro.modelo} {carro.ano} {carro.cor}\n")

carro_astra = Carro("Astra", "Branco", 2011)

Carro.listar_carros()

#2
class Restaurante:
    restaurantes = []
    #3
    def __init__(self, nome, categoria, ativo, cidade, retirada):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.cidade = cidade
        self.retirada = True
        Restaurante.restaurantes.append(self)
    #4
    def __str__(self):
        ativado = "ativado" if self.ativo == True else "desativado"
        print("\nATIVO? | NOME | CATEGORIA | CIDADE | RETIRADA?")
        return(f"{ativado} | {self.nome} | {self.categoria} | {self.cidade} | {self.retirada}")

restaurante_pizza = Restaurante("Agua na boca", "pizza", True, "Rio branco", True)

print(vars(restaurante_pizza))

print(restaurante_pizza)

#5
class Cliente:
    clientes = []
    def __init__(self, nome, idade, cor, profissao):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.profissao = profissao
        Cliente.clientes.append(self)
    
    def listar_clientes():
        print("\nCLIENTE / IDADE / COR / PROFISSAO")
        for cliente in Cliente.clientes:
            print(f"{cliente.nome} / {cliente.idade} /{cliente.cor} / {cliente.profissao}")

cliente_emily = Cliente("Emily", 19, "Branco", "Estudante")
cliente_pedro = Cliente("pedro", 19, "Pardo", "Estudante")
cliente_lucas = Cliente("Lucas", 20, "Branco", "Estagiario")

Cliente.listar_clientes()