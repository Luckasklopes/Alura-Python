from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "gourmet")
restaurante_praca.receber_avaliacao("Lucas", 6)
restaurante_praca.receber_avaliacao("Pedro", 6)
restaurante_praca.receber_avaliacao("Emy", 6)
restaurante_praca.receber_avaliacao("Joao", 11)

restaurante_sushi = Restaurante("sushi", "japonesa")

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()