from cliente import Cliente
from veiculos import Veiculo
from datetime import datetime

class Aluguel:
    def __init__(self, veiculo, cliente, data_retirada, data_devolucao):
        self.__veiculo = veiculo
        self.__cliente = cliente
        self.__data_retirada = self.__validar_data(data_retirada)
        self.__data_devolucao = self.__validar_data(data_devolucao)
        self.__seguro = False


        if veiculo.alugado == True:
            print(f"Não é possivel alugar o veiculo, o {veiculo.modelo} ja esta alugado")
            return
        else:
            veiculo.alugado = True
            veiculo.locatarioAtual = cliente.nome
            cliente.alugado = True
            print(f"{veiculo.modelo} foi locado com sucesso por {cliente.nome}")
            ##verificar se carro ja esta alugado e mudar para cliente poder alugar 1 ou mais carros
    
    def __validar_data(self,data):
        try:
            dataFormatada = datetime.strptime(data, "%d/%m/%Y")
            return dataFormatada
        except ValueError:
            raise ValueError(f"Por favor digite uma data no padrão brasileiro dd/mm/aaaa")

    @property
    def data_retirada(self):
        return self.__data_retirada.strftime("%d/%m/%Y")
    
    @property
    def data_devolucao(self):
        return self.data_devolucao.strftime("%d/%m/%Y")  ##colocar para padrao brasileiro
    
    ##Adicionar função de agendar aluguel
    