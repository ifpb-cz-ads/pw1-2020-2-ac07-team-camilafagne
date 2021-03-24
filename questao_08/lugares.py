class Cidade:
  def __init__(self, cidade):
    self.cidade = cidade

  def mostra(self):
    print(self.cidade)

class Estado(Cidade):
  def __init__(self, cidade, sigla, nome_estado):
    Cidade.__init__(self, cidade)
    self.cidade = cidade.cidade
    self.sigla = sigla
    self.nome_estado = nome_estado
  
  def mostra(self):
    print(self.cidade, self.sigla, self.nome_estado)
    
  def soma(self):
    somando = 0
    for x in self.cidade:  
      if type(x) == int:
        somando = somando + x
    print("A soma da população do Estado da %s: %d" % (self.nome_estado,somando))