from cliente import Cliente
from veiculos import Veiculo
from aluguel import Aluguel
from garagem import Garagem

cliente1 = Cliente("Fulano", "111.111.111-00")
cliente1.exibir_cliente()
veiculo1 = Veiculo("XYZ-1234","Astra","Chevrolet","2001","B","C")
veiculo1.exibir_veiculo()
veiculo2 = Veiculo("ABC-9876","Gol","Volwskwagem","2011","B","C")
veiculo2.exibir_veiculo()
garagem1 = Garagem()
garagem1.adiciona_veiculo(veiculo1)
garagem1.adiciona_veiculo(veiculo2)
Aluguel(veiculo1, cliente1)
garagem1.mostrar_garagem()
garagem1.mostrar_alugados()





