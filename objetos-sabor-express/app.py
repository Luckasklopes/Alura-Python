from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "gourmet")
restaurante_praca.receber_avaliacao("Lucas", 9)
restaurante_praca.receber_avaliacao("Pedro", 6)
restaurante_praca.receber_avaliacao("Emy", 10)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()