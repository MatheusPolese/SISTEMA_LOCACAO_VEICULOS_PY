from cliente import Cliente
from veiculos import Veiculo
from datetime import datetime

class banco_aluguel:
    def __init__(self):
        self.__banco_dados_locacoes = []
        
    def lista_locacoes(self):
         return self.__banco_dados_locacoes
    
    def adiciona_locacao(self, loc):
        self.__banco_dados_locacoes.append(loc)


    def mostra_alugueis(self):
        print("Lista dos alugueis:")
        print("------------------------")
        for loc in  self.__banco_dados_locacoes:
                print(f"| Veiculo {loc.veiculo.modelo} | Cliente {loc.cliente.nome} | Data retirada: {loc.data_retirada} | Data retirada: {loc.data_devolucao}")
        print("------------------------")



class Aluguel:
    def __init__(self, veiculo, cliente, ba, data_retirada, data_devolucao):
        self.__veiculo = veiculo
        self.__cliente = cliente
        self.__ba = ba ##banco de dados dos alugueis
        self.__data_retirada = self.__validar_data(data_retirada)
        self.__data_devolucao = self.__validar_data(data_devolucao)
        ##self.__seguro = False



        disp = True
        locacoes = ba.lista_locacoes()
        for alg in locacoes:
            if alg.veiculo.placa == veiculo.placa:
                #print("cheguei aqui")
                nomeV = veiculo.modelo
                dI = alg.data_retirada 
                dF = alg.data_devolucao 
                #print(f"data inicio carro anterior{dI}")
                #print(f"data fim carro anterior{dF}")
                #print(data_retirada)
                #print(data_devolucao)
                if ((dI <= data_retirada <= dF)  or  (dI <= data_devolucao <= dF) or (data_retirada <= dI <= data_devolucao) or (data_retirada <= dF <= data_devolucao) ):
                    print (f"O veiculo {nomeV} esta indisponivel do periodo de {dI} até {dF}")
                    disp = False
                    
                else:
                    disp = True

        if (disp == True):
            print (f"O veiculo {veiculo.modelo} esta disponivel do periodo de {data_retirada} até {data_devolucao} e esta agendada a locacao")
            ba.adiciona_locacao(self)
            cliente.alugado = True

            ##verificar se carro ja esta alugado e mudar para cliente poder alugar 1 ou mais carros
    

    def __validar_data(self,data):
        try:
            dataFormatada = datetime.strptime(data, "%d/%m/%Y")
            return dataFormatada
        except ValueError:
            raise ValueError(f"Por favor digite uma data no padrão brasileiro dd/mm/aaaa")

    @property
    def data_retirada(self):
        return self.__data_retirada.strftime("%d/%m/%Y")
    
    @property
    def data_devolucao(self):
        return self.__data_devolucao.strftime("%d/%m/%Y")  ##colocar para padrao brasileiro
    
    @property
    def veiculo(self):
        return self.__veiculo
        
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def ba(self):
        return self.__ba
    ##Adicionar função de agendar aluguel
    