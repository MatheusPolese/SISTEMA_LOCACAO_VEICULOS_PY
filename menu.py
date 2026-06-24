from cliente import Cliente , banco_clientes, Cliente_Fisico, Cliente_juridico
from veiculos import banco_veiculos, CriadorSUV, CriadorVAN, CriadorEconomico
from aluguel import Aluguel , banco_aluguel


ba = banco_aluguel()
bv = banco_veiculos()
bc = banco_clientes()


veiculo1 = CriadorVAN().addveiculo("XYZ-1234","Sprinter","Mercedes-Benz","2017","C")
veiculo3 = CriadorSUV().addveiculo("RTB-9876","Kicks","Nissan","2020","B")
veiculo2 = CriadorSUV().addveiculo("ABC-9876","Gol","Volwskwagem","2011","B")

bv.adiciona_veiculo(veiculo1)
bv.adiciona_veiculo(veiculo2)
bv.adiciona_veiculo(veiculo3)

cliente = Cliente_Fisico("Matheus","matheus@gmail.com","321.321.312-00")
cliente1 = Cliente_juridico("Empresa","empresa@gmail.com","000.000.000/1000-00")
bc.adiciona_cliente(cliente)
bc.adiciona_cliente(cliente1)
aluguel2 = Aluguel(veiculo1, cliente,  ba, "26/6/2026", "5/7/2026")

menu = 0
while (menu > 3 or menu < 1):
    print("\n|-------- MENU --------|")
    print("| [1] - VEICULOS       |")
    print("| [2] - CLIENTES       |")
    print("| [3] - LOCAÇÕES       |")
    print("|----------------------|")
    menu = int(input("Digite a opção: "))
    if (menu > 3 or menu < 1):
        print("Por favor! Digite uma das opções do menu")
    elif menu == 1:
        veiculos_menu = 0
        while (veiculos_menu > 3 or veiculos_menu < 1):
            print("|---- MENU VEICULOS ----|")
            print("| [1] - CADASTRAR       |")
            print("| [2] - EXIBIR INFO     |")
            print("|-----------------------|")
            veiculos_menu = int(input("Digite a opção: "))
            if (veiculos_menu > 3 or veiculos_menu < 1):
                print("Por favor! Digite uma das opções do menu")
            elif veiculos_menu == 1:
                tipo_veiculo = 0
                while (tipo_veiculo > 3 or tipo_veiculo < 1):
                    print("|ESCOLHA A OPÇÃO DO TIPO|")
                    print("| [1] - VAN             |")
                    print("| [2] - SUV             |")
                    print("| [3] - ECONOMICO       |")
                    print("|-----------------------|")
                    tipo_veiculo = int(input("Digite a opção: "))
                    if tipo_veiculo == 1:
                        placa = str(input("Digite a placa do veiculo: "))
                        modelo = str(input("Digite o modelo do veiculo: "))
                        marca = str(input("Digite a marca do veiculo: "))
                        ano = str(input("Digite o ano do veiculo: "))
                        porte = str(input("Digite a o porte do veiculo (categoria CNH): "))
                        van = CriadorVAN().addveiculo(placa,modelo,marca,ano,porte)
                        bv.adiciona_veiculo(van)
                        print("Veiculo cadastrado com sucesso!")
                        menu = 0
                    elif tipo_veiculo == 2:
                        placa = str(input("Digite a placa do veiculo: "))
                        modelo = str(input("Digite o modelo do veiculo: "))
                        marca = str(input("Digite a marca do veiculo: "))
                        ano = str(input("Digite o ano do veiculo: "))
                        porte = str(input("Digite a o porte do veiculo (categoria CNH): "))
                        suv = CriadorSUV().addveiculo(placa,modelo,marca,ano,porte)
                        bv.adiciona_veiculo(suv)
                        print("Veiculo cadastrado com sucesso!")
                        menu = 0
                    elif tipo_veiculo == 3:
                        placa = str(input("Digite a placa do veiculo: "))
                        modelo = str(input("Digite o modelo do veiculo: "))
                        marca = str(input("Digite a marca do veiculo: "))
                        ano = str(input("Digite o ano do veiculo: "))
                        porte = str(input("Digite a o porte do veiculo (categoria CNH): "))
                        economico = CriadorEconomico().addveiculo(placa,modelo,marca,ano,porte)
                        bv.adiciona_veiculo(economico)
                        print("Veiculo cadastrado com sucesso!")
                        menu = 0               
            elif veiculos_menu == 2:
                placa = str(input("Digite a placa do veiculo: "))
                bv.exibir_veiculo(placa)
                menu = 0             
    elif menu == 2:
        clientes_menu = 0
        while (clientes_menu > 3 or clientes_menu < 1):
            print("|-------- MENU CLIENTES --------|")
            print("| [1] - CADASTRAR FISICO        |")
            print("| [2] - CADASTRAR JURIDICO      |")            
            print("| [3] - EXIBIR INFO HISTORICO   |")
            print("|-------------------------------|")
            clientes_menu = int(input("Digite a opção: "))
            if (clientes_menu > 3 or clientes_menu < 1):
                print("Por favor! Digite uma das opções do menu")

            elif clientes_menu == 1:
                nome = str(input("Digite o nome do cliente: "))
                email = str(input("Digite o E-mail do cliente: "))
                cpf = str(input("Digite o cpf do cliente: "))
                cliente = Cliente_Fisico(nome,email , cpf)
                bc.adiciona_cliente(cliente)
                print("Cliente cadastrado com sucesso!")
                menu = 0 

            elif clientes_menu == 2:
                nome = str(input("Digite o nome da empresa: "))
                email = str(input("Digite o E-mail do cliente: "))
                cnpj = str(input("Digite o cpnj do cliente: "))
                cliente = Cliente_juridico(nome, email, cnpj)
                bc.adiciona_cliente(cliente)
                print("Cliente cadastrado com sucesso!")
                menu = 0 

            elif clientes_menu == 3:
                id = str(input("Digite o cpf ou cnpj do cliente: "))
                clienteinfo = bc.procura_cliente(id)
                bc.exibir_info(clienteinfo)
                menu = 0  

    elif menu == 3:
        print("|---- OPÇÕES DE ALOCAÇÃO ----|")
        i = bv.mostrar_garagem(ba)
        op = 0
        while (0 <= op or op > i):
            op = int(input("Escolha o veiculo: "))
            veiculo = bv.procura_veiculo(op)    
            data1 = str(input("Digite a data de retirada: "))
            data2 = str(input("Digite a data de devolução: "))
            doc = str(input("Digite seu documento: "))
            cliente = bc.procura_cliente(doc)  
            if cliente == 0:
                menu = 0
                op =-1
                break   
            if menu != 0:  
                aluguel1 = Aluguel(veiculo, cliente,  ba, data1, data2)
            op =-1
            menu = 0
            
        




        