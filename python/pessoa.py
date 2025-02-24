class Pessoa:
  def __init__(self, nome, ano_nascimento):
    self.nome = nome
    self.ano_nascimento = ano_nascimento
    
  def idade(self, ano_atual):
    return ano_atual - self.ano_nascimento

p1 = Pessoa("Felipe", 1995)

print(p1.nome)
print(p1.ano_nascimento) 

print(p1.idade(2025))