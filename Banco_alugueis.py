from aluguel import Aluguel 
from cliente import Cliente
from veiculos import Veiculo

class banco_aluguel:
    def __init__(self):
        self.__lista_dos_alugueis = []
        
    def lista_locacoes(self):
         return self.__lista_dos_alugueis
    
    def adiciona_locacao(self, locacao):
        self.__lista_dos_alugueis.append(locacao)

    def verifica_disponibilidade(self, aluguel_novo, dataI, dataF, disp): 
        for alg in self.__lista_dos_alugueis:
            if alg.veiculo.placa == aluguel_novo.placa:
                nomeV = aluguel_novo.veiculo.modelo
                dI = alg.data_retirada 
                dF = alg.data_devolucao 
                if ((dI <= dataI <= dF)  or  (dI <= dataF <= dF) or (dataI <= dI <= dataF) or (dataI <= dF <= dataF) ):
                     print (f"O veiculo {nomeV} esta indisponivel do periodo de {dI} até {dF}")
                     disp = False
        print (f"O veiculo {nomeV} esta disponivel do periodo de {dataI} até {dataF}")
        disp = True


    def mostra_alugueis(self):
        print("Lista dos alugueis:")
        print("------------------------")
        for aluguel in  self.__lista_dos_alugueis:
                print(f"| Veiculo {aluguel.veiculo.modelo} | Cliente {aluguel.cliente.nome} | Data retirada: {aluguel.data_retirada} | Data retirada: {aluguel.data_devolucao}")
        print("------------------------")
