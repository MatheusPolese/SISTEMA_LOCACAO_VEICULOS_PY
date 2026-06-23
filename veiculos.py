class banco_veiculos:
    def __init__(self):
        self.__lista_dos_veiculos = []

    def procura_veiculo(self, num):
        i = 0
        for veiculo in  self.__lista_dos_veiculos:
            i+=1
            if i == num:
                return veiculo

    def adiciona_veiculo(self, veiculo):
        self.__lista_dos_veiculos.append(veiculo)

    def mostrar_garagem(self):
        print("Lista de veiculos para aluguel:")
        print("------------------------")
        i = 1
        for veiculo in  self.__lista_dos_veiculos:
            print(f"[{i}]|Custo diaria: R$ {veiculo.precodiaria}|{veiculo.marca} {veiculo.modelo} {veiculo.ano} ")
            i+=1
        print("------------------------")
        return (i-1)

    def exibir_veiculo(self, id):
        for veiculo in  self.__lista_dos_veiculos:
            if veiculo.placa == id:
                print(f"|-----Ficha Veiculo-----|")
                print(f"Placa: {veiculo.placa}")
                print(f"Modelo: {veiculo.marca}")
                print(f"Modelo: {veiculo.modelo}")
                print(f"Ano: {veiculo.ano}")
                print(f"Modalidade: {veiculo.modalidade}")
                print(f"Preco diaria: R$ {veiculo.precodiaria}")
                print(f"Alugado: {veiculo.alugado}")
                print(f"Atual locatario: {veiculo.locatarioAtual}")
                print(f"|------------------------|")  
                
from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, placa, modelo, marca, ano: int, modalidade ):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__modalidade = modalidade##CNH A, B, C, D, E
        self.__alugado = False
        self.__locatarioAtual = "Ninguem"
    
    @abstractmethod
    def diaria(self):
        pass

    @property
    def precodiaria(self):
        return self.diaria()

    @property
    def alugado(self):
        return self.__alugado
    
    @property
    def locatarioAtual(self):
        return self.__locatarioAtual

    @locatarioAtual.setter
    def locatarioAtual(self, novocliente):
        self.__locatarioAtual = novocliente
    
    @alugado.setter
    def alugado(self, status):
        self.__alugado = status

    @property
    def placa(self):
        return self.__placa
    
    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def modalidade(self):
        return self.__modalidade


    def exibir_veiculo(self):
            print(f"|-----Ficha Veiculo-----|")
            print(f"Placa: {self.__placa}")
            print(f"Marca: {self.__marca}")
            print(f"Modelo: {self.__modelo}")
            print(f"Ano: {self.__ano}")
            print(f"Modalidade: {self.__modalidade}")
            print(f"Preço Diária: R$ {self.precodiaria:.2f}")  # Pega o valor correto da subclasse
            print(f"Alugado: {self.__alugado}")
            print(f"Atual locatario: {self.__locatarioAtual}")
            print(f"|------------------------|")

class CarroEconomico(Veiculo):
    def diaria(self):
        return 120.00
    
class CarroSUV(Veiculo):
    def diaria(self):
        return 250.00
    
class VAN(Veiculo):
    def diaria(self):
        return 500.00
    

class CriadorVeiculo(ABC):
    @abstractmethod
    def addveiculo(self, placa, modelo, marca, ano, modalidade) -> Veiculo:
        pass


class CriadorEconomico(CriadorVeiculo):
    def addveiculo(self, placa, modelo, marca, ano, modalidade):
        return CarroEconomico(placa, modelo, marca, ano, modalidade)

class CriadorSUV(CriadorVeiculo):
    def addveiculo(self, placa, modelo, marca, ano, modalidade):
        return CarroSUV(placa, modelo, marca, ano, modalidade)

class CriadorVAN(CriadorVeiculo):
    def addveiculo(self, placa, modelo, marca, ano, modalidade):
        return VAN(placa, modelo, marca, ano, modalidade)
    


garagem = banco_veiculos()

# Usando as fábricas para criar os veículos (Sem passar o preço manualmente)
fabrica_suv = CriadorSUV()
suv = fabrica_suv.addveiculo("ABC-1234", "Compass", "Jeep", 2024, "B")

fabrica_van = CriadorVAN()
van = fabrica_van.addveiculo("XYZ-9876", "備Transit", "Ford", 2025, "D")

# Adicionando na garagem
garagem.adiciona_veiculo(suv)
garagem.adiciona_veiculo(van)

# Mostrando os veículos com seus preços definidos pelas subclasses
garagem.mostrar_garagem()