from cliente import Cliente
from veiculos import Veiculo
class Aluguel:
    def __init__(self, cliente, veiculo):
        self.__cliente = cliente
        self.__veiculos = veiculo

    @property
    def cliente(self):
        self.__cliente.alugado = True

    @property
    def veiculos(self):
        self.__veiculos.alugado = True

