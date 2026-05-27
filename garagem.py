from veiculos import Veiculo

#classe para contar quantos carros estão dispo
class Garagem:
    def __init__(self):
        self.__lista_dos_veiculos = []


    def adiciona_veiculo(self, veiculo):
        self.__lista_dos_veiculos.append(veiculo)

    def mostrar_garagem(self):
        print("Lista de veiculos para aluguel:\n")
        for veiculo in  self.__lista_dos_veiculos:
            if veiculo.alugado == False:
                print(f"{veiculo.marca} {veiculo.modelo} - {veiculo.ano}")
        print("-----------------------------------------------------")

    def mostrar_alugados(self):
        print("Lista de veiculos alugados:\n")
        for veiculo in  self.__lista_dos_veiculos:
            if veiculo.alugado == True:
                print(f"{veiculo.marca} {veiculo.modelo} - {veiculo.ano}")
        print("-----------------------------------------------------")

    

