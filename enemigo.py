class Enemigo:

    def __init__(self, nivel, vida, defensa, ataque):
        self.niv = nivel
        self.vida = vida
        self.defn = defensa
        self.atk = ataque

    def atacar(self, objetivo):
        objetivo.vida = objetivo.vida - (self.atk/ 100 * objetivo.defensa)
        print(objetivo.vida)
