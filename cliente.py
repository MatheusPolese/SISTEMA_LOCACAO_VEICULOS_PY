class banco_clientes:
    def __init__(self):
        self.__lista_dos_clientes = []
        
    def adiciona_cliente(self, cliente):
        self.__lista_dos_clientes.append(cliente)

    def mostra_clientes(self):
        print("Lista de clientes:")
        print("------------------------")
        for cliente in  self.__lista_dos_clientes:
                print(f"| Cliente {cliente.nome} | Veiculos alugados {cliente.alugado}")
        print("------------------------")

    def procura_cliente(self, id):
        print("------------------------")
        for cliente in self.__lista_dos_clientes:
            if cliente.cpf == id:
                return cliente
            elif cliente.cnpj == id:
                return cliente
        print("Este CPF não esta cadastrado, por favor realize o cadastro antes de alocar um veiculo!")
        return 0
            

    def exibir_info(self, id):
        print("------------------------")
        for cliente in self.__lista_dos_clientes:
            if cliente.cpf == id:
                print(f"|-----Ficha Cliente-----|")
                print(f"Nome: {cliente.nome}")
                print(f"CPF: {cliente.cpf}")
                print(f"|------------------------|")
            elif cliente.cnpj == id:
                print(f"|-----Ficha Cliente-----|")
                print(f"Nome: {cliente.nome}")
                print(f"CPF: {cliente.cnpj}")
                print(f"|------------------------|")


from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, nome, cpf):
        self._nome = nome
        self._alugado = 0
        
    @property
    def alugado(self):
        return self._alugado
    
    @alugado.setter
    def alugado(self, status):
        if status == True:
            self._alugado = self._alugado + 1
        return self._alugado

    @property
    def nome(self):
        return self._nome
    
    @abstractmethod
    def exibir_cliente(self):
        pass
            


# 2. Definição da Subclasse (Classe Filha)
# Pessoa_Fisica herda de Pessoa
class Cliente_Fisico(Cliente):
    def __init__(self, nome, cpf):
        # Chama o construtor da classe pai (Pessoa) para inicializar nome e
        super().__init__(nome, cpf)
        # Adiciona um atributo específico da subclasse
        self.__cpf = cpf

    def exibir_cliente(self):
        print(f"|-----Ficha Cliente-----|")
        print(f"Nome: {self._nome}")
        print(f"CPF: {self._cpf}")
        print(f"Alugado: {self._alugado}")
        print(f"|------------------------|")

    @property
    def cpf(self):
        return self.__cpf
    
class Cliente_juridico(Cliente):
    def __init__(self, nome, cnpj):
        # Chama o construtor da classe pai (Pessoa) para inicializar nome e
        super().__init__(nome, cnpj)
        # Adiciona um atributo específico da subclasse
        self._cnpj = cnpj

    def exibir_cliente(self):
        print(f"|-----Ficha Cliente-----|")
        print(f"Nome: {self._nome}")
        print(f"CNPJ: {self._cnpj}")
        print(f"Alugado: {self._alugado}")
        print(f"|------------------------|")
    @property
    def cpf(self):
        return self.__cnpj
