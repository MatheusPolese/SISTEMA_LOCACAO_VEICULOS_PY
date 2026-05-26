from cliente import Cliente
from veiculos import Veiculo
class Aluguel:
    def __init__(self, veiculo, cliente):
        self.__comanda = f"{cliente.codigo}-xxx"
        self.__veiculo = veiculo
        self.__cliente = cliente

        veiculo.alugado = True
        cliente.alugado = True

    @property
    def comanda(self):
        return self.__comanda
    
    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def veiculo(self):
        return self.__veiculo
