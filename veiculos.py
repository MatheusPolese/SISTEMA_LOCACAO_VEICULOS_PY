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
        print("------------------------")
        for veiculo in  self.__lista_dos_veiculos:
            if veiculo.placa == id:
                print("------------------------")
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

class Veiculo:
    def __init__(self, placa, modelo, marca, ano: int, modalidade, precodiaria: int ):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__modalidade = modalidade##CNH A, B, C, D, E
        self.__precodiaria = precodiaria##definara o preço do aluguel
        self.__alugado = False
        self.__locatarioAtual = "Ninguem"
    

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

    @property
    def precodiaria(self):
        return self.__precodiaria

  