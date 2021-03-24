from clientes import Cliente
from contas import ContaEspecial

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta1 = ContaEspecial([joão], 1, 1000, 1500)
conta1.extrato()

conta2 = ContaEspecial([maria], 2, 500, 1000)
conta2.extrato()



