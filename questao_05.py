class Televisão:
     def __init__(self, canal_inicializa, min=2, max=14): #parametros no construtor
         self.ligada = False
         self.canal = canal_inicializa
         self.cmin = min
         self.cmax = max
     def muda_canal_para_baixo(self):
        if(self.canal < self.cmin):
              self.canal = self.cmax
       
     def muda_canal_para_cima(self):
         if(self.canal > self.cmax):
               self.canal = self.cmin
         

tv=Televisão(5,4,20)
tv.muda_canal_para_baixo()
print(tv.canal)

tv_2=Televisão(11, 3, 10)
tv_2.muda_canal_para_baixo()
print(tv_2.canal)
