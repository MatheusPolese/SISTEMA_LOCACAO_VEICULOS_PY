import random

class Cliente:
    def __init__(self, nome, cpf):
        self.__codigo = f"{random.randint(0, 9999):04d}"##atruibir codigo aleatorio
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

    @property
    def codigo(self):
        return self.__codigo ##atruibir codigo aleatorio
    

    def exibir_cliente(self):
        print(f"|-----Ficha Cliente-----|")
        print(f"Nome: {self.__nome}")
        print(f"Cpf: {self.__cpf}")
        print(f"codigo: {self.__codigo}")
        print(f"Alugado: {self.__alugado}")
        print(f"|------------------------|")

    


