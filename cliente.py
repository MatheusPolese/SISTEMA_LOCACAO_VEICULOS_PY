class banco_clientes:
    def __init__(self):
        self.__lista_dos_clientes = []
        
    def adiciona_cliente(self, cliente):
        self.__lista_dos_clientes.append(cliente)

    def mostra_clientes(self):
        print("Lista de clientes:")
        print("------------------------")
        for cliente in  self.__lista_dos_clientes:
                print(f"| {cliente.cpf} | Cliente {cliente.nome} | Veiculos alugados {cliente.alugado}")
        print("------------------------")


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
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
    def cpf(self):
        return self.__cpf
    

    def exibir_cliente(self):
        print(f"|-----Ficha Cliente-----|")
        print(f"Nome: {self.__nome}")
        print(f"Cpf: {self.__cpf}")
        print(f"Alugado: {self.__alugado}")
        print(f"|------------------------|")

    


