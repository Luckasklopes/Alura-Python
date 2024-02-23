import os

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("Praça", "gourmet")
restaurante_praca.receber_avaliacao("Lucas", 6)
restaurante_praca.receber_avaliacao("Pedro", 6)
restaurante_praca.receber_avaliacao("Emy", 6)
restaurante_praca.receber_avaliacao("Joao", 11)

bebida_suco = Bebida("Suco de melancia", 5.00, "Grande")
bebida_suco.aplicar_desconto()
prato_paozinho = Prato("Pãozinho", 2.00, "O melhor pão da cidade")
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


restaurante_sushi = Restaurante("sushi", "japonesa")

def main():
    Restaurante.listar_restaurantes()
    #os.system("cls")
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()