from lugares import Cidade
from lugares import Estado


cidade_1 = Cidade(['Triunfo', 9464 , 'Sousa', 65803, 'Cajazeiras', 58446])

cidade_2 = Cidade(['Natal', 890480, 'Pau dos Ferros', 30600, 'Mossoró', 300618])


cidade_3 = Cidade(['Cascavel', 72232, 'Fortaleza', 2687000,'Beberibe', 53949])

estado_1 = Estado(cidade_1,'PB','Paraíba')

estado_2 = Estado(cidade_2,'RN','Rio Grande do Norte')
estado_3 = Estado(cidade_3, 'CE', 'Ceará')

estado_1.soma()

estado_2.soma()

estado_3.soma()
