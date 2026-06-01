from cliente import Cliente 

class Banco_clientes:
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
