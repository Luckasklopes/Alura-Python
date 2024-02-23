from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio): #importando dados de outra classe
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)#dizendo para o codigo que vou usar as funções do ItemCardapio
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        return(self._nome)
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.15