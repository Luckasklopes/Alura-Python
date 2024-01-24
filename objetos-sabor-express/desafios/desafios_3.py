#A
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return(f"O {self.profissao} {self.nome} tem {self.idade} anos")
    
    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        print(f"Bem vindo(a) {self.profissao} {self.nome}")


pessoa_Lucas = Pessoa("Lucas", 19, "Estagiario")

print(vars(pessoa_Lucas))

Pessoa.aniversario(pessoa_Lucas)

Pessoa.saudacao(pessoa_Lucas)

print(pessoa_Lucas)

#B
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return(f"{self.titular} tem R${self.saldo} em sua conta {self.ativo}")

    @classmethod
    def ativar_conta(cls, self):
        self.ativo = not self.ativo

titular_lucas = ContaBancaria("Lucas", 999.99)
titular_emy = ContaBancaria("Emily", 250.99)
ContaBancaria.ativar_conta(titular_emy)

print(titular_lucas)
print(titular_emy)

titular_pedro = ContaBancaria("Pedro", -50.00)
print(f"Quem deve 50 reais é o {titular_pedro.titular}")

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome2 = nome
        self.idade2 = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao2 = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

cliente_joao = ClienteBanco("Joao", 36, "Rua A", "123.456.789-01", "Backend")
cliente_maria = ClienteBanco("Maria", 22, "Rua B", "987.654.321-01", "Estudante")
cliente_jose = ClienteBanco("José", 18, "Rua C", "111.222.333-44", "Frontend")

cliente_ana = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de '{cliente_ana.titular}' com saldo de 'R${cliente_ana.saldo}' criada com sucesso")