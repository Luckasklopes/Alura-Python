from modelos.avalilacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = [] #lista de restaurantes
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
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
    
#    def adicionar_bebida_no_cardapio(self, bebida):
#        self._cardapio.append(bebida)
#
#    def adicionar_prato_no_cardapio(self, prato):
#        self._cardapio.append(prato)
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): #verdadeiro se o item for uma instancia, ou derivado da classe itemcardapio
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, "descricao"):
                print(f"{i}. nome:{item._nome} | preço: R${item._preco} | descrição: {item.descricao}")
            elif hasattr(item, "tamanho"):
                print(f"{i}. nome:{item._nome} | preço: R${item._preco} | tamanho: {item.tamanho}")
