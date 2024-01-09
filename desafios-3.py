#1
base_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ["lucas", "emily", "pedro", "ale"]
anos = [2004, 2024]

#2
for numeros in base_10:
    print(numeros)
print("")
for nome in nomes:
    print(nome)
print("")
for ano in anos:
    print(ano)

#3
numeros = 0
for i in range(1, 11):
    if i % 2 == 1:
        numeros += i
print("A soma dos numeros impares de 1 a 10 é ", numeros)

#4
for i in range(10, 0, -1):
    print(i)

#5
valor = int(input("digite um numero..: "))
for i in range(1, 10):
    resultado = valor*i
    print(f"{valor} x {i} = {resultado}")

#6
q_quatorze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
try:
    for impares in q_quatorze:
        total += impares
    print("A soma dos itens da lista é: ", total)
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#7
q_quinze = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
soma = 0
qnt = 0
for valores in q_quinze:
    soma += valores
    qnt += 1
print("A média dos pares de 0 a 20 é ", int(soma/qnt))