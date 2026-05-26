class Veiculo:
    def __init__(self, placa, modelo, marca, ano, modalidade, categoria):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__modalidade = modalidade##CNH A, B, C, D, E
        self.__categoria = categoria##definara o preço do aluguel
        self.__alugado = False
    
    

    @property
    def alugado(self):
        return self.__alugado
    
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
    def categoria(self):
        return self.__categoria

