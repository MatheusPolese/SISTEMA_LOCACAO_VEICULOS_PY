from cliente import Cliente , banco_clientes, Cliente_Fisico, Cliente_juridico
from veiculos import Veiculo ,  banco_veiculos
from aluguel import Aluguel , banco_aluguel
#from Banco_veiculos import banco_veiculos
#from Banco_clientes import banco_clientes

ba = banco_aluguel()
bv = banco_veiculos()
bc = banco_clientes()


veiculo1 = Veiculo("XYZ-1234","Astra","Chevrolet","2001","B","C")
veiculo2 = Veiculo("ABC-9876","Gol","Volwskwagem","2011","B","C")
veiculo3 = Veiculo("RTB-9876","Kombi","Volwskwagem","1980","B","C")
bv.adiciona_veiculo(veiculo1)
bv.adiciona_veiculo(veiculo2)
bv.adiciona_veiculo(veiculo3)

cliente = Cliente_Fisico("Matheus", "321.321.312-00")
cliente1 = Cliente_juridico("Empresa", "000.000.000/1000-00")
bc.adiciona_cliente(cliente)
bc.adiciona_cliente(cliente1)

aluguel1 = Aluguel(veiculo1, cliente,  ba, "2/6/2026","12/6/2026")
aluguel2 = Aluguel(veiculo1, cliente1, ba, "11/6/2026","23/6/2026")

cliente.exibir_cliente()
veiculo1.exibir_veiculo()

bc.mostra_clientes()
ba.mostra_alugueis()
bv.mostrar_garagem()
