from clientes import Cliente
from contas import Conta

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta1 = Conta([joão], 1, 1000)
conta2 = Conta([maria, joão], 2, 500)


conta1.extrato()
retirou = conta1.saque(1150)
if retirou == True:
  print('Saque realizado com sucesso')

conta2.deposito(300)
conta2.extrato()
retirou2 = conta2.saque(250)
if retirou2 == True:
  print('Saque realizado com sucesso')
