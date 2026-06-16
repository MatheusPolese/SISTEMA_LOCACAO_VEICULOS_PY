from cliente import Cliente , banco_clientes, Cliente_Fisico, Cliente_juridico
from veiculos import Veiculo ,  banco_veiculos
from aluguel import Aluguel , banco_aluguel

ba = banco_aluguel()
bv = banco_veiculos()
bc = banco_clientes()
menu = 0
while (menu > 3 or menu < 1)
    print("|-------- MENU --------|")
    print("| [1] - VEICULOS       |")
    print("| [2] - CLIENTES       |")
    print("| [3] - LOCAÇÕES       |")
    print("|----------------------|")
    menu = int(input("Digite a opção: "))
    if (menu > 3 or menu < 1):
        print("Por favor! Digite uma das opções do menu")
    elif menu == 1:
        veiculos_menu = 0
        while (veiculos_menu > 3 or veiculos_menu < 1)
        print("|---- MENU VEICULOS ----|")
        print("| [1] - CADASTRAR       |")
        print("| [2] - EXIBIR INFO     |")
        print("| [3] - VERIFICA DISP   |")
        print("|-----------------------|")
        veiculos_menu = int(input("Digite a opção: "))
        if (veiculos_menu > 3 or meveiculos_menunu < 1):
            print("Por favor! Digite uma das opções do menu")
        elif veiculos_menu == 1:
            placa = str(input("Digite a placa do veiculo: "))
            modelo = str(input("Digite o modelo do veiculo: "))
            marca = str(input("Digite a marca do veiculo: "))
            ano = str(input("Digite o ano do veiculo: "))
            porte = str(input("Digite a o porte do veiculo (categoria CNH): "))
            custo_diario = float(input("Digite o custo da diaria do veiculo: "))
            veiculo1 = Veiculo(placa,modelo,marca,ano,porte,100)

    elif menu == 2:
        clientes_menu = 0
        while (clientes_menu > 3 or clientes_menu < 1)
        print("|---- MENU CLIENTES ----|")
        print("| [1] - CADASTRAR       |")
        print("| [2] - EXIBIR INFO     |")
        print("| [3] - HISTORICO       |")
        print("|-----------------------|")
        clientes_menu = int(input("Digite a opção: "))
    elif menu == 3:
        loc_menu = 0
        while (loc_menu > 3 or loc_menu < 1)
        print("|---- MENU LOCACOES ----|")
        print("| [1] - ORÇAR LOC       |")
        print("| [2] - ALOCAR          |")
        print("| [3] - VERIFICA DISP   |")
        print("|-----------------------|")
        loc_menu = int(input("Digite a opção: "))
    






veiculo1 = Veiculo("XYZ-1234","Astra","Chevrolet","2001","B",100)
veiculo2 = Veiculo("ABC-9876","Gol","Volwskwagem","2011","B",120)
veiculo3 = Veiculo("RTB-9876","Kombi","Volwskwagem","1980","B",100)
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
