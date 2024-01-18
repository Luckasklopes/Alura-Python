#A
class Musica:
    nome = ""
    artista = ""
    duracao = 0.0

musica_high_hopes = Musica()
musica_high_hopes.nome = "High Hopes"
musica_high_hopes.artista = "Panic!"
musica_high_hopes.duracao = 3.50

musicas = [musica_high_hopes]

print(vars(musica_high_hopes))

#B
class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet"
restaurante_praca.ativo = True

#1
restaurante_praca.categoria = "Italiana"

#2
nome_restaurante = restaurante_praca.nome
print(f"{restaurante_praca.nome}")

#3
if restaurante_praca.ativo == True:
    print("o restaurante está ativo")
else:
    print("o restaurante nao está ativo")

#4
Categoria = Restaurante.categoria

#5
restaurante_praca.nome = "Bistrô"

#6
restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza place"
restaurante_pizza.categoria = "Fast food"

#7
print(restaurante_pizza.categoria)

#8
restaurante_pizza.ativo = True

#9
print(f"{restaurante_praca.nome}, {restaurante_praca.categoria}")