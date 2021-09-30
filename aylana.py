from nuqta import Nuqta

class Aylana:
    def __init__(self, x, y, r) -> None:
        self.markaz = Nuqta(x, y)
        self.radius = r

    def niIchidami(self, nuqta: Nuqta):
        if self.markaz.gachaMasofa(nuqta) > self.radius:  #Tayyor metodlardan foydalanamiz
            return False
        else:
            return True