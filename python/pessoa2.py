class Animal:
  def fazerBarulho(self):
    print("Barulho genérico")
    
  def andar(self):
    print("andou 1 espaço")

class Pessoa(Animal):
  def __init__(self, nome, ano_nascimento):
    super().__init__()
    self.nome = nome
    self.ano_nascimento = ano_nascimento
    
  def idade(self, ano_atual):
    return ano_atual - self.ano_nascimento
    
  def fazerBarulho(self):
    print("Falar")

p1 = Pessoa("Felipe", 1995)

print(p1.nome)
print(p1.ano_nascimento) 

print(p1.idade(2025))

p1.fazerBarulho()
p1.andar()
