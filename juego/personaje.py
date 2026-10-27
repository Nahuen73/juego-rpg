class personaje:

  def __init__(self,vida,mana,nomp,abilidad, nivel, xp):
    self.vida = vida
    self.mana = mana
    self.nomp = nomp
    self.abilidad = abilidad
    self.nivel = 0
    self.xp = xp

  def saludar(self):
    return f'Hola, me llamo {self.nomp}'
  def atacar():
    pass