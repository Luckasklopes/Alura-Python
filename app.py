import os

restaurantes = ["Pizza", "Sushi", "Massa"]


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
    print(subtitulo)
    print("\n\n")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("0. Sair\n")


def cadastrar_restaurante():
    subtitulo("Cadastro de restaurantes")
    nome_do_restaurante = input("digite o nome do restaurante..: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_menu()


def listar_restaurantes():
    subtitulo("Lista de restaurantes")

    for restaurante in restaurantes:
        print(f"- {restaurante}")

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
                print("ativar restaurante")
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