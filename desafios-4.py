#1
pessoa = {'nome': "Lucas", 'idade': 20, 'cor': "azul"}

#2
pessoa['idade'] = 31

del pessoa['cor']

pessoa['profissao'] = "estagiario"

#3
x = 0
for x in range(0, 5):
    x+=1
    print(f"o quadrado de {x} é", x*x)

#4
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

#5
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
