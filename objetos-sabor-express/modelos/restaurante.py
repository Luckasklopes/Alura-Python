class Restaurante:
    restaurantes = [] #lista de restaurantes
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) #todo objeto criado entra na lista de restaurantes
    
    def __str__(self): # define um retorno especial ao chamar o nome do restaurantes
        return(f"{self.nome} | {self.categoria}")
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza express", "Italiano")

restaurantes = [restaurante_praca, restaurante_pizza]

Restaurante.listar_restaurantes()