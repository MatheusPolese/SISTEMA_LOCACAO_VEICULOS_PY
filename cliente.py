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
        for cliente in self.__lista_dos_clientes:
            if isinstance(cliente, Cliente_Fisico) and cliente.cpf == id:
                return cliente
            elif isinstance(cliente, Cliente_juridico) and cliente.cnpj == id:
                return cliente
            
        print("Este CPF não esta cadastrado, por favor realize o cadastro antes de alocar um veiculo!")
        return None

    def exibir_info(self, clienteinfo):
        print(f"|-----Ficha Cliente-----|")
        print(f"Nome: {clienteinfo.nome}")
        print(f"Documento: {clienteinfo.cpf}")
        print(f"quantos veiculos o cliente ja alugou: {clienteinfo.alugado}")
        print(f"|------------------------|")
    

from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = None
        self.email = email
        self.__alugado = 0
        
    @property
    def alugado(self):
        return self.__alugado
    
    @alugado.setter
    def alugado(self, status):
        if status == True:
            self.__alugado = self.__alugado + 1
        return self.__alugado

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, testeemail):
        if "@" in testeemail and testeemail.split("@")[1] == "gmail.com":
            self.__email = testeemail
        else:
            raise ValueError("E-mail inválido! O final precisa ser @gmail.com")
            


class Cliente_Fisico(Cliente):
    def __init__(self, nome, email, cpf):
        super().__init__(nome, email)
        self.__cpf = cpf
    
    @property
    def cpf(self):
        return self.__cpf

    def exibir_cliente(self):
        print(f"|-----Ficha Cliente-----|")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")        
        print(f"CPF: {self.__cpf}")
        print(f"|------------------------|")
    
class Cliente_juridico(Cliente):
    def __init__(self, nome, email, cnpj):
        super().__init__(nome, email)
        self.__cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj
    

    def exibir_cliente(self):
        print(f"|-----Ficha Cliente-----|")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")      
        print(f"CNPJ: {self.__cnpj}")
        print(f"|------------------------|")