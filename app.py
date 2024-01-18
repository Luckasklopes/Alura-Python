import os

#dicionario = conjunto de dados
restaurantes = [{'nome':"Rio's", 'categoria':"pizza", 'ativo':True},
                {'nome':"Spoleto", 'categoria':"Italiana", 'ativo':True},
                {'nome':"Kyoto", 'categoria':"Sushi", 'ativo':False}]


def exibir_logo():
    """Essa função exibe a logo do aplicativo"""
    print(""""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)


def voltar_menu():
    """Essa função sempre retorna ao menu inicial"""
    input("\n\ndigite qualquer tecla para voltar ")
    main()


def finalizar_app():
    """Essa função fecha o app"""
    os.system("cls")
    print("aplicativo finalizado\n")


def opcao_invalida():
    """Essa função é executada ao tentar entrar uma opção invalida no menu"""
    print("opção invalida")
    voltar_menu()


def subtitulo(subtitulo):
    """Essa função é responsavel por exibir o subtitulo do menu atual
    Input:
    - nome do submenu
    
    Output:
    - submenu na tela com *
    """
    os.system("cls")
    linha = "*" * len(subtitulo)
    print(subtitulo)
    print(linha)
    print("\n")


def exibir_opcoes():
    """Essa função exibe as opções do menu inicial"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do  restaurante")
    print("0. Sair\n")


def cadastrar_restaurante():
    """Essa função é responsavel por cadastrar um restaurante no dicionario de dados
    Input:
    - nome do restaurante
    - categoria do restaurante
    
    Output:
    - novo restaurante no dicionario de dados
    """
    subtitulo("Cadastrando restaurante")
    nome_do_restaurante = input("digite o nome do restaurante..: ")
    categoria_do_restaurante = input(f"digite a categoria do restaurante {nome_do_restaurante}..: ")
    cadastro = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(cadastro)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_menu()


def listar_restaurantes():
    """Essa função é responsavel por listar os restaurantes presentes no dicionario de dados
    Output:
    - lista de restaurantes, suas categorias e estado de ativação
    """
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
    """Essa função é responsavel por alternar o estados dos restaurantes entre ativo ou não
    input:
    - nome do restaurante
    
    output:
    - estado do restaurante invertido(ativado -> desativado e vice-versa)
    """
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
    """Essa função é responsavel por receber a escolha do usuario sobre qual submenu abrir
    input:
    - opção desejada
    
    output:
    - submenu relacionado a opção desejada
    """
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
    """Essa é a função main do nosso aplicativo"""
    os.system("cls")
    exibir_logo()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == "__main__":
    """não faço ideia do que essa função faz"""
    main()