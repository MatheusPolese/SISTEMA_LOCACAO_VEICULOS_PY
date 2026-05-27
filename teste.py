from cliente import Cliente
from veiculos import Veiculo
from aluguel import Aluguel
from garagem import Garagem

print("\nCria cliente 1:")
cliente1 = Cliente("Fulano", "111.111.111-00")
cliente1.exibir_cliente()

print("\nCria cliente 2:")
cliente2 = Cliente("Matheus", "321.321.312-00")
cliente2.exibir_cliente()

print("\nCria Veiculo 1:")
veiculo1 = Veiculo("XYZ-1234","Astra","Chevrolet","2001","B","C")
veiculo1.exibir_veiculo()

print("\nCria Veiculo 2:")
veiculo2 = Veiculo("ABC-9876","Gol","Volwskwagem","2011","B","C")
veiculo2.exibir_veiculo()

print("\nCria garagem:")
garagem1 = Garagem()
garagem1.adiciona_veiculo(veiculo1)
garagem1.adiciona_veiculo(veiculo2)
print("\nmostra garagem:")
garagem1.mostrar_garagem()

print("\ncliente 1 tenta alugar veiculo 1:")
Aluguel(veiculo1, cliente1)


print("\ncliente 2 tenta alugar veiculo 1:")
Aluguel(veiculo1, cliente2)


print("\nmostra dados do veiculo 1:")
veiculo1.exibir_veiculo()

print("\nmostra veiculos na garagem:")
garagem1.mostrar_garagem()

print("\nmostra veiculos alugados:")
garagem1.mostrar_alugados()





