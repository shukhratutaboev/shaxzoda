class Nuqta:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def gachaMasofa(self, nuqta):
        return ((self.x - nuqta.x)**2 + (self.y - nuqta.y)**2)**0.5