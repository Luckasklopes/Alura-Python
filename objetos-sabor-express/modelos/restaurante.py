from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = [] #lista de restaurantes
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) #todo objeto criado entra na lista de restaurantes
    
    def __str__(self): # define um retorno especial ao chamar o nome do restaurantes
        return(f"{self._nome} | {self._categoria}")
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"NOME DO RESTAURANTE".ljust(20)} | {"CATEGORIA".ljust(20)} | {"AVALIAÇÃO".ljust(20)} | {"STATUS".ljust(20)}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo.ljust(20)}")

    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"
    
    def receber_avaliacao(self, cliente, nota):
        if nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return("Restaurante novo!!")
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media