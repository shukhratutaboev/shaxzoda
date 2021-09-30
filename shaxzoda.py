from nuqta import Nuqta
from aylana import Aylana
class Shaxzoda:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.start = Nuqta(x1, y1)
        self.end = Nuqta(x2, y2)

    def kesibUtadimi(self, aylana: Aylana):  
        if aylana.niIchidami(self.start) and aylana.niIchidami(self.end):  #Tayyor metodlardan foydalanamiz
            return False
        elif aylana.niIchidami(self.start) or aylana.niIchidami(self.end):
            return True
        else:
            return False