#1
valor = int(input("digite um numero..: "))

if valor == 0:
    print(f"0 é par ou impar?")
elif valor % 2 == 0:
    print(f"o numero {valor} é par")
else:
    print(f"o numero {valor} é impar")

#2
idade = int(input("digite sua idade..: "))

if idade < 0:
    print(f"{valor} não é uma idade valida")
elif idade <= 12:
    print(f"com {idade} anos você é uma criança")
elif idade <= 18:
    print(f"com {idade} anos você é um adolescente")
else:
    print(f"com {idade} anos você ja é um adulto")

#3
email = "zezinho@gmail.com"
senha = "teste123123"

email_digitado = input("digite seu email..: ")
senha_digitada = input("digite sua senha..: ")

if email_digitado == email:
    if senha_digitada == senha:
        print("Logado com sucesso")
    else:
        print("senha incorreta")
else:
    print("email incorreto")

#4
x = int(input("digite as cordenadas x..: "))
y = int(input("digite as cordenadas y..: "))
if x > 0 and y > 0:
    print("você está no primeiro quadrante")
elif x < 0 and y > 0:
    print("você está no segundo quadrante")
elif x < 0 and y < 0:
    print("você está no terceiro quadrante")
elif x > 0 and y < 0:
    print("você está no quarto quadrante")
else:
    print("você está na origem")