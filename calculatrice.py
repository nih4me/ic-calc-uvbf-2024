class Calculatrice:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f'{self.nombre1} + {self.nombre2} = {resultat}')
        return resultat
    
    def division(self):
        if self.nombre2 == 0:
            return "Erreur"
        resultat = self.nombre1 / self.nombre2
        print(f'{self.nombre1} / {self.nombre2} = {resultat}')
        return resultat