from aluguel import Aluguel 
from cliente import Cliente
from veiculos import Veiculo

class banco_aluguel:
    def __init__(self):
        self.__lista_dos_alugueis = []
        
    def adiciona_locacao(self, aluguel):
        self.__lista_dos_alugueis.append(aluguel)

    def verifica_disponibilidade(self, aluguel_novo, dataI, dataF, disp): 
        for alugueis_p in self.__lista_dos_alugueis:
            if alugueis_p.veiculo.placa == aluguel_novo.placa:
                nomeV = aluguel_novo.veiculo.modelo
                dI = alugueis_p.data_retirada 
                dF = alugueis_p.data_devolucao 
                if (dI <= dataI <= dF  and  dI <= dataF <= dF):
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
