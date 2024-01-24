class Restaurante:
    restaurantes = [] #lista de restaurantes
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self) #todo objeto criado entra na lista de restaurantes
    
    def __str__(self): # define um retorno especial ao chamar o nome do restaurantes
        return(f"{self._nome} | {self._categoria}")
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"NOME DO RESTAURANTE".ljust(20)} | {"CATEGORIA".ljust(20)} | {"STATUS".ljust(20)}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo.ljust(20)}")

    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("pizza express", "Italiano")

restaurantes = [restaurante_praca, restaurante_pizza]

Restaurante.listar_restaurantes()