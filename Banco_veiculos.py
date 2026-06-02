from veiculos import Veiculo
from aluguel import Aluguel

#classe para contar quantos carros estão dispo
class banco_veiculos:
    def __init__(self):
        self.__lista_dos_veiculos = []


    def adiciona_veiculo(self, veiculo):
        self.__lista_dos_veiculos.append(veiculo)

    def mostrar_garagem(self):
        print("Lista de veiculos para aluguel:")
        print("------------------------")
        for veiculo in  self.__lista_dos_veiculos:
            if veiculo.alugado == False:
                print(f"|{veiculo.marca} | {veiculo.modelo} - {veiculo.ano} | Disponivel para locação")
            if veiculo.alugado == True:
                print(f"|{veiculo.marca} | {veiculo.modelo} - {veiculo.ano} | Indisponivel para locação")
        print("------------------------")



    

