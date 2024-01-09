import os

def exibir_logo():
    print(""""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def finalizar_app():
    os.system("cls")
    print("Finalizando o app\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção..: "))
    #opcao_escolhida = int(opcao_escolhida)

    #print("Você escolheu a opção", opcao_escolhida)
    #print(f"Você escolheu a opção {opcao_escolhida}")

    match opcao_escolhida:
        case 1:
            print("cadastrar restaurante")
        case 2:
            print("listar restaurantes")
        case 3:
            print("ativar restaurante")
        case 0:
            finalizar_app()
        case _:
            print("opção invalida")

#    if opcao_escolhida == 1:
#        print("cadastrar restaurante")
#    elif opcao_escolhida == 2:
#        print("Listar restaurantes")
#    elif opcao_escolhida == 3:
#        print("Ativar restaurante")
#    else:
#        finalizar_app()

def main():
    exibir_logo()
    exibir_opcoes()
    escolher_opcao()
    print("teste")
    
if __name__ == "__main__":
    main()