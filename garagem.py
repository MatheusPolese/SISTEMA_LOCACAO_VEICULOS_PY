from veiculos import Veiculo

#classe para contar quantos carros estão dispo
class Garagem:
    def __init__(self):
        self.__lista_dos_veiculos = []


    def adiciona_veiculo(self, veiculo):
        self.__lista_dos_veiculos.append(veiculo)

    def mostrar_garagem(self):
        print("Lista de veiculos para aluguel:\n")
        for veiculo1 in  self.__lista_dos_veiculos:
            print(f"{veiculo.marca} {veiculo.modelo} - {veiculo.ano}")

        print("-----------------------------------------------------")
        

    

