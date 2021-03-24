class Televisão:
     def __init__(self):
           self.ligada = False
           self.canal = 2
           self.tamanho = 40
           self.marca = 'LG'
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1

tv_1 = Televisão()
tv_1.tamanho = 32
tv_1.marca = 'Philco'

tv_2 = Televisão()
tv_2.tamanho = 50
tv_2.marca= 'Sony'

print("1- Marca = %s, tamanho = %s" % (tv_1.marca, tv_1.tamanho))
print("2- Marca = %s, tamanho = %s" % (tv_2.marca, tv_2.tamanho))