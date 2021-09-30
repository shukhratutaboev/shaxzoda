class Nuqta:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def gachaMasofa(self, nuqta):  #ushbu method boshqa bir nuqta qabul qiladi joriy nuqtadan o'sha berilgan nuqtagacha bo'lgan masofani float sifatida qaytaradi
        return ((self.x - nuqta.x)**2 + (self.y - nuqta.y)**2)**0.5