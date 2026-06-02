from cliente import Cliente
from veiculos import Veiculo
from aluguel import Aluguel
from Banco_veiculos import banco_veiculos
from Banco_clientes import banco_clientes
from Banco_alugueis import banco_aluguel


bv = banco_veiculos()
bc = banco_clientes()
ba = banco_aluguel()


cliente1 = Cliente("Fulano", "111.111.111-00")
cliente2 = Cliente("Matheus", "321.321.312-00")
cliente3 = Cliente("Maria", "000.000.000-00")
bc.adiciona_cliente(cliente1)
bc.adiciona_cliente(cliente2)
bc.adiciona_cliente(cliente3)

veiculo1 = Veiculo("XYZ-1234","Astra","Chevrolet","2001","B","C")
veiculo2 = Veiculo("ABC-9876","Gol","Volwskwagem","2011","B","C")
veiculo3 = Veiculo("RTB-9876","Kombi","Volwskwagem","1980","B","C")
bv.adiciona_veiculo(veiculo1)
bv.adiciona_veiculo(veiculo2)
bv.adiciona_veiculo(veiculo3)

aluguel1 = Aluguel(veiculo1, cliente1, "2/6/2026","12/6/2026")
aluguel2 = Aluguel(veiculo1, cliente1, "3/6/2026","2/7/2026")
aluguel3 = Aluguel(veiculo2, cliente1, "24/6/2026","12/9/2026")
aluguel4 = Aluguel(veiculo3, cliente1, "2/6/2026","12/10/2026")

ba.adiciona_locacao(aluguel1)
ba.adiciona_locacao(aluguel2)
ba.adiciona_locacao(aluguel3)
ba.adiciona_locacao(aluguel4)


print("\nmostra veiculos na garagem:")
bv.mostrar_garagem()

print("\nmostra clientes da empresa:")
bc.mostra_clientes()

print("\nmostra alugueis da empresa:")
ba.mostra_alugueis()

