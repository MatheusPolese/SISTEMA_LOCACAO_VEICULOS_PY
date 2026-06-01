from cliente import Cliente
from veiculos import Veiculo
from aluguel import Aluguel
from garagem import Garagem
from banco_de_clientes import Banco_clientes

garagem = Garagem()
Banco_de_dados = Banco_clientes()


cliente1 = Cliente("Fulano", "111.111.111-00")
cliente2 = Cliente("Matheus", "321.321.312-00")
cliente3 = Cliente("Maria", "000.000.000-00")
Banco_de_dados.adiciona_cliente(cliente1)
Banco_de_dados.adiciona_cliente(cliente2)
Banco_de_dados.adiciona_cliente(cliente3)

veiculo1 = Veiculo("XYZ-1234","Astra","Chevrolet","2001","B","C")
veiculo2 = Veiculo("ABC-9876","Gol","Volwskwagem","2011","B","C")
veiculo3 = Veiculo("RTB-9876","Kombi","Volwskwagem","1980","B","C")
garagem.adiciona_veiculo(veiculo1)
garagem.adiciona_veiculo(veiculo2)
garagem.adiciona_veiculo(veiculo3)


Aluguel(veiculo1, cliente1)
Aluguel(veiculo1, cliente1)
Aluguel(veiculo2, cliente1)
Aluguel(veiculo3, cliente1)

print("\nmostra veiculos na garagem:")
garagem.mostrar_garagem()

print("\nmostra clientes da empresa:")
Banco_de_dados.mostra_clientes()

