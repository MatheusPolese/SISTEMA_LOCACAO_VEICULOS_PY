from cliente import Cliente
from veiculos import Veiculo
from aluguel import Aluguel


print(f"------------------------")
cliente1 = Cliente("Fulano", "111.111.111-00")
print(f"Nome: {cliente1.nome}")
print(f"Cpf: {cliente1.cpf}")
print(f"codigo: {cliente1.codigo}")
print(f"Alugado: {cliente1.alugado}")
print(f"------------------------")
print(f"------------------------")
veiculo1 = Veiculo("XYZ-1234","Astra","2001","B","C")
print(f"Placa: {veiculo1.placa}")
print(f"Modelo: {veiculo1.modelo}")
print(f"Ano: {veiculo1.ano}")
print(f"Modalidade: {veiculo1.modalidade}")
print(f"Categoria: {veiculo1.categoria}")
print(f"Alugado: {veiculo1.alugado}")
print(f"------------------------")

Aluguel(veiculo1, cliente1)

print(f"------------------------")
print(f"Status cliente alugado: {cliente1.alugado}")
print(f"Status veiculo alugado: {veiculo1.alugado}")
print(f"------------------------")