import os

#dicionario = conjunto de dados
restaurantes = [{'nome':"Rio's", 'categoria':"pizza", 'ativo':True},
                {'nome':"Spoleto", 'categoria':"Italiana", 'ativo':True},
                {'nome':"Kyoto", 'categoria':"Sushi", 'ativo':False}]


def exibir_logo():
    print(""""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)


def voltar_menu():
    input("\n\ndigite qualquer tecla para voltar ")
    main()


def finalizar_app():
    os.system("cls")
    print("aplicativo finalizado\n")


def opcao_invalida():
    print("opção invalida")
    voltar_menu()


def subtitulo(subtitulo):
    os.system("cls")
    linha = "*" * len(subtitulo)
    print(subtitulo)
    print(linha)
    print("\n")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do  restaurante")
    print("0. Sair\n")


def cadastrar_restaurante():
    subtitulo("Cadastrando restaurante")
    nome_do_restaurante = input("digite o nome do restaurante..: ")
    categoria_do_restaurante = input(f"digite a categoria do restaurante {nome_do_restaurante}..: ")
    cadastro = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(cadastro)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_menu()


def listar_restaurantes():
    subtitulo("Listando restaurantes")
    print(f"{"- NOME".ljust(17)} | {"CATEGORIA".ljust(15)} | {"ESTADO".ljust(15)}")
    print("-" * 49)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        estado_restaurante = "ativado" if restaurante['ativo'] else "desativado"
        print(f"- {nome_restaurante.ljust(15)} | {categoria_restaurante.ljust(15)} | {estado_restaurante.ljust(15)}")

    voltar_menu()


def alternar_estado_restaurante():
    subtitulo("Alternando estado dos restaurantes")
    nome_restaurante = input("Nome do restaurante a ser ativado/desativado..:")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #inverte o estado, se for ativo desativa e viceversa
            if restaurante['ativo'] == True:
                estado = "Ativado"
            else:
                estado = "Desativado"
            print(f"O restaurante {nome_restaurante} foi {estado} com sucesso!")
    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} nao foi encontrado")

    voltar_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção..: "))
        #opcao_escolhida = int(opcao_escolhida)

        #print("Você escolheu a opção", opcao_escolhida)
        #print(f"Você escolheu a opção {opcao_escolhida}")

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 0:
                finalizar_app()
            case _:
                opcao_invalida()

    #    if opcao_escolhida == 1:
    #        print("cadastrar restaurante")
    #    elif opcao_escolhida == 2:
    #        print("Listar restaurantes")
    #    elif opcao_escolhida == 3:
    #        print("Ativar restaurante")
    #    else:
    #        finalizar_app()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_logo()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == "__main__":
    main()